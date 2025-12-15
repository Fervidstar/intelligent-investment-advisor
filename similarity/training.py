# 训练相似度模型
# 导入必要的库
import pandas as pd
from sentence_transformers import SentenceTransformer, InputExample, losses, models
from torch.utils.data import DataLoader
import torch

# 选用预训练的中文轻量模型，会自动下载
model_name = 'BAAI/bge-small-zh-v1.5' 
word_embedding_model = models.Transformer(model_name, max_seq_length=256)
pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension())
model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

# 读取训练数据
all_data=pd.read_csv(f'E:/stock_analysis/similarity/train_sentences.csv')
train_sentences=all_data['text'].tolist()
# 准备数据加载器
# SimCSE不需要标签，只需要InputExample包含文本即可
train_examples = [InputExample(texts=[t, t]) for t in train_sentences] # 重复两次是为了配合库的格式，内部Loss会处理
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=32)

# 定义损失函数：MultipleNegativesRankingLoss 在无监督对数据对上表现类似 SimCSE
train_loss = losses.MultipleNegativesRankingLoss(model)

# 开始训练
print("开始训练...")
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=3,               # 训练3轮
    warmup_steps=100,       # 预热步数
    show_progress_bar=True,
    optimizer_params={'lr': 3e-5}
)
# 保存模型
model.save("stock_similarity_model")
print("训练完成！")