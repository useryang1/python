# -*- coding:utf-8 -*-
import urllib.request
import re
import xlwt#用来创建excel文档并写入数据

#获取原码
def get_content(page):
    #url ='https://search.51job.com/list/080200,000000,0000,00,9,99,Java,2,'+ str(page)+'.html'
    url = 'https://search.51job.com/list/080200,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4,2,' + str(page) + '.html'
    a = urllib.request.urlopen(url)#打开网址
    html = a.read().decode('gbk')#读取源代码并转为unicode
    return html

def get(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)" href="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)" href="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)#匹配换行符
    items = re.findall(reg,html)
    return items
def excel_write(items,index):

#爬取到的内容写入excel表格
    for item in items:#职位信息
        for i in range(0,7):
            #print item[i]
            #if(i==1 or i==3):
             #   ws.write(index, i, "=HYPERLINK("+item[i]+")")  # 行，列，数据
            #else:
                ws.write(index,i,item[i])#行，列，数据
        print(index)
        index+=1

newTable="test.xls"#表格名称
wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
ws = wb.add_sheet('sheet1')#创建表格
headData = ['招聘职位','职位要求（url）','公司名称','公司简介（url）','地址','薪资','日期']#表头部信息
for colnum in range(0, 7):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列

for each in range(1,10):
    index=(each-1)*50+1
    excel_write(get(get_content(each)),index)
wb.save(newTable)