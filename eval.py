# 获取股票当前的估值指标：市盈率、市净率、市销率、股息率、股票价值倍数（EV/EBITDA）、EPS、BPS
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

def get_eval_data(
        ts_code:str, 
        date:pd.Timestamp=pd.Timestamp(datetime.datetime.today()),
        pro:ts.pro_api=pro
        )->dict:
    start_date=(date-pd.DateOffset(years=1)).strftime("%Y%m%d")
    end_date=date.strftime("%Y%m%d")
    eval_data={}
    # 每日指标中的估值数据
    daily_eval:pd.DataFrame = pro.daily_basic(**{
        "ts_code": ts_code,
        "trade_date": "",
        "start_date": start_date,
        "end_date": end_date,
        "limit": "",
        "offset": ""
    }, fields=[
        "trade_date",
        "pe_ttm",
        "pb",
        "ps_ttm",
        "dv_ttm",
        'total_mv'
    ])
    # 保留 'trade_date' 列，将其余非数值型列转换为 np.nan
    cols_to_process = daily_eval.columns.difference(['trade_date'])
    daily_eval[cols_to_process] = daily_eval[cols_to_process].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    # 计算pe/pb的分位数
    daily_eval['pe_ttm_rank'] = daily_eval['pe_ttm'].rank(pct=True)*100
    daily_eval['pb_rank'] = daily_eval['pb'].rank(pct=True)*100
    # 财务指标中的估值数据
    financial_eval:pd.DataFrame = pro.fina_indicator(**{
        "ts_code": ts_code,
        "ann_date": "",
        "start_date": "",
        "end_date": "",
        "period": "",
        "update_flag": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ebitda",
        "end_date",
        "eps",
        "bps",
        "fcfe_ps"
    ])
    cols_to_process=financial_eval.columns.difference(['end_date'])
    financial_eval[cols_to_process] = financial_eval[cols_to_process].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    # 存储数据
    eval_data['PE(TTM)']=np.round(daily_eval['pe_ttm'].iloc[0], 3)
    eval_data['PE(TTM)分位数']=np.round(daily_eval['pe_ttm_rank'].iloc[0], 3)
    eval_data['PB']=np.round(daily_eval['pb'].iloc[0], 3)
    eval_data['PB分位数']=np.round(daily_eval['pb_rank'].iloc[0], 3)
    eval_data['PS(TTM)']=np.round(daily_eval['ps_ttm'].iloc[0], 3)
    eval_data['股息率']=np.round(daily_eval['dv_ttm'].iloc[0], 3)
    eval_data['EPS']=np.round(financial_eval['eps'].iloc[0], 3)
    eval_data['BPS']=np.round(financial_eval['bps'].iloc[0], 3)
    try:
        eval_data['EV/EBITDA']=np.round(daily_eval['total_mv'].iloc[0]/financial_eval['ebitda'].iloc[0], 3)
    except:
        eval_data['EV/EBITDA']=np.nan
    return eval_data

def eval_analysis(symbol:str)->str:
    ts_code=symbol_to_ts_code(symbol)
    df=get_eval_data(ts_code)
    result=f'股票代码：{symbol}，{get_stock_name(symbol)}的估值指标（PE/PB的分位数为过去一年的分位数）：\n'
    for key, value in df.items():
        result+=f"+ {key}: {value}\n"
    return result

if __name__=="__main__":
    print(eval_analysis('688567'))