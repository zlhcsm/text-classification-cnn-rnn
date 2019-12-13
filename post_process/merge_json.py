import json
import sys
from collections import defaultdict
from post_process import process_classify as pc
from data.cnews_loader import open_file, id_to_category


def extra_result_file(test_dir, y):
    """
    用来整合结果数据，组合最后生成的json格式
    :param test_dir:
    :param y:
    :return:
    """
    get_data = []
    with open_file(test_dir) as f:
        for line in f:
            label, content = line.strip().split('\t')
            get_data.append(content)
    id_to_cate = id_to_category()
    cate_list = []
    for index in y:
        cate_list.append(id_to_cate[str(index)])

    # defaultdict类的初始化函数接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值
    zipped = defaultdict(list)
    for (key, value) in zip(cate_list, get_data):
        # 处理孕产次
        if(key == "孕产次"):
            nums = pc.extract_yunzhou_yunci(value)
            tags = ("孕次", "产次")
            dictionary = dict(zip(tags, nums))
            zipped[key].append(dictionary)

        # 处理孕周
        elif (key == "孕周"):
            nums = pc.extract_yunzhou_yunci(value)
            tags = ("周数", "天数")
            dictionary = dict(zip(tags, nums))
            zipped[key].append(dictionary)

        # 处理阿氏评分
        elif(key == "阿氏评分"):
            nums = pc.extract_alpha(value)
            tags = ("1分钟", "5分钟", "10分钟")
            dictionary = dict(zip(tags, nums))
            zipped[key].append(dictionary)

        # 如果是其他情况，则直接加入dict即可
        else:
            zipped[key].append(value)

    with open('write.json', 'w', encoding="utf-8") as f:
        json.dump(zipped, f, ensure_ascii=False)
