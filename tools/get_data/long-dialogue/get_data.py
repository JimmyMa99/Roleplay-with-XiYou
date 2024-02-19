from tqdm import tqdm
import json
import copy
import argparse
import os

single_conversation_={
            "system": "",
            "input": "",
            "output": ""
        }
template_={
    "conversation":[

    ]
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default='data/西游记.txt', help='input file')
    parser.add_argument('--save_path', type=str, default='output/', help='output file')
    return parser.parse_args()

def load_txt(path):
    with open (path, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def conversation_tolist(conversation):
    if '\n\n' in conversation:
        conversation=conversation.replace('\n\n','\n')
    if '\\n\\n' in conversation:
        conversation=conversation.replace('\\n\\n','\n')
    if '\\n' in conversation:
        conversation=conversation.replace('\\n','\n')
    if '\n' in conversation:
        conversation_list=conversation.split('\n')
        return conversation_list
    elif conversation == '"无对话内容"':
        return []
    else:
        return []

def build_single_conversation(conversation_list,taglist):
    #进来的是一段的对话
    #count the number of tag in the conversation
    long_conver=len(conversation_list)
    counter_taglist=[]
    long_conversationlist=[]
    summary_list=[]
    for tag in taglist:
        counter_tag=0
        for sentence in conversation_list:
            if (tag+'：') in sentence:
                counter_tag+=1
        counter_taglist.append(counter_tag)
    for i,tag in zip(counter_taglist,taglist):
        long_conversationlist=[]
        if i!=0:
            for sentence in conversation_list:
                
                if (tag+'：') not in sentence:
                    single_conversation=copy.deepcopy(single_conversation_)
                    single_conversation['system']=tag
                    if '无对话内容' in sentence: sentence=''
                    colon_index = sentence.find("：")
                    single_conversation['input']=sentence[colon_index+1:]
                    single_conversation['output']=''
                    long_conversationlist.append(single_conversation)
                else:
                    colon_index = sentence.find("：")
                    if len(long_conversationlist)!=0:
                        long_conversationlist[-1]['output']=sentence[colon_index+1:]
                    else:
                        single_conversation=copy.deepcopy(single_conversation_)
                        single_conversation['system']=tag
                        single_conversation['input']=''
                        single_conversation['output']=sentence[colon_index+1:]
                        long_conversationlist.append(single_conversation)
            
        else:
            long_conversationlist.append([])
        summary_list.append(long_conversationlist)
    return summary_list
    
def build_long_conversation(convermember,summary_list):
    assert len(convermember)==len(summary_list)
    all_conversation=[]
    for summary in summary_list:
        if len(summary)!=0:
            template=copy.deepcopy(template_)
            for item in summary:
                template['conversation'].append(item)
            # template['conversation'].append(summary.items())
            all_conversation.append(template)
        else:
            all_conversation.append([])
    return all_conversation

def save_json(args,data,tag):
    with open((args.save_path+tag+'.jsonl'), 'a', encoding='utf-8') as f:
        # for item in data:
        #     if item == []:
        #         continue
        if data == {"conversation": [[]]}:
            return
        json_item = json.dumps(data, ensure_ascii=False)  # 同上
        f.write(json_item + "\n")
            
def run(args):
    conversation=load_txt(args.data_path)
    conversationlist=conversation.split('\n')
    answers=[]
    tag_list=['唐三藏','孙悟空','猪八戒','沙悟净']
    # bar=tqdm(total=len(promptlist))
    for prompt_item in tqdm(conversationlist):
        answer=conversation_tolist(prompt_item)
        if len(answer)!=0:answers.append(answer)
        single_conversationlist=build_single_conversation(answer,tag_list)
        savelist=build_long_conversation(tag_list,single_conversationlist)
        for i in range(len(tag_list)):
            save_json(args,savelist[i],tag_list[i])

if __name__ == '__main__':
    args=get_args()
    os.makedirs(args.save_path,exist_ok=True)
    run(args)
