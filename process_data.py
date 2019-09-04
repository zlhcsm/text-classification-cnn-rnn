import time
import re

paragraph = "剖宫产；g/p 5/2 孕38+6 枕左前剖宫产；巨大儿；疤痕子宫胎膜早破；\
高龄初产妇妊娠监督；足月单活胎；"


def phrasing(par):
    sentences = re.split('[；;,\s]', par)
    while '' in sentences:
        sentences.remove('')
    return sentences


sen_list = phrasing(paragraph)
with open('data/cnews/show_data.txt', 'w', encoding='utf8') as file_object:
    for sen in sen_list:
        file_object.write('孕产次')
        file_object.write('\t')
        file_object.write(sen)
        file_object.write('\n')

print("结束于：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
