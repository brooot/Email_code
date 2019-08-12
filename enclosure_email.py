import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
 
sender = '2802156052@qq.com'
receivers = ['1442704671@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
passwd = "dosmtpsmljioddgc"
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("小火龙", 'utf-8')
message['To'] =  Header("可爱的你", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
 
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('./Email_code/attach.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字（后缀不能改，且前面只能是英文）
att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
message.attach(att1)
 
# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('./Email_code/web.html', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="web.html"'
message.attach(att2)
 
try:
    smtpObj = smtplib.SMTP("smtp.qq.com", port=25)
    smtpObj.login(sender , passwd)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: ", e)