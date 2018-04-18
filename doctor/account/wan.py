#!/usr/bin/env python  
# -*-coding:utf8-*-  
import re
import requests
from bs4 import BeautifulSoup
import urllib 
import time
import MySQLdb
import os
import sys
import django

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctor.settings")
 
django.setup()

"""def insert_news(biaoti,lianjie,zuozhe,chuchu,shouluchu,jianjie,guanjianci,time):
    cursor.execute("INSERT IGNORE INTO zhongliu VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",(biaoti,lianjie,zuozhe,chuchu,shouluchu,jianjie,guanjianci,time))
    connection.commit()

def create_table():
    cursor.execute("CREATE TABLE zhongliu (biaoti varchar(255),lianjie varchar(255),zuozhe varchar(255),chuchu varchar(255),shouluchu varchar(255),jianjie varchar(255),guanjianci varchar(255),time varchar(255))")
    #connection.commit()

def insert_doc(biaoti,time):
    cursor.execute("INSERT IGNORE INTO infocenter_document (Dtitle,Dpub_date) VALUES(%s,%s);",(biaoti,time))
    print("yes")"""
from account.models import Document

def get_docu(ci):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}#requests headers信息
    for page in range(1,10):
        url = "http://s.wanfangdata.com.cn/Paper.aspx?q=%s&f=top&p=%i"%(ci,page)#可修改页码page
        biaoti=[];lianjie=[];zuozhe=[];chuchu=[];jianjie=[];guanjianci=[];#shouluchu=[]
        html = requests.get(url,headers = headers).text
        soup = BeautifulSoup(html,"lxml")
        souplist = soup.find_all("div",{"class":"record-item"})
        for soups in souplist:#爬取每一页的信息
            try:
                title = soups.find("a",{"class":"title"})
                biaoti.append(title.get_text())
                lianjie.append(title.get("href"))
                soup_creators = soups.find_all("a",{"class":"creator","target":"_blank"})
                all_creator=''
                for creator in soup_creators:
                    all_creator=all_creator+creator.get_text()+","
                zuozhe.append(all_creator.rstrip(','))
                #print("出处为\n"+soups.find("a",href = re.compile("http://c.wanfangdata.com.cn/Periodical")).get_text()+soups.find("a",href = re.compile("http://c.wanfangdata.com.cn/periodical")).get_text())
                chuchu.append(soups.find("a",href = re.compile("http://c.old.wanfangdata.com.cn/Periodical")).get_text()+soups.find("a",href = re.compile("http://c.old.wanfangdata.com.cn/periodical")).get_text())
                """shouluxinxi = soups.find("span",{"class":"core"})
                shoulu_list = shouluxinxi.find_all("span")
                all_shoulu=''
                for shoulu in shoulu_list:
                    all_shoulu=all_shoulu + shoulu.get("title") + ","
                shouluchu.append(all_shoulu.rstrip(','))"""
                jianjie.append(soups.find("div",{"class":"record-desc"}).get_text().strip())
                soup_guanjianci = soups.find("div",{"class":"record-keyword"})
                guanjiancis = soup_guanjianci.find_all("span")
                all_guanjianci=''
                for soup_guanjianci in guanjiancis:
                    all_guanjianci = all_guanjianci + soup_guanjianci.get_text() + ","
                guanjiancijihe=all_guanjianci
                guanjianci.append(guanjiancijihe.rstrip(','))
            except AttributeError,e:
                #此处有信息缺失
                pass
        localtime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        for i in range(0,len(biaoti)-1):
            obj = Document(Dsummary = jianjie[i],Dkeyword=ci, Dauther = zuozhe[i],Dshoulu_date=chuchu[i] ,Dtitle = biaoti[i],Dpub_date=localtime,Durl=lianjie[i])
            try:
                obj.save()
            except :
                pass
            
#ci = "肺癌"#填入关键词

if __name__ == "__main__":
    get_docu("")
    pass
