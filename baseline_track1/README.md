
## 实验准备
### 模型下载
  本基线采用 **[glm-3-turbo](https://open.bigmodel.cn/dev/api#glm-3-turbo)** 模型，可自行前往官网申请API调用。
### 数据准备
  在 **[智源指数](https://)** 平台上获取数据，放到 [data/CRMUS](data/CRMUS) 文件夹中.

其它具体细节可参考 https://github.com/hiyouga/LLaMA-Factory/blob/main/README_zh.md
### 环境搭建
```bash
pip install zhipuai
```

## 模型训练

本赛道为提示学习赛道，无需训练模型，设计提示学习方式即可，如 **[run.py](run.py)** 中所示：
```
根据故事回答下面的单项选择题，只给出答案即可：
故事：...
问题：...
选项：...
答案：
```

