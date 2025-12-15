import react_search_agent
from agentscope.agent import ReActAgent, UserAgent
from agentscope.message import Msg
from agentscope.pipeline import MsgHub, sequential_pipeline, fanout_pipeline
import asyncio
import agentscope
import os
# 引入输入处理函数
from input_processing import similarity, market_agent_msg, eval_agent_msg, macro_agent_msg
# 引入提示词
from prompts import *
# 引入Agent类
from react_search_agent import react_search_agent
from debate_agent import debate_agent
from judge_agent import Judge_agent

# 初始化agentscope，并注册至agentscope_studio
agentscope.init(
    project="Multi-Agent Stock Analysis System",
    name="Multi-Agent Stock Analysis System",
    studio_url="http://localhost:3000",
)

# 创建multi-agent system所使用的agent
# 1. 创建3个research_agent
# （1）市场Agent：根据市场数据、估值情况与消息面预测短期市场趋势
market_agent=react_search_agent(name="market_agent",sys_prompt=market_agent_prompt)
# （2）估值Agent：根据估值情况、杜邦分析法数据进行调研，预测长期趋势
eval_agent=react_search_agent(name="eval_agent",sys_prompt=eval_agent_prompt)
# （3）宏观与行研Agent：调研宏观市场环境与行业发展趋势
macro_and_industry_agent=react_search_agent(name="macro_and_industry_agent",sys_prompt=macro_and_industry_agent_prompt)
# 2. 创建debate_agent：根据summary agent的客观报告，分为看多方与看空方进行辩论
bullish_agent=debate_agent(name="bullish_agent",sys_prompt=bullish_agent_prompt)
bearish_agent=debate_agent(name="bearish_agent",sys_prompt=bearish_agent_prompt)
# 3. 创建judge_agent：作为辩论的主持人，评价并形成最终报告
judge_agent=Judge_agent(name="judge_agent",sys_prompt=judge_agent_prompt)

# 合并3个research_agent的输出作为summary_agent的输入
def merge_research_outputs(market_msg: Msg, eval_msg: Msg, macro_and_industry_msg: Msg) -> Msg:
    """
    Merge the outputs from three research agents into a single message
    for the summary agent.
    
    Args:
        market_msg (Msg): Output from research_react_agent_1
        eval_msg (Msg): Output from research_react_agent_2  
        macro_and_industry_msg (Msg): Output from research_react_agent_3
        
    Returns:
        Msg: Combined message containing all three research outputs
    """
    combined_content = (
        f"# 市场数据、估值情况与股票消息面的调研结果:\n{market_msg.get_text_content()}\n\n"
        f"# 估值情况、杜邦分析法与企业长期发展趋势的调研结果:\n{eval_msg.get_text_content()}\n\n"
        f"# 宏观市场环境与行业发展趋势的调研结果:\n{macro_and_industry_msg.get_text_content()}"
    )
    
    
    return Msg(
        name="research_merge",
        content=combined_content,
        role="user"
    )

