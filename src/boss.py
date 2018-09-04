# -*- coding:utf-8 -*-
import re
import xlwt#用来创建excel文档并写入数据
import requests
from requests.exceptions import RequestException

#获取原码
def get_content(page):
    #url ='https://search.51job.com/list/080200,000000,0000,00,9,99,Java,2,'+ str(page)+'.html'
    url = 'https://www.zhipin.com/c101210100-p100101/h_101210100/?query=CTO&page=' + str(page)
    #a = urllib.request.urlopen(url)#打开网址
    #html = a.read().decode('gbk')#读取源代码并转为unicode
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    try:
        # 获取网页内容，返回html数据
        response = requests.get(url, headers=headers)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            html_c = response.text
            return response.text
        return None
    except RequestException as e:
        return None

def get(html):
    #reg = re.compile(r'class="job-primary">.*? <a href="(.*?)".*? class="job-title">(.*?)</div>.*? class="red">(.*?)</span>.*?<p>(.*?) <em class="vline"></em>(.*?)<em class="vline"></em>(.*?)</p>.*?<h3 class="name"><a href="(.*?)" .*? target="_blank">(.*?)</a></h3>',re.S)#匹配换行符
    #reg = re.compile(r'class="job-primary">.*? <a href="(.*?)".*? class="job-title">(.*?)</div>',re.S)#匹配换行符
    #reg = re.compile(r'class="job-primary">.*? <a href="(.*?)".*? class="job-title">(.*?)</div>.*? class="red">(.*?)</span>', re.S)  # 匹配换行符
    reg = re.compile(r'class="job-primary">.*? <a href="(.*?)".*? class="job-title">(.*?)</div>.*? class="red">(.*?)</span>.*?<h3 class="name"><a href="(.*?)".*? target="_blank">(.*?)</a></h3>',re.S)  # 匹配换行符
    items = re.findall(reg,html)
    return items

urlhead='https://www.zhipin.com/'
def excel_write(items,index):

#urlhead='https://www.zhipin.com/'
#爬取到的内容写入excel表格
    for item in items:#职位信息
        for i in range(0,5):
            #print item[i]
            if(i==0 or i==3):
               ws.write(index, i, urlhead+item[i]+")")  # 行，列，数据
            else:
                ws.write(index,i,item[i])#行，列，数据
        print(index)
        index+=1

newTable="test.xls"#表格名称
wb = xlwt.Workbook(encoding='utf-8')#创建excel文件，声明编码
ws = wb.add_sheet('sheet1')#创建表格
headData = ['职位要求（url）','招聘职位','薪资','公司简介（url）','公司名称']#表头部信息
for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列

for each in range(1,20):
    index=(each-1)*30+1
    excel_write(get(get_content(each)),index)
wb.save(newTable)