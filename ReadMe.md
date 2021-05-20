# 使用方法及介绍
1.更改 \splider_multi\splider_multi\spiders\ 下面文件进行爬取文件内容调整
2.更改setting.py 文件进行配置文件更改
3.更改items.py文件进行爬虫输出对象修改
4.更改pipelines.py文件进行爬取数据后续处理
5.运行run.py文件进行爬虫文件执行


原女神网站， 15K id ， 先下载15k原始数据， 并压成少量大文件(h5)
对原图做face++， 保存结果， 并把结果压成少量大文件
当需要256x256数据，对原始h5，和face++结果并行操作，设置过滤条件，获取对齐256数据。也存成少量大文件。
当需要512x512数量，同上。
参考arcface_crawler/face++ filter 封装成脚本，colab并行。