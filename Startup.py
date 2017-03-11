from jieba import analyse
from MsgsGenerator import logs
from WordCloudPlot import plot as word_cloud_plot

if __name__ == '__main__':
    tags = []
    analyse.set_stop_words('分词忽略列表.txt')
    with open('全部消息记录.txt') as file:
        for group, friend, msgs in logs(file):
            print('正在解析: %s分组下的%s' % (group, friend))
            for time, who, content in msgs:
                tags.extend(analyse.extract_tags(content, topK=8))
    if len(tags) > 0:
        word_cloud_plot(tags, '词云外观.jpg')
