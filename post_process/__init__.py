import re


# 处理孕周\孕次\apgar的方法
def process_number(sen):
    res = re.findall(r"\d+\.?\d*", sen)
    if len(res) > 3:
        res = res[1::2]
    print(res)
    return res

