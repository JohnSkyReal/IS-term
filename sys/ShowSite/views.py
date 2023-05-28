from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# import os
import time
# from collections import Counter
import json
import openai

openai.api_key = r'please request from author'


def home(request):
    return render(request, 'home.html')


def train(request):
    global flag
    flag = 0
    return render(request, 'train.html')


def application(request):
    return render(request, 'application.html')


def about_us(request):
    return render(request, 'about_us.html')


# 读取训练日志
with open(r'train.log', 'r', encoding='utf-8')as f:
    lines = f.readlines()
log_len = len(lines)
# 用于计算输出log的行数
flag = 0


# 动态加载训练log内容（使用POST需加入@csrf_exempt）
def add_ajax(request):
    global lines
    global flag
    global log_len
    if request.is_ajax():
        ajax_string = lines[flag]
        flag += 1
        if flag == log_len - 1:
            flag = 0
        return HttpResponse(ajax_string)


def application_post(request):
    eva_result, time_spent = 'Null', 'Null'
    if request.POST:
        # 获取用户输入文本
        input_data = str(request.POST["input_data"]).strip()
        if input_data:
            eva_result, time_spent = gpt3(input_data)
        else:
            input_data = "First of all, the use of these classes as a reference distribution being expected for a research group with a medium performance allows the evaluation of each research group's citation impact in 【#tbl0005】 for its own."
            eva_result, time_spent = 'Information Science terms:\nperformance\nimpact', 'Time cost: %.5f sec.' % 0

        model_type = 'Model used: GPT-3'
        return render(request, 'application.html', {'use_model': model_type, 'input_data': input_data, 'textarea_tag': '<textarea class=\"right_textarea\">', 'textarea_tag_end':'</textarea>', 'split_tag': '<hr/>', 'result': eva_result, 'total_time': time_spent})


def auto_completion(prompt):
    response = openai.Completion.create(
        model="curie:ft-personal:curieepoch4-2023-05-20-09-17-35",
        prompt=prompt,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["END"]
    )
    print(response["choices"][0]["text"])
    print('-'*20)
    return response


def gpt3(prompt):
    prompt = prompt + '\n\n###\n\n'
    start = time.clock()
    response = auto_completion(prompt)
    # response = {"id": "cmpl-7ID3AnrfWI9WWIJx7cpn1yRwA19nV", "object": "text_completion", "created": 1684574424, "model": "curie:ft-personal:curieepoch4-2023-05-20-09-17-35", "choices": [{"text": " performance\nimpact ", "index": 0, "logprobs": 'null', "finish_reason": "stop"}], "usage": {"prompt_tokens": 50, "completion_tokens": 4, "total_tokens": 54}}
    end = time.clock()
    terms = [each.strip() for each in response["choices"][0]["text"].replace('END', '').split('\n') if each.strip()]
    if terms:
        eva_result = 'Information Science terms:\n' + '\n'.join(terms)
    else:
        eva_result = 'No Information Science terms detected!'
    time_spent = 'Time cost: %.5f sec.' % (end - start)
    return eva_result, time_spent


def test(request):
    result = ['what', 'the', 'hell', 'are', 'you', '!']
    return HttpResponse(json.dumps(result), content_type="application/json")
