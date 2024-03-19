# CCL24-Eval 儿童故事常识推理与寓意理解评测

&emsp;&emsp;语言模型（LMs）已经在众多自然语言处理任务中取得令人兴奋的进展，达到甚至超越了人类的水平。尽管已经具备了一定的文本理解和推理能力，但模型在涉及超越文本表层含义的深层语义理解及推理任务，如故事寓意理解、常识推理等仍表现不佳。     
&emsp;&emsp;为了提升语言模型的常识推理和深层语义理解能力，我们收集了四百多个经典寓言故事-伊索寓言，构建了儿童故事常识推理与寓意理解数据集（Commonsense Reasoning and Moral Understanding in Children's Stories，CRMUS），考察模型对与故事相关的常识知识理解和推理能力以及捕获故事深层语义和把握故事整体情节的能力。     
&emsp;&emsp;本次评测设置了两个赛道，其中赛道一可以通过设计提示策略的方式使用ChatGPT、GPT-4、文心一言等大模型；赛道二可以通过微调开发集的方式使用ChatGLM、LLaMA等开源大模型，但需注意使用的模型参数量不能超过7B。    

+ 组织者
  + 谭红叶（山西大学）
  + 李&emsp;茹（山西大学）
  + 张&emsp;虎（山西大学）
  + 俞&emsp;奎（合肥工业大学）
+ 联系人
  + 郭亚鑫（山西大学博士生，[202112407002@email.sxu.edu.cn]()）
  + 孙欣伊（山西大学博士生）
  + 强鹏鹏（山西大学博士生）
  + 闫国航（山西大学硕士生）
  + 梁斐豪（山西大学硕士生）
  
