from zhipuai import ZhipuAI
import json
client = ZhipuAI(api_key="*************************")  # 填写您自己的APIKey

input_json_file = './CRMUS/filename'
with open(input_json_file, 'r', encoding='utf-8') as f:
    data_test = json.load(f)
with open("output.txt", 'w') as f_o:
    for item in data_test:
        data = str("根据故事回答下面的单项选择题，只给出答案即可：" + "\n故事:" + item['story'] + "\n问题:" + item[
            'question'] + "\n选项:\n" + '\n'.join(item['options']) + "\n答案:")
        response = client.chat.completions.create(
            model="GLM-3-Turbo",  # 填写需要调用的模型名称
            messages=[
                {"role": "user", "content": data}
            ],
        )
        answer = response.choices[0].message.content
        # print("zhipuAI:", answer)
        f_o.write("zhipuAI:" + answer)


