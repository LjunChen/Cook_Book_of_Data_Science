from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

host_server='smtp.163.com'
sender='chenliujun0556@163.com'
pwd='*****'
receivers_list=[['sven163','chenliujun0556@163.com'],['svenfudan','19110690005@fudan.edu.cn']]

for receiver in receivers_list:
    mail_title = 'python办公自动化的邮件'
    mail_content = '''Dear {}:
    <p>你好，这是一个测试邮件,</p>
    <p><a href="http://www.baidu.com">百度</a></p>
    <p>图片演示：</p>
    '''.format(receiver[0])
    msg = MIMEMultipart()
    msg['Subject'] = Header(mail_title, 'utf-8')
    msg['From'] = sender
    msg['To'] = Header(receiver[1])
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    #msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    ###插入附件
    attachment = MIMEApplication(open('D:/test.xlsx', 'rb').read())
    attachment.add_header('content-Disposition', 'attachment', filename='test.xlsx')
    msg.attach(attachment)
    try:
        smtp = SMTP_SSL(host_server)
        smtp.ehlo(host_server)
        smtp.login(sender, pwd)
        smtp.sendmail(sender, receiver[1], msg.as_string())
        smtp.quit()
    except:
        print('发送给{}的邮件失败了'.format(receiver[1]))