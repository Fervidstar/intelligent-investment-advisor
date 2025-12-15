---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:5435
- loss:MultipleNegativesRankingLoss
base_model: BAAI/bge-small-zh-v1.5
widget:
- source_sentence: 行业：化学制药，性质：None，规模：大盘股。业务内容：专注于小分子药物研发服务与产业化应用的平台型高新技术企业,主要业务包括小分子药物发现领域的分子砌块和工具化合物的研发,以及小分子药物原料药,中间体的工艺开发和生产技术改进,为全球医药企业和科研机构提供从药物发现到原料药和医药中间体的规模化生产的相关产品和技术服务.
  sentences:
  - 行业：IT设备，性质：民营企业，规模：中盘股。业务内容：卡莱特是一家以视频处理算法为核心,硬件设备为载体,为客户提供视频图像领域综合化解决方案的高科技公司.公司产品主要分为LED显示控制系统,视频处理设备,云联网播放器三大类,可实现视频信号与图像数据的显示控制,编辑处理,传输分析等各类功能.
  - 行业：化学制药，性质：None，规模：大盘股。业务内容：专注于小分子药物研发服务与产业化应用的平台型高新技术企业,主要业务包括小分子药物发现领域的分子砌块和工具化合物的研发,以及小分子药物原料药,中间体的工艺开发和生产技术改进,为全球医药企业和科研机构提供从药物发现到原料药和医药中间体的规模化生产的相关产品和技术服务.
  - 行业：日用化工，性质：地方国企，规模：大盘股。业务内容：主要产品:化妆品,中药饮片,四技.
- source_sentence: 行业：软件服务，性质：中央国企，规模：大盘股。业务内容：计算机软件开发及产品的销售及服务
  sentences:
  - 行业：元器件，性质：民营企业，规模：小盘股。业务内容：产品主要包括半导体显示器件及特种胶粘材料两大系列.主营业务为半导体显示器件及特种胶粘材料的研发,生产和销售.
  - 行业：软件服务，性质：中央国企，规模：大盘股。业务内容：计算机软件开发及产品的销售及服务
  - 行业：电气设备，性质：民营企业，规模：小盘股。业务内容：主营业务:专注于输电线路铁塔的研发,设计,生产和销售.主营产品为输电线路铁塔.
- source_sentence: 行业：出版业，性质：地方国企，规模：大盘股。业务内容：主营业务:图书,报纸,期刊,电子出版物总发行,安徽省内中小学教科书发行及音像制品批发零售等.
  sentences:
  - 行业：化工原料，性质：地方国企，规模：小盘股。业务内容：主要产品:改性铵油炸药,膨化硝铵炸药,乳化炸药,震源药柱和硝酸铵;主营业务:工业炸药及相关产品的生产,销售,民爆产品的生产与销售,工程爆破服务,硝酸铵及其制品的生产与销售.
  - 行业：环境保护，性质：中央国企，规模：中盘股。业务内容：公司主要业务为生活类垃圾处理业务.
  - 行业：出版业，性质：地方国企，规模：大盘股。业务内容：主营业务:图书,报纸,期刊,电子出版物总发行,安徽省内中小学教科书发行及音像制品批发零售等.
- source_sentence: 行业：专用机械，性质：民营企业，规模：微盘股。业务内容：墓地销售代理,殡葬服务
  sentences:
  - 行业：塑料，性质：民营企业，规模：微盘股。业务内容：公司是热塑性高分子粘接材料及其应用制品的专业供应商,专注于各类热塑性环保粘接材料的研发,生产及销售.公司主要产品包括各类热熔胶胶粉及胶粒,热熔胶网膜,太阳能电池封装用EVA胶膜和热熔胶胶膜.
  - 行业：乳制品，性质：民营企业，规模：小盘股。业务内容：公司专注于乳制品及乳饮料的研发,生产和销售,并以低温乳制品,低温乳饮料为主打产品.
  - 行业：专用机械，性质：民营企业，规模：微盘股。业务内容：墓地销售代理,殡葬服务
