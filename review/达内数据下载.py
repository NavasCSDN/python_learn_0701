##问题：1. /a/text()无法匹配中文
##问题: 2. urlencode()后没有urldecode方法
##问题； 3. 文档是否已下载，都载入了，浪费时间，
import requests
import os
from lxml import etree

class GetNoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.auth = ('tarenacode', 'code_2014')
        self.headers = {'User-Agent': 'Mozilla/5.0'}

        # 遍历html得到所有的a链接
    def get_url(self, url):
        html = requests.get(url, headers=self.headers, auth=self.auth).content.decode('utf-8','ignore')
        # print(html)
        parse_html = etree.HTML(html)
        # print(parse_html.xpath('//a'))
        return parse_html, url
        #判断a链接是否以'/'结束，如果是则继续循环遍历，不是则保存数据
    def get_href(self,html, next_url):
        all_href = html.xpath('//a')
        # print(html,next_url)
        # print(all_href)
        for href_a in all_href:
            href = href_a.xpath('./@href')[0]
            document_name = href_a.xpath('./text()')[0]
            if href == '../':
                print('返回上层界面，不考虑')
            elif href[-1] == '/':
                h, n = self.get_url(next_url+href)
                self.get_href(h, n)
            else:
                #此处不转码，以二进制方式保存
                document = requests.get(url=next_url+href, headers= self.headers, auth=self.auth).content
                self.save_document(next_url+href, document, document_name)

    #判断文件夹是否存在，不存在则创建&&判断文件是否存在，不存在则保存，存在则跳过
    def save_document(self, filename, html, document_name):

        name = document_name
        directory = '/home/tarena/TDD/TRY' + filename[25:-(len(name))]
        print(name)
        print('*'*50)
        print(directory)
        #判断文件夹是否存在
        if not os.path.isdir(directory):
            #递归创建目录
            os.makedirs(directory)
        total_dir = directory + name
        print('*'*50)
        print(total_dir)
        #判断文件是否存在
        if not os.access(total_dir, os.F_OK):
            with open(total_dir, 'wb') as f:
                f.write(html)
            print('%s下载成功'%filename)

    def main(self):
            html, url = self.get_url(self.url)
            self.get_href(html, url)

if __name__ == '__main__':
    spider = GetNoteSpider()
    spider.main()


