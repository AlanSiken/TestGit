# -*- coding: UTF-8 -*-
from aip import AipOcr
#定义常规变量
APP_ID = 'xxxx'
API_KEY = 'xxxx' 
SECRET_KEY = 'xxxxx'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)#初始化AipFace对象

def Get_File_Contnet(IMG_Path):
    with open(IMG_Path,'rb') as Ip:  #以二进制性质读待识别的图片
        return Ip.read()   #返回PIL读取结果

def main():
    IMG_Path = input('请输入待识别图片的路径：')
    result = aipOcr.basicGeneral(Get_File_Contnet(IMG_Path))#调用通用文字识别, 图片参数为本地图片，并把返回值添加进result
    print('*'*32)
    print('检测到可能有%s行\n内容如下：'%(result['words_result_num']))#取出内容行数
    print('>'*32)
    with open('识别内容.txt','w+') as fd:   #以写+读的形式打开文件，若不存在就新建一个
        fd.write("检测到图片文字可能有 %s 行\n内容如下: "%(result["words_result_num"])+'\n')
    list =result['words_result']  #把返回值中的识别内容添加进列表中
    for i in list:
        print(i['words'])
        with open('识别内容.txt','a') as fd:  #以追加方式写+读打开文件，若不存在就新建一个
            fd.write(i['words'] + '\n')#写入识别内容

if __name__ == '__main__':
    main()
