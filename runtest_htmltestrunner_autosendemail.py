# coding=utf-8
'''
Created on 2016-7-26
@author: xxx
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from test_case import test_baidu
from test_case import test_youdao


#定义：取最新测试报告
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path

def send_email(newfile):
    f=open(newfile,'rb')
    mail_body=f.read()
    #调试使用
    #print u'打印'
    #print mail_body
    f.close()

    #发送邮箱服务器
    smtpserver = 'xxx.xxx.com'
    #发送邮箱
    sender = 'xxx@xxx.com'
    #发送邮箱用户名/密码
    user = "xxx@xxx.com"
    password = 'xxxx'
    #发送邮件主题
    subject = 'Script Failure Rate Weekly Report'

    #接收邮箱 多个接收邮箱receiver=['XXX@126.com','XXX@126.com','XXX@doov.com.cn']
    receiver='xxx@163.com'

    #编写 HTML类型的邮件正文
#    MIMEText这个效果和下方用MIMEMultipart效果是一致的
#    msg = MIMEText(mail_body,'html','utf-8')
    msg=MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body,'html','utf-8')
    msg.attach(msg_html1)

    #添加附件
    msg_html = MIMEText(mail_body,'html','utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    
    msg['From'] = 'xxx@xxx.com<xxx@xxx.com>'
    msg['To'] = "xxx@163.com"
    #msg['Subject']=Header(subject,'utf-8')
    msg['Subject']=subject
#    msg['Date']=time.strftime('%Y-%m-%d')

    #连接发送邮件
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver,25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__=='__main__':
    #执行测试
    print ('=====AutoTest Start======')

    test_dir = 'C:\\Users\\lxm\\Desktop\\test_project\\test_case'
    #测试报告的路径
    test_report_dir='E:\\MATT\\pythontest\\testresult'
    
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir+'\\'+ now + 'result.html'
    fp=open(filename ,'wb')
    
    runner = HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况：')
    runner.run(discover)
    fp.close() 
    
    #2.取最新测试报告
    new_report=new_file(test_report_dir)
    
    #3.发送邮件，发送最新测试报告html
    send_email(new_report)
    print ('=====AutoTest Over======')
    
