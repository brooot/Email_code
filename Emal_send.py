import smtplib
from email.mime.text import MIMEText
from email.header import Header
def email_send():
    sender = '2802156052@qq.com'   #发送人邮箱
    passwd = 'dosmtpsmljioddgc' #发送人邮箱授权码
    receivers = '1442704671@qq.com' #收件人邮箱
    subject = 'python 邮件测试' #主题
    content = 'test again'    #正文
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender # 设置发送人
    print(msg['From'])
    msg['TO'] = receivers+','+sender # 设置接受人
    print(msg['TO'])
    try:
        s = smtplib.SMTP_SSL('smtp.qq.com',465)
        print("连接邮件服务器成功！")
    except Exception as e:
        print("连接服务器失败：" + e)
        return
    try:
        s.login(sender,passwd)
        print("登陆成功！")
    except Exception as e:
        print("登陆失败：",e)
        return
    try:
        s.sendmail(sender,receivers,msg.as_string())
        print('发送成功！')
    except Exception as e:
        print('发送失败:',e)

email_send()