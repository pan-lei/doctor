#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/26 10:12
# @Author  : 潘磊
# @function:

import re
from bs4 import BeautifulSoup
import urllib.parse as up


class HtmlParser(object):

    def parseRoot(self, url, html_cont):
        '''
        获取网页中的url以及内容
        '''
        # print("进入parse(self, url, html_cont)函数")
        if url is None or html_cont is None:
            return
        # print(len(html_cont))
        soup = BeautifulSoup(
            html_cont,      # 网页源代码
            'html.parser',   # 解析器
            from_encoding="gb18030"
        )
        new_urls = self._get_department_urls(url, soup)         # 由 根url 获取 科室的url
        # new_data = self._get_new_data(url, soup)
        return new_urls

    def parseDepartment(self, url, html_cont):
        # print("进入parse(self, url, html_cont)函数")
        if url is None or html_cont is None:
            return
        # print(len(html_cont))
        soup = BeautifulSoup(
            html_cont,  # 网页源代码
            'html.parser',  # 解析器
            from_encoding="gb18030"
        )
        # print(html_cont)
        new_urls = self._get_problem_urls(url, soup)  # 由 科室的url 获取
        # new_data = self._get_new_data(url, soup)
        return new_urls

    def parseProblem(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(
            html_cont,  # 网页源代码
            'html.parser',  # 解析器
            from_encoding="gb18030"
        )
        # print(html_cont)
        self._get_dialog_content(url, soup)  # 由 问题url 获取 对话
        # return cont


    def _get_department_urls(self, url, soup):
        '''
        获取新的url列表
        '''
        # print("进入_get_new_urls(self, url, soup)函数")
        new_urls = set()
        fo = open('E:\PythonProject\doctor\html\department_urls.txt', 'w', encoding='utf-8')
        ''' 网页内容分析
        <ul class="tab-type-one first-clinic j-tab-wrap">
		
			<li class="tab-item cur">
				<a href="/pc/qalist/clinicno_4/">皮肤性病科</a>
			</li>
		
			<li class="tab-item">
				<a href="/pc/qalist/clinicno_1/">妇科</a>
			</li>
		
		</ul>
        '''
        nodes = soup.find('ul', class_="tab-type-one first-clinic j-tab-wrap").find_all('li')
        # print(nodes)
        # print('-------------------')
        for node in nodes:
            # print(node)
            dep_name = node.find('a').get_text()                          # 获取科室名字
            new_url = node.find('a')['href']                              # 获取<a>中的链接
            # print(new_url)
            new_url_full = up.urljoin(url, new_url)                       # 使新的链接格式进行规范
            new_urls.add(new_url_full)
            # print(new_url_full)
            new_urls.add(new_url_full)
            fo.write(new_url_full)
            fo.write('\n')

        fo.close()
        return new_urls

    # 获取问题url
    def _get_problem_urls(self, url, soup):
        new_urls = set()
        fo = open('E:\PythonProject\doctor\html\problem_urls.txt', 'a+', encoding='utf-8')
        ''' 网页内容分析
        <div class="hot-qa main-block">
	
            <div class="hot-qa-item  first ">
                <div class="qa-item qa-item-ask">
                    <a href="/pc/qa/6OqdUlIBYG4SksGSuTxmLg/" target="_blank">
                        <i class="ask-tag">问</i>
                        
                            为什么我的背上长了这么多痘痘,会挠出血
                        
                    </a>
                </div>
                <div class="qa-item qa-item-answer">
                    <i class="ask-tag answer-tag">答</i>
                    你好，平时脸上长红色的痘痘...
                </div>
                
                <div class="qa-item qa-item-doctor">
                    <em>李朝辉</em>
                    南宫妇幼保健院
                </div>
                
                <span class="date">2018-03-23</span>
            </div>
        
            <div class="hot-qa-item ">
                <div class="qa-item qa-item-ask">
                    <a href="/pc/qa/qUUHRYRZy_g7q5bDIIeRGw/" target="_blank">
                        <i class="ask-tag">问</i>
                        
                            青春期毛孔粗大长痘痘怎么办
                        
                    </a>
                </div>
                <div class="qa-item qa-item-answer">
                    <i class="ask-tag answer-tag">答</i>
                    用过药吗？ 有效果吗？ 什么药物 ...
                </div>
                
                <div class="qa-item qa-item-doctor">
                    <em>宋跃林</em>
                    吉林省图们市人民医院
                </div>
                
                <span class="date">2018-03-23</span>
            </div>
	
        </div>
        '''
        nodes = soup.find('div', class_="hot-qa main-block").find_all('div', class_="qa-item qa-item-ask")
        # print(nodes)
        # print('-------------------')
        for node in nodes:
            # print(node)
            new_url = node.find('a')['href']                              # 获取<a>中的链接
            # print(new_url)
            new_url_full = up.urljoin(url, new_url)                       # 使新的链接格式进行规范
            new_urls.add(new_url_full)
            # print(new_url_full)
            new_urls.add(new_url_full)
            fo.write(new_url_full)
            fo.write('\n')

        fo.close()
        return new_urls

    def _get_dialog_content(self, url, soup):
        fo = open('E:\PythonProject\doctor\html\dialog_cont.txt', 'a+', encoding='utf-8')
        '''网页内容分析
        <div class="problem-detail-wrap">
            <div class="tip-msg">
                <p>提示：疾病因人而异，他人的咨询记录仅供参考，擅自治疗存在风险。</p>
            </div>
            <div class="block-line">
                <img class="avatar-left" src="https://media2.chunyuyisheng.com/@/media/images/2017/04/22/c072/8a13d525d3a4_w48_h48_.png" alt="用户头像">
                <div class="context-left">
                    <h6 class="doctor-name">患者</h6>
                    <p class="paragraph-detail right blue">
                        走路滑了下然后膝盖错位了，然后1'2分钟后又归位了，没有看医生现在第三天了，还是肿的？怎么会好的快点呢？（女，24岁）<br>
                    </p>
                </div>
            </div>
		  
		    <div class="elite-recommendation"></div>
			
				<div class="block-line">
				
					<img class="avatar-left" src="https://media2.chunyuyisheng.com/@/media/images/2018/02/12/11e6f7be5ebe_w325_h325_.jpg?imageMogr2/thumbnail/150x" alt="">
					<div class="context-left">
						<h6 class="doctor-name">周世荣医生</h6>
						
							<p class="paragraph-detail left">
								
                                错位后需要固定一段时间，即使复位了也有周围韧带损伤

							</p>
						
					</div>
				
				</div>
			
				<div class="block-line">
				
					<img class="avatar-left" src="https://media2.chunyuyisheng.com/@/media/images/2017/04/22/c072/8a13d525d3a4_w48_h48_.png" alt="用户头像">
					<div class="context-left">
						<h6 class="doctor-name">患者</h6>
						
							<p class="paragraph-detail right blue">
								
                                那我要去医院检查看看吗？

							</p>
						
					</div>
				
				</div>
			
				<div class="block-line">
					<img class="avatar-left" src="https://media2.chunyuyisheng.com/@/media/images/2018/02/12/11e6f7be5ebe_w325_h325_.jpg?imageMogr2/thumbnail/150x" alt="">
					<div class="context-left">
						<h6 class="doctor-name">周世荣医生</h6>
							<p class="paragraph-detail left">
                                现在除了肿还有其他症状吗
							</p>
					</div>
				</div>
		</div>
        '''
        # print('hello')
        # nodes = soup.find('div', class_="problem-detail-wrap").find_all('div', class_='block-line')
        nodes = soup.find('div', class_="problem-detail-wrap").find_all('p')
        # print(nodes)
        num = 0
        fo.write(str(num) + '\n')
        for node in nodes:
            dic = node.attrs       # dic = {'class': ['paragraph-detail', 'right', 'blue']}
            num += 1
            # 存在问题，因为dic是一个字典类型，但在这里直接用dic['class']却无法获取其value值
            # 只能用下面这种折中的方法
            # key = 'class'     # 这样也不行
            # print(dic[key])
            # 这样才可以
            for i in dic:     # i = 'class'
                # print(dic[i])
                # print(dic[i][1])      # dic[i][1] = right 或者 left
                if dic[i][1] == 'right':
                    print('患者说:' + node.get_text().strip())
                    fo.write('患者说:' + node.get_text().strip() + '\n')
                elif dic[i][1] == 'left':
                    print('医生说:' + node.get_text().strip())
                    fo.write('医生说:' + node.get_text().strip() + '\n')
                else:
                    print('------无对话------')
        fo.close()






    def _get_new_data(self, url, soup):
        '''
        获取内容
        '''
        data = {}
        data['url'] = url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        # title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        # data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        # summary_node = soup.find('div', class_ = "lemma-summary")
        # data["summary"] = summary_node.get_text()

        return data

