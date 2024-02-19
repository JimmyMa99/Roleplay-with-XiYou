from openai import OpenAI
from tqdm import tqdm
import json
import copy
import argparse
import os
import time

api_key = ''
api_base_url = ''

base_prompt = ''
template = {
    "conversation": [
        {
            "system": "user",
            "input": "xxx",
            "output": "xxx"
        }
    ]
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--questions_path', type=str, default='data/questions.txt', help='input file')
    parser.add_argument('--save_path', type=str, default='output/swj.jsonl', help='output file')
    parser.add_argument('--repeat', type=int, default=1, help='repeat times for each question')
    return parser.parse_args()

def load_txt(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().splitlines()
    return data

def save_answer(answer, save_path):
    with open(save_path, 'a', encoding='utf-8') as f:  # Change to 'a' mode for appending
        json_item = json.dumps(answer, ensure_ascii=False)
        f.write(json_item + "\n")

def get_response(prompt, max_retries=5):
    client = OpenAI(api_key=api_key, base_url=api_base_url)
    messages = [{'role': 'system', 'content': base_prompt}, {'role': 'user', 'content': prompt}]
    for attempt in range(max_retries):
        try:
            completion = client.chat.completions.create(model='gpt-3.5-turbo', messages=messages, temperature=0.3)
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait a bit before retrying
            else:
                print("Max retries reached, skipping...")
                return None

def run(args):
    dir_path = os.path.dirname(args.save_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    questions = load_txt(args.questions_path)
    for _ in range(args.repeat):
        for question in tqdm(questions):
            response = get_response(question)
            if response:
                answer = copy.deepcopy(template)
                answer['conversation'][0]['input'] = question
                answer['conversation'][0]['output'] = response
                save_answer(answer, args.save_path)

if __name__ == '__main__':
    args = get_args()
    run(args)
