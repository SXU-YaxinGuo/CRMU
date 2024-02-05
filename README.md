# CCL24-Eval 儿童故事常识推理与寓意理解评测
Commonsense Reasoning and Moral Understanding Evaluation in Children's Stories，CRMU
## 1.任务简介
&emsp;&emsp;儿童故事常识推理与寓意理解评测（Evaluation on Commonsense Reasoning and Moral Understanding in Children's Stories，CRMU）任务旨在从常识推理（Commonsense Reasoning）和寓意理解（Moral Understanding）两个任务多角度评价中文预训练语言模型和大型语言模型的常识推理和故事理解能力。本评测包含以下2个子任务：
- 常识推理（Commonsense Reasoning）：基于给定的故事和常识问题，选择正确的候选答案。
-	寓意匹配（Moral Matching）：基于给定的故事，从多个候选答案中选择最符合故事的寓意。
+ 组织者
  + 谭红叶（山西大学）
  + 李  茹（山西大学）
  + 张  虎（山西大学）
  + 俞  奎（合肥工业大学）
+ 负责人
  + 郭亚鑫（山西大学博士生，202112407002@email.sxu.edu.cn）
+ 联系人
  + 闫国航（山西大学硕士生，yanguohang@qq.com）
## 2.评测数据
### 数据集规模
&emsp;&emsp;本评测使用的数据来源于网页收集的经典寓言故事。常识推理任务的问题和选项由人工标注，涉及到的常识类型包含时间常识、空间常识、生物常识、物理常识以及社会常识。寓意理解任务包问题和选项采用人工标注和自动生成结合的方式。所有任务均为中文，各子任务数据量统计如下：
|数据集划分|验证集|测试集|
| :-----:|:-----:|:-----: |
| 数据集划分  |开发集  |测试集 |
| 常识推理 | 872 |  872  |
| 寓意匹配|  654  |  654  |
##### 标注数据由json格式给出，包含以下内容：
+ dev_
+ test_
### 数据样例
&emsp;&emsp;各任务数据样例如下：
