from agentscope.message import Msg
from similarity.similarity import StockSearchEngine
from market import market_analysis
from eval import eval_analysis
from dupont import dupont_analysis
import os
import pandas as pd
import re

# 处理股票代码的函数
current_path = os.getcwd()
stock_list=pd.read_csv(os.path.join(current_path, "stock_list.csv"), dtype={"symbol":str})
stock_list.set_index("symbol", inplace=True)

def get_stock_name(symbol:str)->str:
    return stock_list.loc[symbol, "name"]

# 提取股票代码的函数
def extract_stock_code(text):
    """
    提取字符串中第一个出现的六位数字的股票代码，若没有找到，返回'000001'
    
    Args:
        text (str): 输入的字符串
        
    Returns:
        str: 六位数字股票代码或'000001'
    """
    # 使用正则表达式匹配连续的六位数字
    match = re.search(r'\b\d{6}\b', text)
    if match:
        return match.group(0)
    else:
        return '000001'

# 形成三个research agent的输入
# 提取输入的信息中的股票代码，推理得到和它相似的股票
def similarity(msg:Msg)->list:
    # 提取输入中的股票代码
    input_text=msg.get_text_content()
    code=extract_stock_code(input_text)
    # 推理相似的股票
    similarity_engine=StockSearchEngine(
        model_path=os.path.join(current_path, 'similarity', "stock_similarity_model"), 
        data_path=os.path.join(current_path, 'similarity', "train_sentences.csv")
    )
    result=[{'代码': code, '名称': get_stock_name(code), '相似股票': get_stock_name(code)}]
    result=result+similarity_engine.search_by_code(code)
    return result

def basic_information(stock_list:list)->str:
    # 输入的第一部分：调研股票的基础信息
    result='正在调研的股票'
    result=result+f'代码：{stock_list[0]['代码']}，股票名称：{stock_list[0]['名称']}\n\n'
    result=result+f'与该股票相似的股票有：\n'
    for stock in stock_list[1:]:
        result=result+f'+ 股票代码：{stock["代码"]}，股票名称：{stock["名称"]}\n'
    return result

# （1）市场Agent：根据市场数据、估值情况与消息面预测短期市场趋势
def market_agent_msg(stock_list:list)->Msg:
    # 输入的第一部分：调研股票的基础信息
    result=basic_information(stock_list)+'\n\n'
    # 输入的第二部分：各股票的市场数据
    result=result+'''
    以下是各股票市场数据：
    -----\n
    '''
    for stock in stock_list:
        result=result+market_analysis(stock['代码'])+'\n\n'
    result=result+'-----\n\n'
    # 输入的第三部分：各股票的估值情况
    result=result+'''
    以下是各股票估值数据：
    -----\n
    '''
    for stock in stock_list:
        print(stock['代码'])
        result=result+eval_analysis(stock['代码'])+'\n\n'
    result=result+'-----\n'
    return Msg(
        name='User',
        role='user',
        content=result
    )

# （2）估值Agent：根据估值情况、杜邦分析法数据进行调研，预测长期趋势
def eval_agent_msg(stock_list:list)->Msg:
    # 输入的第一部分：调研股票的基础信息
    result=basic_information(stock_list)+'\n\n'
    # 输入的第二部分：各股票的估值情况
    result=result+'''
    以下是各股票估值数据：
    -----\n
    '''
    for stock in stock_list:
        result=result+eval_analysis(stock['代码'])+'\n\n'
    result=result+'-----\n\n'
    # 输入的第三部分：各股票的杜邦分析数据
    result=result+'''
    以下是各股票杜邦分析数据：
    -----\n
    '''
    for stock in stock_list:
        result=result+dupont_analysis(stock['代码'])+'\n\n'
    result=result+'-----\n'
    return Msg(
        name='User',
        role='user',
        content=result
    )
# （3）宏观与行研Agent：调研宏观市场环境与行业发展趋势
def macro_agent_msg(stock_list:list)->Msg:
    # 输入的第一部分：调研股票的基础信息
    result=basic_information(stock_list)
    return Msg(
        name='User',
        role='user',
        content=result
    )

if __name__ == '__main__':
    msg=Msg(
        name='User',
        content='300750',
        role='user'
    )
    similarity_list=similarity(msg)
    print(market_agent_msg(similarity_list).content)
    print(eval_agent_msg(similarity_list).content)
    print(macro_agent_msg(similarity_list).content)