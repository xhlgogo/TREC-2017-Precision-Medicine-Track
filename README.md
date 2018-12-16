# TREC-2017-Precision-Medicine-Track
## 一、实验描述
### 3人小组，使用一个信息检索系统，Galago或Elastic Search或Terrier，完成TREC 2017 Precision Medicine Track的检索任务。
### 1.检索任务：
#### TREC 2017 Precision Medicine Track：http://www.trec-cds.org/2017.html
#### 从该检索评测任务网站上自行下载数据集和查询集。
### 2.相关文档集：
#### 相关的生物医学论文：http://www.trec-cds.org/qrels-treceval-abstracts.2017.txt
#### 相关的临床试验：http://www.trec-cds.org/qrels-treceval-clinical_trials.2017.txt
### 3.信息检索工具集：
#### Terrier：http://terrier.org/

## 二、作业提交
### 1.报告文件《信息检索大作业：精准医疗检索.pdf》
### 2.附件：
#### 1）数据源处理代码_extract.py
#### 2）处理后的查询集_topic.xml
#### 3）查询结果_res.zip
#### 4）评价指标_eval.zip
#### 5）相关文档集_eval.txt
### 3.实验环境
#### 1）服务器参数：8 核 32G 内存 Ubuntu16.04
#### 2）软件版本：Terrier5.0， JRE1.8
### 4.实验过程
#### 1）提取数据
#### 2）创建索引
#### 3）检索
#### 4）结果评估
### 5.实验结果
![实验结果.png](https://github.com/xhlgogo/TREC-2017-Precision-Medicine-Track/blob/master/addtion/%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C.PNG)
### 6.讨论与展望
#### 1）实验心得
##### 本小组查询性能达到预期，利用了服务器平台处理数据源、创建索引和查询，实验过程并不一帆风顺。
##### 在开始的时候，我们选取 Galago 作为检索工具，编写了 python 程序对数据源 xml 文档进行了单文件测试，在成功后对所有文档解压并准备检索，但全部解压为 xml 和 txt 文档，过程漫长且占储存空间太大，在此过程中我们找到了可以使用 python 的 lib 库 gzip 打开gz 文件免去解压过程，并获得了实验室服务器的使用权限，于是我们将数据源上传至服务器，采用多线程对数据源压缩文件处理，处理用时大约 2 小时。
##### 之后，我们对比了三种检索工具，从使用便捷性、文档齐全性和创新性三个方面综合考虑，最终选择了 Terrier 作为本小组的检索工具。
##### 确认了检索工具之后我们开始创建索引，利用官网文件，选择了单通道创建，用时约50 分钟。在选择检索模型的过程中，我们比较了官网给出的各种加权模型，依据实验要求选择了十个相对不同的加权检索模型进行实验的检索评估，得到的检索结果较好。
#### 2）实验展望
##### 实验的不足之处主要在与没有很好的理解官网的检索模型，由检索工具 Terrier 没有得到 MRR 和 NDCG 两个评价指标；实验的完善之处在于建立了完整的数据源索引模型，使用了十种不同的加权检索模型进行检索，正确使用官网给出的命令参数，得到的检索评价指标较好。