&emsp;&emsp;&emsp;评测任务详细内容可查看 **[智源指数评测网站](https://t)**，遇到任何问题请在选手交流QQ群（938913901）或Issues中提问，欢迎大家参与。

## 1.任务简介

&emsp;&emsp;儿童故事常识推理与寓意理解评测旨在从常识推理和寓意理解两个子任务评价语言模型的常识推理和故事理解能力，两个子任务均为中文。  
&emsp;&emsp;常识推理（Commonsense Reasoning）：基于给定的故事和常识问题，选择正确的候选答案。该任务要求模型根据故事涉及到的常识知识（通常是隐含的）进行推理并回答问题。问题形式为单选题，包括问题和四个选项。  
&emsp;&emsp;寓意理解（Moral Understanding）：基于给定的故事，从多个候选答案中选择最恰当的、最符合故事情节的寓意。该任务是包含四个寓意选项的单项选择题。

## 2.评测数据

### 2.1 数据集概况：

&emsp;&emsp;本任务使用的经典寓言故事由人工从网页上收集。  
&emsp;&emsp;常识推理子任务的问题和答案由人工标注，寓意理解子任务采用自动构建和人工标注结合的方式。常识推理任务涉及到的常识类型包含社会常识、生物常识、时间常识、空间常识以及物理常识，对应的题目数量如表所示。（注：部分题目涉及到多种常识类型）

| **常识类型** | **数量** |
|----------|:------:|
| 社会常识     |  1048  |
| 生物常识     |  426   |
| 时间常识     |  308   |
| 空间常识     |  259   |
| 物理常识     |  178   |


&emsp;&emsp;标注数据由json格式给出，具体包含以下四个文件：
```
dev_CRMUS_CR.json    常识推理开发集
test_CRMUS_CR.json   常识推理测试集
dev_CRMUS_MU.json    寓意理解开发集
test_CRMUS_MU.json   寓意理解测试集
```
&emsp;&emsp;数据集规模如表所示。
  
  | 数据集      | **开发集** | **测试集** | **总计** |
  |:--------:|:-------:|:-------:|:------:|
  | 常识推理(CR) |   400   |  1692   |  2092  |
  | 寓意理解(MU) |   252   |  1056   |  1308  |
  
  ### 2.2 数据样例
  
&emsp;&emsp;常识推理子任务的开发集和测试集中的每条数据包含以下内容：编号(id）、标题(title)、故事(story)、问题(question)、选项(options)、答案(answer)、常识类型(type)，其中测试集的 `"answer"` 字段为空字符串。   
&emsp;&emsp;具体数据样例如下所示：
```json
    {
        "id": "12_88",
        "title": "公鸡和宝玉",
        "story": "一只公鸡在田野里为自己和母鸡们寻找食物。他发现了一块宝玉，便对宝玉说：\"若不是我，而是你的主人找到了你，他会非常珍惜地把你捡起来；但我发现了你却毫无用处。我与其得到世界上一切宝玉，倒不如得到一颗麦子好。\"",
        "question": "关于公鸡对宝玉的看法，下列选项描述正确的是？",
        "options": [
            "A．宝玉太硬了，不好吃",
            "B．主人非常喜欢吃宝玉",
            "C．宝玉不是食物，但自己可以拿去卖钱",
            "D．宝玉不是食物，不能吃"
        ],
        "answer": "D",
        "type": "生物常识、物理常识"
    }
```

  &emsp;&emsp;寓意理解子任务的开发集和测试集中的每条数据包含以下内容：编号(id）、标题(title)、故事(story)、问题(question)、选项(options)、答案(answer)，其中测试集的 `"answer"` 字段为空字符串。   
  &emsp;&emsp;具体数据样例如下所示：
```json
    {
        "id": "12_34",
        "title": "寒鸦与鸽子",
        "story": "寒鸦看见一群不愁吃喝的鸽子舒适地住在鸽舍里，便将自己的羽毛全都涂成白色，跑到鸽舍里，与他们一起过活。寒鸦一直不敢出声，鸽子便以为他也是只鸽子，允许他在—起生活，可是，有一次，他不留心，发出了一声叫声，鸽子们立刻辨认出了他的本来面目，将他啄赶出来。寒鸦在鸽子那里再也吃不到食了，只好又回到他的同类那里。然而他的毛色与以前不同了，寒鸦们不认识他，不让他与他们一起生活。这样，这只寒鸦因想贪得两份，最后却一份都没得到。",
        "question": "下列哪个选项最符合故事说明的寓意？",
        "options": [
            "A.人们应该满足于自己所有的东西，贪得无厌，最后会一无所获。",
            "B.不要因为别人的目光而改变自己，真实的自我才是最重要的。",
            "C.寒鸦失去一切归咎于它的贪婪。",
            "D.人们应该勇于展示真实的自我。"
        ],
        "answer": "A"
    }
```
  **注意：测试集输出与验证集格式保持一致**
  
  ### 2.3 基线系统
  
 &emsp;&emsp;赛道一使用的基线模型为智谱AI的大模型 **[GLM-3-Turbo](https://open.bigmodel.cn/dev/api#glm-3-turbo)** ，具体信息可查看 **[baseline_track1/README.md](baseline_track1/README.md)** 。赛道二使用的基线模型为使用中文语料微调的LLaMA-2开源模型 **[chinese-alpaca-2-7b-hf](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2)** ，具体信息可查看 **[baseline_track2/README.md](baseline_track2/README.md)** 。
## 3.评价标准

&emsp;&emsp;各子任务评测指标如下：

| 任务   | **评价指标**        | **解释** |
| ---- |-----------------|--------|
| 常识推理 | Acc<sub>1</sub> | 答案准确率  |
| 寓意匹配 | Acc<sub>2</sub> | 答案准确率  |

&emsp;&emsp;参赛模型的最终评测成绩取上述所有评价指标的加权平均值 **Score=0.4*Acc<sub>1</sub>+0.6*Acc<sub>2</sub>**，其中Acc<sub>1</sub>是常识推理子任务的答案准确率，Acc<sub>2</sub>是寓意理解子任务的答案准确率。

&emsp;&emsp;指标计算脚本eval.py会随数据集一起发布。     
#### 注意：各位选手在参赛的同时也要认真撰写中英文技术报告，它也是评分的重要依据。同时优秀的中英文评测报告将有机会收录到ACL/CCL Anthology！

## 4.测评赛程

### 4.1 报名方式：

&emsp;&emsp;本次评测在**智源指数平台**上进行报名, 届时将会开通相应的报名系统。

&emsp;&emsp;参赛队伍**同时需要向评测组织者发送电子邮件（[202112407002@email.sxu.edu.cn]()）**，邮件标题为：“CCL2024-儿童故事常识推理与寓意理解评测-参赛单位”，例如：“CCL2024-儿童故事常识推理与寓意理解评测-山西大学”，**报名表[在本项目内](儿童故事常识推理与寓意理解评测报名表.docx)**。   

&emsp;&emsp;完成报名后需加入**评测交流QQ群：938913901**。

### 4.2 赛程安排：

-    报名时间：2024年3月1日-4月20日

-    开发集、测试集发布：2024年3月25日
  
  
  
#### 完成报名后，参赛队伍在智源指数平台上获取评测数据。
  
  

-    最终测试文件与模型提交：2024年5月1日

-    参赛队伍成绩及排名公布：2024年5月10日

-    参赛队伍提交技术报告：2024年5月21日

-    中英文技术报告反馈：2024年6月5日

-    获奖名单公布：2024年6月15日

-    评测研讨会：2024年7月25日-7月28日
  
  ### 4.3 结果提交
  
&emsp;&emsp;本次评测结果在**智源指数平台**上进行提交和排名，届时将会开通相应的提交与评测系统，参赛者可以在网站上注册账号并提交相应的测试文件。在参赛期间，严禁参赛团队注册其它账号多次提交。   
&emsp;&emsp;**赛道一参赛者**最终需要提交以下文件：   
&emsp;&emsp;1)输出结果文件：以utf-8为编码格式的json文件，其中的文件格式与**验证集**保持一致，在"answer"项中放入答案即可，结果文件格式不正确不予计算成绩。两个文件命名为：test_CRMUS_CR.json与test_CRMUS_MU.json。   
&emsp;&emsp;2)提示策略说明文档，该文档是docx文件，其中的内容为使用大模型时所构造的提示策略。  
&emsp;&emsp;参赛者提交压缩文件并命名为CRMUS_1.zip，其中包含以下文件：   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;test_CRMUS_CR.json   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;test_CRMUS_MU.json   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_CR_prompt.docx   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_MU_prompt.docx

&emsp;&emsp;**赛道二参赛者**最终需要提交以下文件：   
&emsp;&emsp;1)&emsp;输出结果文件：同赛道一输出结果文件。   
&emsp;&emsp;2)&emsp;模型文件：评测使用的模型。所提交模型必须真实可复现，文件命名为：CRMUS_CR_model.zip与CRMUS_MU_model.zip。   
&emsp;&emsp;3)&emsp;模型说明文档：该文档是docx文件，其中的内容为模型代码运行调试流程，文件命名为： CRMUS_CR.docx与CRMUS_MU.docx。   
&emsp;&emsp;参赛者提交压缩文件并命名为CRMUS_2.zip，其中包含以下文件：   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;test_CRMUS_CR.json   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;test_CRMUS_MU.json   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_CR_model.zip   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_MU_model.zip   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_CR.docx   
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;CRMUS_MU.docx
  
  ## 5.奖项设置
  
   &emsp;&emsp;赛道一和赛道二都将分别评选出如下奖项，由中国中文信息学会计算语言学专委会（CIPS-CL）为获奖队伍提供荣誉证书。

  | 奖项  | 一等奖  | 二等奖  | 三等奖  |
  |:---:|:----:|:----:|:----:|
  | 数量  | 1名   | 1名   | 1名   |
  | 奖励  | 荣誉证书 | 荣誉证书 | 荣誉证书 |
  
  ## 6.注意事项
  
  1)&emsp;由于版权保护问题，CRMUS数据集只免费提供给用户用于非盈利性科学研究使用，参赛人员不得将数据用于任何商业用途。如果用于商业产品，请联系谭红叶老师，邮箱[tanhongye@sxu.edu.cn]()。   
  2)&emsp;每名参赛选手只能参加一支队伍，如果某选手以注册多个账号的方式参加多支队伍，将取消相关队伍的参赛资格。   
  3)&emsp;数据集的具体内容、范围、规模及格式以最终发布的真实数据集为准。针对测试集，不允许参赛人员执行任何人工标注。   
  4)&emsp;参赛队伍可在参赛期间随时上传测试集的预测结果，**智源指数平台每天可提交5次**，系统会实时更新当前最新榜单排名情况，参赛团队应避免注册其它账号多次提交。   
  5)&emsp;允许使用公开的或个人/组织内部的代码、工具、外部数据等，但需要保证参赛结果可以复现。   
  6)&emsp;参赛队伍需协助评测组织者对测试结果进行验证，包含且不限于复现模型结果、提供prompt设计策略等，否则成绩无效。   
  7)&emsp;算法与系统的知识产权归参赛队伍所有。要求最终结果排名前6的队伍提供算法代码与系统报告（包括方法说明、数据处理、参考文献和使用开源工具、外部数据等信息）。提交完毕将采用随机交叉检查的方法对各个队伍提交的模型进行检验，如果在排行榜上的结果无法复现，将取消获奖资格。   
  8)&emsp;参赛团队需保证提交作品的合规性，若出现下列或其他重大违规的情况，将取消参赛团队的参赛资格和成绩，获奖团队名单依次顺延。重大违规情况如下：   
  &emsp;&emsp;a.使用小号、串通、剽窃他人代码等涉嫌违规、作弊行为；   
  &emsp;&emsp;b.团队提交的材料内容不完整，或提交任何虚假信息；   
  &emsp;&emsp;c.参赛团队无法就作品疑议进行足够信服的解释说明。

  ### 算力赞助
北京并行科技股份有限公司将为每个参赛队伍提供一定的算力支持。

  ### 测评单位
  
  山西大学&emsp;&emsp;合肥工业大学
