import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import pickle
import os

current_path = os.getcwd()

stock_list=pd.read_csv(os.path.join(os.getcwd(), "stock_list.csv"), dtype={"symbol":str})
stock_list.set_index("symbol", inplace=True)
def get_stock_name(symbol:str)->str:
    return stock_list.loc[symbol, "name"]

# ===========================
# 步骤 A: 初始化与向量库构建 (首次运行或数据更新时执行)
# ===========================
class StockSearchEngine:
    def __init__(self, model_path, data_path, embeddings_cache_path=os.path.join(current_path,'similarity',"stock_embeddings.pkl")):
        self.model = SentenceTransformer(model_path)
        self.df = pd.read_csv(data_path, dtype={'code':str}) # 假设你有 stock_data.csv
        self.embeddings_cache_path = embeddings_cache_path
        self.embeddings = None
        
        # 尝试加载缓存的向量，避免每次启动都重新计算（5000条数据虽然快，但缓存更好）
        if os.path.exists(self.embeddings_cache_path):
            print("加载缓存的向量库...")
            with open(self.embeddings_cache_path, "rb") as f:
                self.embeddings = pickle.load(f)
        else:
            print("首次运行，正在构建向量库（需要几秒钟）...")
            self.update_embeddings()

    def update_embeddings(self):
        """将所有股票文本转化为向量并保存"""
        # 这里的 text_col 是你上一轮构建的组合文本：[行业][性质]...[业务]
        sentences = self.df['text'].tolist() 
        
        # 编码并归一化（归一化后，点积等同于余弦相似度）
        self.embeddings = self.model.encode(sentences, convert_to_tensor=True, normalize_embeddings=True)
        
        # 保存到硬盘
        with open(self.embeddings_cache_path, "wb") as f:
            pickle.dump(self.embeddings, f)
        print("向量库构建完成并已保存。")

    # ===========================
    # 步骤 B: 核心功能 - 查相似股
    # ===========================
    def search_by_code(self, stock_code, top_k=5):
        """输入股票代码，找相似股"""
        # 1. 找到该股票在DataFrame中的索引
        query_row = self.df[self.df['code'] == stock_code]
        if query_row.empty:
            return f"未找到代码 {stock_code}"
        
        idx = query_row.index[0]
        query_embedding = self.embeddings[idx] # 取出该股票的向量

        # 2. 计算与所有其他股票的相似度 (矩阵乘法)
        # cos_scores 形状: [1, 5300]
        cos_scores = torch.mm(query_embedding.unsqueeze(0), self.embeddings.transpose(0, 1))
        
        # 3. 排序取出前 k 个
        scores, indices = torch.topk(cos_scores[0], k=top_k+1) # +1是因为第一名肯定是它自己
        
        results = []
        for score, i in zip(scores, indices):
            if i == idx: continue # 跳过自己
            info = self.df.iloc[i.item()]
            results.append({
                "代码": info['code'],
                "名称": get_stock_name(info['code']),
                "相似度": f"{score:.4f}"
            })
        return results

    def search_by_text(self, query_text, top_k=5):
        """输入任意文本（如：'光刻机制造'），找相关股票"""
        # 1. 将查询文本转化为向量
        query_embedding = self.model.encode(query_text, convert_to_tensor=True, normalize_embeddings=True)
        
        # 2. 计算相似度
        cos_scores = torch.mm(query_embedding.unsqueeze(0), self.embeddings.transpose(0, 1))
        
        # 3. 排序
        scores, indices = torch.topk(cos_scores[0], k=top_k)
        
        results = []
        for score, i in zip(scores, indices):
            info = self.df.iloc[i.item()]
            results.append({
                "代码": info['code'],
                "名称": get_stock_name(info['code']),
                "相似度": f"{score:.4f}"
            })
        return results

# ===========================
# 4. 使用示例
# ===========================
if __name__ == "__main__":
    # 假设你的数据文件叫 stock_data_full.csv，里面必须有一列 'combined_text' 是之前训练时的拼接文本
    # 如果没有，需要先生成这一列
    
    engine = StockSearchEngine(
        model_path=os.path.join(current_path, 'similarity', "stock_similarity_model"), 
        data_path=os.path.join(current_path, 'similarity', "train_sentences.csv")
    )

    print("\n--- 测试1: 根据代码查相似 (例如：贵州茅台 600519) ---")
    # 注意：确保csv里的code是字符串格式，且与输入一致
    similar_stocks = engine.search_by_code("600519") 
    for stock in similar_stocks:
        print(stock)

    '''
    print("\n--- 测试2: 语义搜索 (例如：寻找做锂电池隔膜的公司) ---")
    concept_stocks = engine.search_by_text("锂电池隔膜生产与研发")
    for stock in concept_stocks:
        print(stock)
    '''