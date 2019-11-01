
# 医学文本结构化  - 测试教程
此工具包的结构化分类范围为：孕周、孕次、高危因素、胎位、结果、阿氏评分。

# Text Classification with CNN and RNN

使用卷积神经网络以及循环神经网络进行中文文本分类

CNN做句子分类的论文可以参看: [Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)

还可以去读dennybritz大牛的博客：[Implementing a CNN for Text Classification in TensorFlow](http://www.wildml.com/2015/12/implementing-a-cnn-for-text-classification-in-tensorflow/)

以及字符级CNN的论文：[Character-level Convolutional Networks for Text Classification](https://arxiv.org/abs/1509.01626)

本文是基于TensorFlow在中文数据集上的简化实现，使用了字符级CNN和RNN对中文文本进行分类，达到了较好的效果。

文中所使用的Conv1D与论文中有些不同，详细参考官方文档：[tf.nn.conv1d](https://www.tensorflow.org/api_docs/python/tf/nn/conv1d)


## 环境

- Python 3.6
- TensorFlow 1.14.0
- numpy
- scikit-learn
- scipy

## 运行过程
1，将`预处理`句子放在`data/lianyin.txt`中。  
2，跳转到`run_cnn.py`文件并执行。即`Run run_cnn`   

![images/jiaocheng1.png](images/jiaocheng1.png)

## 最终结果
```python
{'胎位':
 ['剖宫产', 'g/p', '枕左前剖宫产'],
  '孕产次': ['5', '4'],
  '孕周': ['38', '6'],
  '高危因素': ['巨大儿', '疤痕子宫胎膜早破', '高龄初产妇妊娠监督'], 
  '结果': ['足月单活胎'], 
  '阿氏评分': ['1', '10', '5', '9', '10', '8']
}
```

## 文件说明
#### post_process
结构化后处理脚本文件
#### data
存放训练数据的文件夹

---
### 遗留问题（作者）
1，文件的路径  
2，数据分割时，apgar的分割如何兼容
