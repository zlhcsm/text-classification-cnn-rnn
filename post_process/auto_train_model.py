from threading import Timer
import datetime


# 往训练文件中添加纠正数据
# 文件不能一次读多次写
def modify_data(tag, sen):
    train_data_path = '../test.txt'
    with open(train_data_path, encoding="utf-8", mode="a") as file:
        file.write(tag + "\t")
        file.write(sen + '\n')


# 定时任务
def auto_system():
    # 获取时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    # 格式化
    line = f'{ts}'
    # 模拟写入数据
    modify_data('tag', line)
    print(line)
    # 启动定时器任务，每三秒执行一次
    Timer(3, auto_system).start()


auto_system()
