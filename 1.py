from urllib import request
from bs4 import BeautifulSoup
import re
import json
shequList=[{
	"name":"重庆社区",
	"img":["","",""]
}]
shequName=["重庆社区","南京社区"]
p=0
djpage=0
fileName="data.sql"
def glyh(cs):
	cs.replace("'", "\\'")
	cs.replace("\"", "\\'")
	return cs
def okpa(http) :
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		global p
		p=p+1
		print("当前第"+str(int(djpage))+"页 第"+str(int(p))+"条");
		print(http);
		bf = BeautifulSoup(html,"lxml")
		if bf.find_all("iframe"):
			src = bf.find_all("iframe")[0].attrs['src']
		else:
			src=http
		src=src.replace("https:","")
		src=src.replace("salerinfo.html","")
		#print(bf.find_all("div",class_="fix-im-cate")[0].get_text())
		response2 = request.urlopen("https:"+src)
		html2 = response2.read()
		bf2 = BeautifulSoup(html2,"lxml")
		if bf2.find_all("img",id="head-img"):
			img=bf2.find_all("img",id="head-img")[0].attrs['src']		#头像地址
		elif bf2.find_all("div",class_="w-head-pic"):
			img=bf2.find_all("div",class_="w-head-pic")[0].find('img').attrs['src']		#头像地址
		else:
			img="无"
		if bf2.find_all("h1",class_="title"):
			title=bf2.find_all("h1",class_="title")[0].get_text()		#店铺名称
		elif bf2.find_all("div",class_="w-head-pic"):
			title=bf2.find_all("div",class_="w-head-pic")[0].find('img').attrs['alt']		#店铺名称
		else:
			title="无"
		if(len(bf2.find_all("div",class_="no-about"))>0):
			jianjie="暂无店铺介绍"
		elif bf2.find_all("pre",class_="content-item morestatus content-item-info1"):
			jianjie= bf2.find_all("pre",class_="content-item morestatus content-item-info1")[0].get_text()		#公司简介
		elif bf2.find_all("p",class_="introduce-company-msg"):
			jianjie=bf2.find_all("p",class_="introduce-company-msg")[0].get_text()
		else:
			jianjie="无"
		if(bf2.find_all("div",class_="info-content")):
			gongsi=bf2.find_all("div",class_="info-content")[0].get_text()		#公司名称
			address=bf2.find_all("div",class_="info-content")[3].get_text()		#公司地址
		else:
			gongsi="无"
			address="无"
		fuwuarray=[]
		if(bf2.find_all("div",class_="category-item")):
			fuwu=bf2.find_all("div",class_="category-item")		#公司服务
			for o in fuwu:
				fuwuarray.append(o.get_text())				#存储为数组
		else:
			fuwuarray.append("无")
		if(bf2.find_all("img",class_="certificate-img lazy")):	
			yingye = bf2.find_all("img",class_="certificate-img lazy")[0].attrs['data-original'];		#营业执照
		else:
			yingye="无"
		shequAddress=""
		sname=""
		sphone=""
		if(bf2.find_all("a",class_="zworks-item")):
			shequlen=len(bf2.find_all("a",class_="zworks-item"))
			shequ=bf2.find_all("a",class_="zworks-item")[0]
			sqName=shequ.get_text();			#社区名字
			sqsrc = shequ.attrs['href']     	#社区地址
			response3 = request.urlopen(sqsrc)
			html3 = response3.read()
			bf3 = BeautifulSoup(html3,"lxml")
			gwimg=[]
			gwimgList=bf3.find_all("img",style="width:100%;height: 100%;")
			shequList = bf3.find_all("div",class_="info-form-head-right")
			bsq=[] #社区用户信息
			for d in shequList:
				sname=d.find("div",class_="head-title").get_text()
				sphone=d.find("div",class_="head-title-phone").get_text()
				a={}
				a['name']=sname
				a['phone']=sphone
				bsq.append(a)
			if bf3.find_all("p",class_="zwork-positon"):
				shequAddress=bf3.find_all("p",class_="zwork-positon")[0].get_text()		#社区地址
			else:
				shequAddress="无"
			for i in gwimgList:
				gwimg.append(i.attrs['src'])
		else:
			sqsrc="无"
			sqName="无"
			gwimg=""
			bsq=""
		'''
		for i in range(shequlen):
			shequ=bf2.find_all("a",class_="zworks-item")[i]
			sqName=shequ.get_text();
			if sqName in shequName:
				dqshequ.append(sqName)
			else:
				dqshequ.append(sqName)
				shequName.append(sqName)
		'''
		img=glyh(img)
		bsq=json.dumps(bsq)
		title=glyh(title)
		jianjie=glyh(jianjie)
		gongsi=glyh(gongsi)
		address=glyh(address)
		yingye=glyh(yingye)
		shequAddress=glyh(shequAddress)
		sqName=glyh(sqName)
		sqsrc=glyh(sqsrc)
		sql='INSERT INTO `gongsi`.`gsinfo` SET `title`="'+title+'",`jianjie`="'+jianjie+'",`gsname`="'+gongsi+'",`address`="'+address+'",`yingye`=\''+yingye+'\',`fuwu`=\''+json.dumps(fuwuarray)+'\',`url`=\''+glyh(url)+'\',`logo`="'+img+'",`shequ`="'+sqName+'",`shequUser`=\''+bsq+'\',`shequAddress`="'+shequAddress+'",`shequimg`=\''+json.dumps(gwimg)+'\';'
		with open(fileName,'a',encoding='utf-8') as f:    #设置文件对象
			f.write(sql)                 #将字符串写入文件中
def palist(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		print("开始"+http);
		bf = BeautifulSoup(html,"lxml")
		global djpage
		listindex=bf.find_all("div",class_="pagination")[0].find_all("li",class_="active")[0].find('a').get_text();
		djpage=listindex
		list=bf.find_all("a",class_="name")
		listlen=len(bf.find_all("a",class_="name"))
		z=0
		for i in list:
			z=z+1
			if z>=listlen:
				palist(paindex(http))
				print(paindex(http));
			else:
				i=i.attrs['href'].replace("?fr=djwy", "")
				newurl="https:"+i+"salerinfo.html";
				#print(str(z)+" " + str(listlen));
				okpa(newurl)
def paindex(http):
	if __name__ == "__main__":
		response = request.urlopen(http)
		html = response.read()
		#print("开始");
		bf = BeautifulSoup(html,"lxml")
		listindex=len(bf.find_all("div",class_="pagination")[0].find_all("li"));
		w=0
		for d in range(listindex):
			w=w+1
			t="active"
			s=str(bf.find_all("div",class_="pagination")[0].find_all("li")[d])
			if(t in s):
				break

		list=bf.find_all("div",class_="pagination")[0].find_all("li")
		page=list[w].find("a").attrs['href']					#下一个
		return "https://"+http.split("/")[2]+page;
url = input("输入爬取的列表地址：")
fileName = input("输入保存的文件名称(例如：data.sql)：")
palist(url);
