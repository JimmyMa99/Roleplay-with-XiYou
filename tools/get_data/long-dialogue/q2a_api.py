import argparse
from openai import OpenAI
from tqdm import tqdm

# Define your base prompt as before
base_prompt='你是一个对话整理大师，以下内容为《西游记》节选，请你整理出角色“唐三藏”，“孙悟空”，“猪八戒”，“沙悟净”四人的对话内容，当然，这四人在小说中可能以别的名字出现，如：唐三藏->金蝉子，孙悟空->猴王->行者等人物需要你根据理解自行判别，直接返回对话内容，返回格式为：唐三藏：{对话内容}，孙悟空：{对话内容}，猪八戒：{对话内容}，沙悟净：{对话内容}，某人说：{对话内容}；若内容中无对话，则直接回答“无对话内容”无需提及人物，若对话不完整或者你没法确定对话的人物关系，你可以放弃整理，直接回复“无对话内容”无需提及人物，若出现非四人内任务与四人对话，非四人内的以“某人说”记录，请保持对话的准确性，不要修改和翻译，请不要解释。以下为节选片段：'

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def get_response(prompt):
    client = OpenAI(
        api_key='',
        base_url='',
    )

    messages = [{
        'role': 'system',
        'content': base_prompt,
    }, {
        'role': 'user',
        'content': prompt
    }]

    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.3,
    )
    return completion.choices[0].message.content

def run(file_path):
    prompts = load_txt(file_path).split('\n')

    for prompt in tqdm(prompts):
        response = get_response(prompt)
        with open(f'conversation.txt', 'a', encoding='utf-8') as f:
            f.write(response + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process conversation inputs.')
    parser.add_argument('--file_path', type=str, required=True, help='Path to the input text file')
    args = parser.parse_args()

    run(args.file_path)
