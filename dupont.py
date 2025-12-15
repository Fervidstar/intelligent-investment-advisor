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
def get_dupont_data(
        ts_code:str, 
        date:pd.Timestamp=pd.Timestamp(datetime.datetime.today()),
        pro:ts.pro_api=pro
        )->pd.DataFrame:
    # 获取过去三年的财务数据
    start_date=(date-pd.DateOffset(years=5)).strftime("%Y%m%d")
    end_date=date.strftime("%Y%m%d")
    df:pd.DataFrame = pro.fina_indicator(**{
        "ts_code": ts_code,
        "ann_date": "",
        "start_date": start_date,
        "end_date": end_date,
        "period": "",
        "update_flag": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "end_date",
        "update_flag",
        "roe",
        "profit_to_gr",
        "dp_assets_to_eqt",
        "assets_turn"
    ])
    # 整理数据
    # 保留 'trade_date' 列，将其余非数值型列转换为 np.nan
    cols_to_process = df.columns.difference(['end_date'])
    df[cols_to_process] = df[cols_to_process].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    df=df.sort_values(by=['end_date', 'update_flag'], ascending=[False, False])
    df=df.drop_duplicates(subset=['end_date'])
    df=df.drop(columns=['update_flag'])
    df['end_date']=pd.to_datetime(df['end_date'])
    # 筛选年报数据
    df=df.loc[df['end_date'].dt.month==12]
    df=df.iloc[:3]
    df['end_date']=df['end_date'].dt.year
    # 重命名列名
    df.rename(columns={
        "end_date": "年份",
        "roe": "净资产收益率",
        "profit_to_gr": "净利润率",
        "dp_assets_to_eqt": "权益乘数",
        "assets_turn": "总资产周转率"
    },
    inplace=True)  
    return df

def dupont_analysis(symbol:str)->str:
    ts_code=symbol_to_ts_code(symbol)
    df=get_dupont_data(ts_code)
    result=f'''
    股票代码：{symbol}，{get_stock_name(symbol)}过去三年年报中的杜邦分析法所需财务指标：

    {df.to_markdown(index=False, floatfmt='.3f')}
    '''
    return result