- source_sentence: 行业：小金属，性质：民营企业，规模：巨盘股。业务内容：主要产品:高性能合金材料,环保合金材料,节能合金材料和替代合金材料;多晶硅,单晶硅电池及组件.主营业务:高性能,高精度有色合金材料的研发,生产和销售;太阳能电池,组件的研发,生产和销售及光伏电站的建设运营.
  sentences:
  - 行业：出版业，性质：地方国企，规模：大盘股。业务内容：主营业务:广告代理和制作,印刷,书报刊零售等.
  - 行业：电气设备，性质：民营企业，规模：巨盘股。业务内容：公司系国内知名的智能家电电控产品,工业定制电源和工业自动化产品供应商,研制的产品广泛应用于智能家电,消费电子,医疗,通信,大功率LED显示及照明,工业自动化,电力,交通,节能环保及装备制造等众多行业,并不断在新领域渗透和拓展.
  - 行业：小金属，性质：民营企业，规模：巨盘股。业务内容：主要产品:高性能合金材料,环保合金材料,节能合金材料和替代合金材料;多晶硅,单晶硅电池及组件.主营业务:高性能,高精度有色合金材料的研发,生产和销售;太阳能电池,组件的研发,生产和销售及光伏电站的建设运营.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on BAAI/bge-small-zh-v1.5

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-small-zh-v1.5](https://huggingface.co/BAAI/bge-small-zh-v1.5). It maps sentences & paragraphs to a 512-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-small-zh-v1.5](https://huggingface.co/BAAI/bge-small-zh-v1.5) <!-- at revision 7999e1d3359715c523056ef9478215996d62a620 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 512 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 512, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    '行业：小金属，性质：民营企业，规模：巨盘股。业务内容：主要产品:高性能合金材料,环保合金材料,节能合金材料和替代合金材料;多晶硅,单晶硅电池及组件.主营业务:高性能,高精度有色合金材料的研发,生产和销售;太阳能电池,组件的研发,生产和销售及光伏电站的建设运营.',
    '行业：小金属，性质：民营企业，规模：巨盘股。业务内容：主要产品:高性能合金材料,环保合金材料,节能合金材料和替代合金材料;多晶硅,单晶硅电池及组件.主营业务:高性能,高精度有色合金材料的研发,生产和销售;太阳能电池,组件的研发,生产和销售及光伏电站的建设运营.',
    '行业：出版业，性质：地方国企，规模：大盘股。业务内容：主营业务:广告代理和制作,印刷,书报刊零售等.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 512]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  1.0000, -0.0442],
#         [ 1.0000,  1.0000, -0.0442],
#         [-0.0442, -0.0442,  1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 5,435 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              |
  | details | <ul><li>min: 34 tokens</li><li>mean: 92.38 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 34 tokens</li><li>mean: 92.38 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                    | sentence_1                                                                                                                                    |
  |:----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>行业：汽车配件，性质：None，规模：小盘股。业务内容：从事电驱动系统的研发,生产,销售及服务,已对驱动电机,控制器,传动三大总成自主掌握核心技术和实现完整布局.</code>                                                | <code>行业：汽车配件，性质：None，规模：小盘股。业务内容：从事电驱动系统的研发,生产,销售及服务,已对驱动电机,控制器,传动三大总成自主掌握核心技术和实现完整布局.</code>                                                |
  | <code>行业：元器件，性质：民营企业，规模：中盘股。业务内容：主营业务为新型电子元器件(高密度印刷线路板等)的研发,生产和销售,产品主要应用于消费电子,网络通讯,电脑周边,汽车电子和工业控制等领域.主要产品以连接器,电容屏,按键,像机与LCD模组用FPCB等为主.</code> | <code>行业：元器件，性质：民营企业，规模：中盘股。业务内容：主营业务为新型电子元器件(高密度印刷线路板等)的研发,生产和销售,产品主要应用于消费电子,网络通讯,电脑周边,汽车电子和工业控制等领域.主要产品以连接器,电容屏,按键,像机与LCD模组用FPCB等为主.</code> |
  | <code>行业：半导体，性质：None，规模：大盘股。业务内容：主要向客户提供FPGA产品,包括FPGA芯片和专用EDA软件两部分.主营业务为FPGA芯片和专用EDA软件的研发,设计和销售.</code>                                       | <code>行业：半导体，性质：None，规模：大盘股。业务内容：主要向客户提供FPGA产品,包括FPGA芯片和专用EDA软件两部分.主营业务为FPGA芯片和专用EDA软件的研发,设计和销售.</code>                                       |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 2.9412 | 500  | 0.0052        |


### Framework Versions
- Python: 3.12.9
- Sentence Transformers: 5.1.2
- Transformers: 4.57.3
- PyTorch: 2.9.1+cpu
- Accelerate: 1.12.0
- Datasets: 4.4.1
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply},
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->