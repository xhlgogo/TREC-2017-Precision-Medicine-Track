# -*- coding: utf-8 -*-
import re
import gzip
import os

from multiprocessing import Pool
regxArr = ["<PMID Version="1">", "</PMID>", "<PMID Version="1">", "<ArticleTitle>", "</ArticleTitle>", "<ArticleTitle>",
    "<AbstractText>", "</AbstractText>", "<AbstractText>"]

def handleSingleFile(input_path, output_path):
    # file_open = open(input_path)
    file_save = open(output_path, "w")

    f=gzip.open(input_path, mode="rt")
    input_lines = [i.strip() for i in f.readlines()]
    #output_lines = []
    isInsertText = False
    isInsertDOCNO = False
    for i in input_lines:
        if i == "<PubmedArticle>":
            file_save.write("<DOC>\n")
            isInsertText = False
            isInsertDOCNO = False
            isDouble = True
        elif i == "</PubmedArticle>" and isDouble == True:
            '''
            if not isInsertText :
                file_save.write("<DOCNO> </DOCNO>\n")
            '''
            file_save.write("\n</DOC>\n")


        elif isInsertDOCNO == False and re.match(regxArr[2], i):

            number = i.replace(regxArr[0], "").replace(regxArr[1], "")
            file_save.write('<DOCNO>' + number + '</DOCNO>\n')
            isInsertDOCNO = True

        elif re.match(regxArr[5], i):
            title = i.replace(regxArr[3], "").replace(regxArr[4], "")
            file_save.write(title + " ")
        elif re.match(regxArr[8], i):
            text = i.replace(regxArr[7], "")
            fromIndex = i.find(">")
            text = text[fromIndex+1:-1]
            file_save.write(text + "\n</DOC>\n")
            isDouble = False

    #file_open.close()
    file_save.close()

def task_part1():
    for i in range(1, 301):
        input_path = "./part1/medline17n%04d.xml.gz" % i
        save_path = "./res/part1/medline17n%04d" % i
        handleSingleFile(input_path, save_path)

def task_part2():
    for i in range(301, 547):
        input_path = "./part2/medline17n%04d.xml.gz" % i
        save_path = "./res/part2/medline17n%04d" % i
        handleSingleFile(input_path, save_path)
def task_part3():
    for i in range(547, 718):
        input_path = "./part3/medline17n%04d.xml.gz" % i
        save_path = "./res/part3/medline17n%04d" % i
        handleSingleFile(input_path, save_path)
def task_part4():
    for i in range(718, 851):
        input_path = "./part4/medline17n%04d.xml.gz" % i
        save_path = "./res/part4/medline17n%04d" % i
        handleSingleFile(input_path, save_path)
def task_part5():
    for i in range(851, 890):
        input_path = "./part5/medline17n%04d.xml.gz" % i
        save_path = "./res/part5/medline17n%04d" % i
        handleSingleFile(input_path, save_path)

def read_meeting(path):
    for i in os.listdir(path):
        with open(os.path.join(path, i),'r') as fs, open(os.path.join('/Users/zyj/Desktop/res', i), 'w') as fw:
            start = 0;
            fw.write('<DOC>\n<DOCNO>'+i.split('.')[0]+'</DOCNO>\n')
            lines = fs.readlines()
            for line in lines:
                if start == 0 and re.match('Title', line):
                    start = 1;
                if start:
                    fw.write(line.strip() + ' ')
            fw.write('\n</DOC>\n')



if __name__ == "__main__":
    '''
    p1 = Process(target=task_part1)
    p2 = Process(target=task_part2)
    p3 = Process(target=task_part3)
    p4 = Process(target=task_part4)
    p5 = Process(target=task_part5)
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    '''
    read_meeting('./extra_abstracts')
    # file_path =""
    # file_path = "/Users/zcy/Desktop/information/medline17n0001.xml"
    # if not os.path.exists(file_path):
    #     print ("Not Exist "+file_path)
    # save_path ="/Users/zcy/Desktop/information/document/medline17n%03d" % i
    # print ("handle:"+save_path)
    # handleSingleFile(file_path,save_path)
