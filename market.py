# 导入必要的库
import numpy as np
import pandas as pd
import tushare as ts
from dotenv import load_dotenv, find_dotenv
import os
import datetime

# 初始化Tushare接口
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
pro=ts.pro_api(os.environ.get("TUSHARE_API_KEY"))
stock_list=pd.read_csv(os.path.join(os.getcwd(), "stock_list.csv"), dtype={"symbol":str})
stock_list.set_index("symbol", inplace=True)

def symbol_to_ts_code(symbol:str)->str:
    return stock_list.loc[symbol, 'ts_code']
def get_stock_name(symbol:str)->str:
    return stock_list.loc[symbol, "name"]

# 将股票代码转换为ts_code，方便后续获取数据
def get_market_data(
        ts_code:str, 
        date:pd.Timestamp=pd.Timestamp(datetime.datetime.today()),
        pro:ts.pro_api=pro
        )->pd.DataFrame:
    # 获取过去3个月的市场数据
    start_date=(date-pd.DateOffset(months=6)).strftime("%Y%m%d")
    end_date=date.strftime("%Y%m%d")
    df:pd.DataFrame = pro.daily(**{
        "ts_code": ts_code,
        "trade_date": "",
        "start_date": start_date,
        "end_date": end_date,
        "limit": "",
        "offset": ""
    }, fields=[
        "trade_date",
        "open",
        "high",
        "low",
        "close",
        "pre_close",
        "pct_chg",
        "vol",   
    ])
    turnover:pd.DataFrame=pro.daily_basic(**{
        "ts_code": ts_code,
        "trade_date": "",
        "start_date": start_date,
        "end_date": end_date,
        "limit": "",
        "offset": ""
    }, fields=[
        "turnover_rate",
        "trade_date"
    ])
    # 整理数据
    # 合并换手率数据
    df=pd.merge(df, turnover, on="trade_date")
    # 保留 'trade_date' 列，将其余非数值型列转换为 np.nan
    cols_to_process = df.columns.difference(['trade_date'])
    df[cols_to_process] = df[cols_to_process].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    # 按日期排序
    df['trade_date']=pd.to_datetime(df['trade_date'])
    df.sort_values(by="trade_date", ascending=True, inplace=True)
    
    # 1. 移动平均线
    df['ma5'] = df['close'].rolling(window=5).mean()
    df['ma20'] = df['close'].rolling(window=20).mean()
    df['ma60'] = df['close'].rolling(window=60).mean()
    # 2. 计算波动率（20日年化波动率、14日ATR）
    df['vol_20d'] = df['pct_chg'].rolling(window=20).std() * np.sqrt(252)
    df['TR'] = df[['high', 'low', 'pre_close']].apply(lambda x: max(x['high'] - x['low'], abs(x['high'] - x['pre_close']), abs(x['low'] - x['pre_close'])), axis=1)
    df['ATR_14d'] = df['TR'].rolling(window=14).mean()
    # 重命名列名
    df.rename(columns={
        "trade_date": "日期",
        "open": "开盘价",
        "high": "最高价",
        "low": "最低价",
        "close": "收盘价",
        "pct_chg":"涨跌幅",
        "vol":"成交量",
        "turnover_rate": "换手率"
    },
    inplace=True)  
    
    # 重新排列列顺序
    columns_order = [
        "日期", "开盘价", "最高价", "最低价", 
        "收盘价", "涨跌幅", "成交量", "换手率",
        "ma5", "ma20", "ma60",
        "vol_20d", "ATR_14d"
    ]
    df = df[columns_order]
    # 仅筛选最近5个交易日的数据
    df.sort_values(by="日期", ascending=False, inplace=True)
    df = df.iloc[:5]
    return df

def market_analysis(symbol:str)->str:
    ts_code=symbol_to_ts_code(symbol)
    df=get_market_data(ts_code)
    result=f'''
    股票代码：{symbol}，{get_stock_name(symbol)}过去5个交易日的市场表现：

    {df.to_markdown(index=False, floatfmt='.3f')}
    '''
    return result

if __name__=="__main__":
    print(market_analysis('000001'))