import re

# common
# common
# 提取数字信息
def process_number(sen):
    res = re.findall(r"\d+\.?\d*", sen)
    if len(res) > 3:
        res = res[1::2]
    return res


# 提取孕周/孕次信息
def extract_yunzhou_yunci(sen):
    arr = process_number(sen)
    return arr[0], arr[1]


# 提取阿氏评分信息
def extract_alpha(sen):
    """
    :param sen:
    :return: 阿氏评分：1分钟，5分钟，10分钟的值
    """
    arr = process_number(sen)
    # 如果不存在就返回None，如果存在就返回相应的值
    return arr[0] if len(arr) > 0 else None,\
           arr[1] if len(arr) > 1 else None,\
           arr[2] if len(arr) > 2 else None


