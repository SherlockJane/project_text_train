# coding:utf-8
import jieba
import sys
import time

sys.path.append("../../")
import codecs
import os
import re


# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

def LoadStopWordList(filepath):
    """
    创建停用词list
    """
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def FenCi(readfile, outfile, stopwords):
    # r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+0123456789'
    for line in readfile.readlines():
        # 更高效的字符串替换
        # line = re.sub(r, ' ', line)
        newline = jieba.cut(line, cut_all=False)
        outstr_list = list()
        for word in newline:
            if word not in stopwords:
                outstr_list.append(word)
        str_out = ' '.join(outstr_list)
        # str_out.encode('utf-8')\
        print(str_out)
        print(str_out, file=outfile, end=' ')

def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        content = file.read()
        file.close()
        return content


def saveFile(path, result):
    with open(path, 'w', errors='ignore') as file:
        file.write(result)
        file.close()

if __name__ == '__main__':
    fromdir = "./data/"
    todir = "./fenci/"
    stopWordFile = "stopword.txt"
    # 一次只能对一个文档进行分词
    file = "train_positive.txt"
    # file = "train_negative.txt"
    infile = open(os.path.join(fromdir, file), 'r', encoding='UTF-8')
    outfile = open(os.path.join(todir, file), 'w+', encoding='UTF-8')
    # 这里加载停用词
    stopwords = [line.strip() for line in open(os.path.join(todir, stopWordFile), 'r', encoding='UTF-8').readlines()]
    FenCi(infile, outfile, stopwords)
    infile.close()
    outfile.close()
