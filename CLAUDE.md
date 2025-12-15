# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Multi-Agent Stock Analysis System that uses AI agents to perform comprehensive stock market analysis. The system combines multiple specialized agents with financial data analysis, similarity matching, and a debate system to generate balanced stock reports.

## Architecture

### Core Components

1. **Multi-Agent System** (`main.py`)
   - Research agents: market_agent, eval_agent, macro_and_industry_agent
   - Debate agents: bullish_agent, bearish_agent
   - Judge agent for final decisions
   - Uses AgentScope framework for agent orchestration

2. **Data Processing Pipeline**
   - **Similarity Engine** (`similarity/`): Sentence-transformers based model for finding similar stocks
   - **Market Data** (`market.py`): Fetches stock price data, technical indicators via Tushare API
   - **Valuation Analysis** (`eval.py`): PE, PB, PS ratios and fundamental metrics
   - **DuPont Analysis** (`dupont.py`): Financial statement analysis for long-term trends

3. **Agent Types**
   - **React Search Agents** (`react_search_agent.py`): Web search-enabled research agents
   - **Debate Agents** (`debate_agent.py`): Optimistic/pessimistic viewpoint agents
   - **Judge Agent** (`judge_agent.py`): Uses reasoning model for balanced decisions

### Data Flow

1. User inputs stock code → similarity matching finds comparable stocks
2. Three research agents analyze market data, valuation metrics, and macro trends in parallel
3. Debate system discusses findings with bullish/bearish perspectives
4. Judge agent synthesizes into final balanced report
5. Reports saved to `report/{stock_code}/` directory

## Setup and Dependencies

### Environment Variables Required

- `DEEPSEEK_API_KEY`: For chat and reasoning models
- `TUSHARE_API_KEY`: For Chinese stock market data
- `DASHSCOPE_API_KEY`: For web search functionality

### Key Files

- `requirements.txt`: Python dependencies
- `stock_list.csv`: Chinese stock universe with symbol mappings
- `similarity/train_sentences.csv`: Training data for similarity model
- `similarity/stock_similarity_model/`: Fine-tuned sentence transformers model
- `similarity/stock_embeddings.pkl`: Cached vector embeddings

### Key Functions

- `similarity()`: Find similar stocks using sentence embeddings
- `market_analysis()`: Get market data and technical indicators
- `eval_analysis()`: Calculate valuation metrics
- `dupont_analysis()`: Perform DuPont financial analysis
- `main_workflow()`: Orchestrate the complete analysis pipeline

## Development

### Running the System

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables in .env file
# Then run the main system
python main.py
```

### Testing Individual Components

```bash
# Test market data retrieval
python market.py

# Test similarity search
python similarity/similarity.py

# Test valuation analysis
python eval.py

# Test DuPont analysis
python dupont.py
```

## Model Architecture

- **Chat Model**: DeepSeek-chat for agent interactions
- **Reasoning Model**: Deepseek-reasoner for judge agent decisions
- **Similarity Model**: BGE-small-zh-v1.5 fine-tuned on stock descriptions
- **Web Search**: Alibaba Tongyi WebSearch via MCP protocol

## Report Structure

Reports are generated in `report/{stock_code}/`:
- `market report.md`: Technical analysis and market sentiment
- `eval report.md`: Valuation and financial metrics analysis
- `macro and industry report.md`: Industry and macroeconomic context
- `final report.md`: Synthesized conclusion from debate system

## Important Notes

- Stock symbols use 6-digit Chinese format (e.g., "000001")
- Market data limited to recent 5 trading days for timely analysis
- Similarity model requires embeddings file on first run
- System uses async/await pattern for agent orchestration
- All financial data sourced via Tushare API