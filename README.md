# Roleplay-with-XiYou

# 简介

基于《西游记》原文、白话文、ChatGPT生成数据制作的角色扮演多LLM聊天室。

包括模型：[三藏-Chat](https://github.com/JimmyMa99/SanZang-Chat)，[悟空-Chat](https://github.com/JimmyMa99/WuKong-Chat)，[八戒-Chat](https://github.com/JimmyMa99/BaJie-Chat)，[悟净-Chat](https://github.com/JimmyMa99/WuJing-Chat)

> 改编不是乱编，戏说不是胡说。——六小龄童（六老师）
> 

# 快速开始

<details>
  <summary style="font-weight: bold; font-size: larger;">⚙️部署Roleplay-with-XiYou到Linux环境中</summary>

## 环境配置

新建环境-安装lmdeploy

使用 pip ( python 3.8+) 安装 LMDeploy，或者[源码安装](https://github.com/InternLM/lmdeploy/blob/main/docs/zh_cn/build.md)

```jsx
conda create -n chatXY python=3.10 -y
pip install lmdeploy
```

LMDeploy的预编译包默认是基于 CUDA 11.8 编译的。如果需要在 CUDA 12+ 下安装 LMDeploy，请执行以下命令：

```jsx
export LMDEPLOY_VERSION=0.2.0
export PYTHON_VERSION=38
pip install https://github.com/InternLM/lmdeploy/releases/download/v${LMDEPLOY_VERSION}/lmdeploy-${LMDEPLOY_VERSION}-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux2014_x86_64.whl
#比如pip install https://github.com/InternLM/lmdeploy/releases/download/v0.2.3/lmdeploy-0.2.3-cp310-cp310-manylinux2014_x86_64.whl
```

## 下载权重

从modelscope下载权重（可以先尝试两个）

```jsx
apt install git git-lfs -y
git lfs install
cd **Roleplay-with-XiYou**
#三藏-Chat
git clone https://www.modelscope.cn/JimmyMa99/SanZang-Chat.git
#悟空-Chat
git clone https://www.modelscope.cn/JimmyMa99/WuKong-Chat.git
#八戒-Chat
git clone https://www.modelscope.cn/JimmyMa99/BaJie-Chat.git
#悟净-Chat
git clone https://www.modelscope.cn/JimmyMa99/WuJing-Chat.git
```

## lmdeploy api

使用lmdeploy开启服务，以开启悟空-Chat 和 八戒-Chat 为例：

```jsx
#悟空-Chat 启动
lmdeploy serve api_server ./WuKong-Chat --server-name ${gradio_ui_ip} --server-port ${gradio_ui_port}
```

新建一个终端，开启八戒-Chat

```jsx
#八戒-Chat 启动
lmdeploy serve api_server ./WuKong-Chat --server-name ${gradio_ui_ip} --server-port ${gradio_ui_port}
```

## 聊天室开启

- 下载简易聊天室，启动服务端

```jsx
git clone https://github.com/JimmyMa99/Easy-Chatroom.git
cd Easy-Chatroom
python server_start.py
```

- 启动客户端

```jsx
cd Easy-Chatroom
#第一个bot
python bot_start.py
#第二个bot
python bot_start.py
#开启观察客户端（人提问）
python client_start.py
```

## 效果一览

![Untitled](figure/展示图.png)

</details>

# 数据获取

待更新

# 模型微调

待更新

# 相关链接

待更新