# debate system
async def run_debate_with_judge(initial_summary: Msg, max_rounds: int = 5) -> Msg:
    """
    Run a multi-round debate between two debate agents with a judge agent
    that determines when to end the debate and provides the final summary.
    
    Args:
        initial_summary (Msg): The initial summary from the summary agent
        max_rounds (int): Maximum number of debate rounds to prevent infinite loops
        
    Returns:
        Msg: Final output from the judge agent containing the debate summary
    """
    # Initialize debate history with the initial summary
    debate_history = [initial_summary]
    
    # Create a message hub for the debate participants
    async with MsgHub(
        participants=[bullish_agent, bearish_agent, judge_agent],
        announcement=initial_summary
    ) as hub:
        
        round_count = 0
        debate_ended = False
        
        while not debate_ended and round_count < max_rounds:
            # Start a new debate round
            round_count += 1
            
            # Get responses from both debate agents
            response1 = await bullish_agent()
            response2 = await bearish_agent()
            
            # Add responses to debate history
            debate_history.extend([response1, response2])
            
            # Ask judge if debate should continue
            judge_input = Msg(
                name="judge_input",
                content=(
                    f"Current debate round: {round_count}\n"
                    f"Debate history:\n"
                    f"{'-' * 50}\n"
                    f"{''.join([f'{msg.name}: {msg.get_text_content()}\n\n' for msg in debate_history])}"
                    f"{'-' * 50}\n"
                    "Based on the current state of the debate, should it continue? "
                    "If yes, respond with 'CONTINUE'. If the debate has reached a conclusion "
                    "or sufficient depth, respond with 'END' followed by your final summary "
                    "of the key points discussed."
                ),
                role="user"
            )
            
            judge_response = await judge_agent(judge_input)
            judge_text = judge_response.get_text_content()
            
            if judge_text and "END" in judge_text.upper():
                debate_ended = True
                # Extract the summary part after "END"
                if "END" in judge_text:
                    summary_start = judge_text.find("END") + len("END")
                    final_summary = judge_text[summary_start:].strip()
                    if not final_summary:
                        final_summary = judge_text
                else:
                    final_summary = judge_text
                
                return Msg(
                    name="final_output",
                    content=final_summary,
                    role="assistant"
                )
            else:
                # Broadcast judge's decision to continue to both debate agents
                continue_msg = Msg(
                    name="judge",
                    content=f"Round {round_count} complete. Continue debate.",
                    role="user"
                )
                hub.broadcast(continue_msg)
        
        # If max rounds reached, force judge to provide final summary
        final_judge_input = Msg(
            name="final_judge_input",
            content=(
                f"Maximum debate rounds ({max_rounds}) reached. "
                "Please provide a comprehensive final summary of the debate."
            ),
            role="user"
        )
        final_judge_response = await judge_agent(final_judge_input)
        return final_judge_response

# multi-agent system
async def main_workflow(user_input: Msg) -> Msg:
    """
    Main workflow orchestrating the entire multi-agent system.
    
    Args:
        user_input (str): Original user input
        
    Returns:
        Msg: Final output from the judge agent
    """
    # Step 1: Process user input through three different processors
    stock_list=similarity(user_input)
    code=stock_list[0]['代码']
    # 若report目录下不存在以code命名的文件夹，则创建文件夹存放报告
    report_path=os.path.join(os.getcwd(), 'report')
    folder_path = os.path.join(report_path, code)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    market_input = market_agent_msg(stock_list)
    eval_input = eval_agent_msg(stock_list)
    macro_input = macro_agent_msg(stock_list)
    
    # Step 2: Run three research agents in parallel with their respective inputs
    market_report = await market_agent(market_input)
    eval_report = await eval_agent(eval_input)
    macro_and_industry_report = await macro_and_industry_agent(macro_input)
    research_results=[market_report, eval_report, macro_and_industry_report]
    # 输出报告
    reports_name=['market report.md', 'eval report.md', 'macro and industry report.md']
    for result, report_name in zip(research_results, reports_name):
        with open(os.path.join(folder_path, report_name), 'w', encoding='utf-8') as f:
            f.write(result.get_text_content())
    
    # Step 3: Merge research outputs
    merged_research = merge_research_outputs(
        research_results[0], 
        research_results[1], 
        research_results[2]
    )
    
    # Step 4: Run debate with judge
    final_output = await run_debate_with_judge(merged_research)
    # 输出报告
    with open(os.path.join(folder_path, 'final report.md'), 'w', encoding='utf-8') as f:
        f.write(final_output.get_text_content())
    return final_output

# 程序主体
async def main():
    user = UserAgent("User")
    # 保持程序运行以维持Studio连接
    msg = Msg(
        name='Stock_Analyst',
        role='assistant',
        content='请输入股票代码，例如：000001（默认代码）'
    )
    while True:
        msg = await user(msg)
        if msg.get_text_content() == "exit":
            break
        msg = await main_workflow(msg)

asyncio.run(main())