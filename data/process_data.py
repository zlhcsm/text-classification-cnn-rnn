import time
import re


def process_data():
    txt = load_txt()  # 加载文件
    sen_list = phrasing(txt)  # 分句
    gen_used_input(sen_list)  # 生成json


def load_txt():
    txt = ''
    with open('data/lianyin.txt', 'r', encoding='utf8') as ly:
        txt = ly.read()
    return txt


def phrasing(par):
    sentences = re.split('[；;,，！!.。\s]', par)
    while '' in sentences:
        sentences.remove('')
    print("-------切分好的句子如下：--------")
    for line in sentences:
        print(line)
    return sentences


# 用来生成可用的输入信息
def gen_used_input(sen_list):
    with open('data/cnews/show_data.txt', 'w', encoding='utf8') as file_object:
        for sen in sen_list:
            file_object.write('孕产次')
            file_object.write('\t')
            file_object.write(sen)
            file_object.write('\n')


# print("结束于：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 测试
# process_data()