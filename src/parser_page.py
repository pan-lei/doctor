#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 15:41
# @Author  : 潘磊
# @function: 获取分页数据中的 科室url  2-10页的url，并保存到以科室名命名的文件中

from bs4 import BeautifulSoup
import urllib.parse as up

class PageParser(object):
    def parsePage(self, name, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(
            html_cont,                  # 网页源代码
            'html.parser',              # 解析器
            from_encoding="gb18030"
        )
        self._get_page_urls(name, url, soup)         # 由 根url 获取 科室的url



    # 获取 2-30 页url
    def _get_page_urls(self, name, url, soup):
        ''' 网页内容分析
        <div class="pagebar">
	
		    <a class="prev disabled" href="javascript:void(0)">上一页</a>
	
	        <a class="page" href="javascript:void(0)">1</a>
	 
		    <a class="next" href="/pc/qalist/clinicno_4/?page=2#hotqa">下一页</a>
	
        </div>
        '''
        file_name = 'E:\PythonProject\doctor\department\\' + name + '.txt'
        fw = open(file_name, 'w', encoding='utf-8')
        try:
            node = soup.find('div', class_="pagebar").find('a', class_="next")
            # print(node)
            new_url = node['href']                      # 获取<a>中的链接
            # print(new_url)
            fw.write(url)
            for i in range(2,31):
                new_url_temp = ''.join([url[:-1], '?page=',str(i), '#', new_url.split('#')[1]])
                # print(new_url_temp)
                new_url_full = up.urljoin(url, new_url_temp)  # 使新的链接格式进行规范
                # print(new_url_full)
                fw.write(new_url_full)
                fw.write('\n')

        except:
            print('获取页数出错了')

        fw.close()
