from lxml import etree
import time
import requests
import random
from useragent import ua_list
import os

class ClSpider_novel(object):
    def __init__(self):
        self.url = 'http://xn--5uw.ml/thread0806.php?fid=20&search=&page={}'
        self.page = 1
        self.file_path = ''

    def get_page(self, url):
        html = requests.get(url, headers = {'User-Agent':random.choice(ua_list)}).content.decode('gbk','ignore')
        return html

    def parse_page(self,url):
        html = self.get_page(url)
        parse_html = etree.HTML(html)
        #基准xpath
        dd_list = parse_html.xpath('//h3')
        #获得一页的所有内容和链接的上一层对象h3
        #for循环h3，将每一个链接进行二次解析，调用parse_page_two
        for dd in dd_list:
            two_page_link = dd.xpath('./a/@href')[0]
            two_page_link = 'http://xn--5uw.ml/'+two_page_link
            self.parse_page_two(two_page_link)

    def parse_page_two(self, url):
        #接收parse_page传过来的地址，并解析得到html
        html = self.get_page(url)
        #基准xpath
        parse_html = etree.HTML(html)
        #获得一页的<h4>和保存内容<div>[0]
        name = parse_html.xpath('//h4/text()')
        content = parse_html.xpath('//div[@class="tpc_content do_not_catch"]/text()')
        content_total = ''
        if name and content:
            name = name[0]
            if len(content[0])>=30:
                for i in content:
                    content_total+=i
                # 调用write_page函数，将名称和内容保存
                self.write_page(name, content_total)
    def write_page(self, name, content):
        #接收parse_page_two内容，写入本地txt
        filename = self.file_path + '/' + name + 'txt'
        with open(filename, 'w') as f:
            f.write(content)

    def main(self):
        for page in range(0,21):
            url = self.url.format(page)
            # 每一页建立一个单独文件夹
            self.file_path = './小说/' + str(self.page)
            os.mkdir(self.file_path)

            self.parse_page(url)
            # time.sleep(random.randint(1,3))
            print('第{}页爬取完成'.format(self.page))
            self.page += 1

if __name__ == '__main__':
    start = time.time()
    spider = ClSpider_novel()
    spider.main()
    end = time.time()
    print('爬取共耗时{}'.format(end-start))

##<h3><a href="htm_data/1907/20/3575953.html" target="_blank" id="">内容</a></h3>
##http://xn--5uw.ml/htm_data/0805/20/140845.html
#<h4>文章题目</h4>
#<div class="tpc_content do_not_catch">[0]