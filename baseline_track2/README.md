
## 实验准备
### 模型下载
  本基线采用 **[chinese-alpaca-2-7b-hf](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)** 模型。

  下载模型文件到 [model](model) 文件夹中，即可通过 `--model_name_or_path ./model/模型名称` 参数指定模型。
### 数据准备
  在 **[智源指数](https://)** 平台上获取数据，放到 [data/CRMUS](data/CRMUS) 文件夹中，并务必在 [data/Cdataset_info.json](data/dataset_info.json) 文件中按照以下格式提供信息：
```
"数据名称": {
    "file_name": "数据路径"
  }
```
例如：  
```  
"dev_CRMUS_CR": {
    "file_name": "./CRMUS/dev_CRMUS_CR.json"
  },
```
添加后可通过指定 `--dataset 数据集名称` 参数使用数据集。
### 软件依赖

| 必需项       | 至少     | 推荐      |
| ------------ | ------- | --------- |
| python       | 3.8     | 3.10      |
| torch        | 1.13.1  | 2.2.0     |
| transformers | 4.37.2  | 4.38.2    |
| datasets     | 2.14.3  | 2.17.1    |
| accelerate   | 0.27.2  | 0.27.2    |
| peft         | 0.9.0   | 0.9.0     |
| trl          | 0.7.11  | 0.7.11    |

| 可选项       | 至少     | 推荐      |
| ------------ | ------- | --------- |
| CUDA         | 11.6    | 12.2      |
| deepspeed    | 0.10.0  | 0.13.1    |
| bitsandbytes | 0.39.0  | 0.41.3    |
| flash-attn   | 2.3.0   | 2.5.5     |

其它具体细节可参考 https://github.com/hiyouga/LLaMA-Factory/blob/main/README_zh.md
### 环境搭建
```bash
# git clone https://github.com/hiyouga/LLaMA-Factory.git
# cd LLaMA-Factory
conda create -n llama_factory python=3.10
conda activate llama_factory
pip install -r requirements.txt
```

## 模型训练

### 指令监督微调
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train \
    --model_name_or_path path_to_llama_model \
    --dataset data_name \
    --template default \
    --finetuning_type lora \
    --lora_target q_proj,v_proj \
    --output_dir path_to_checkpoint \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 3.0 \
    --plot_loss
```

### 模型预测
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_predict \
    --model_name_or_path path_to_llama_model \
    --adapter_name_or_path path_to_checkpoint \
    --dataset data_name \
    --template default \
    --finetuning_type lora \
    --output_dir path_to_predict_result \
    --per_device_eval_batch_size 1 \
    --max_samples 2000 \
    --predict_with_generate
```

### 合并 LoRA 权重并导出模型

```bash
CUDA_VISIBLE_DEVICES=0 python src/export_model.py \
    --model_name_or_path path_to_llama_model \
    --adapter_name_or_path path_to_checkpoint \
    --template default \
    --finetuning_type lora \
    --export_dir path_to_export \
    --export_size 2 \
    --export_legacy_format False
```
## 参考
[1]@Misc{llama-factory,
  title = {LLaMA Factory},
  author = {hiyouga},
  howpublished = {\url{https://github.com/hiyouga/LLaMA-Factory}},
  year = {2023}
}

[2]@article{Chinese-LLaMA-Alpaca,
    title={Efficient and Effective Text Encoding for Chinese LLaMA and Alpaca},
    author={Cui, Yiming and Yang, Ziqing and Yao, Xin},
    journal={arXiv preprint arXiv:2304.08177},
    url={https://arxiv.org/abs/2304.08177},
    year={2023}
}