# @Author : alan
# @File : ALogFry.py

import re
import os

xss = "script<alert|script%3Ealert|img src=|img%20src=|document.domain"
comm = "whoami|ifconfig|ipconfig|wget.*http|dir|curl.*ifs|wget.*ifs|uname|think.*invokefunction|echo|net%20user|net user|phpinfo"
sqlinj = "select.*count|select.*limit|select.*regexp|select.*master|group%20by|group by|union.*select|select.*xp_cmdshell|select.*from"
file = "web.xml|database.properties|config.xml|web_config.xml|known_hosts|htpasswd|DS_Store|boot.ini|win.ini|my.ini|etc/passwd|etc/shadow|httpd.conf|.sql|.svn|.bak"
webshell = "shell.jsp|ant.jsp|server.jsp|i.jsp|shell.php|ant.php|server.php|i.php|shell.asp|ant.asp|server.asp|i.asp"
x = c = s = e = w = 0
if os.path.exists('./log'):
    pathDir = os.listdir('./log/')
    for allDir in pathDir:
        p = os.path.join('./log/' + allDir)
        os.remove(p)
else:
    os.mkdir('./log')
    pathDir = os.listdir('./log/')
    for allDir in pathDir:
        p = os.path.join('./log/' + allDir)
        os.remove(p)
lpathDir = os.listdir('./logs')
if len(lpathDir) < 1:
    print("logs目录下无日志文件！！！")
else:
    for lallDir in lpathDir:
        h = os.path.join('./logs/' + lallDir)
        with open(h, 'rt', encoding='utf-8') as f:
            for i in f:
                # 对字符串进行分割，分割之后以列表形式存在
                n = i.split()
                ip = n[0]
                time = n[3] + n[4]
                method = n[5]
                uri = n[6]
                # XSS攻击检测
                if re.search(xss, uri, re.I):
                    with open('./log/xss.txt', 'at', encoding='utf-8') as f:
                        f.writelines(i)
                    x += 1
                # 命令执行攻击检测
                if re.search(comm, uri, re.I):
                    with open('./log/comm.txt', 'at', encoding='utf-8') as f:
                        f.writelines(i)
                    c += 1
                # sql注入攻击检测
                if re.search(sqlinj, uri, re.I):
                    with open('./log/sqlinj.txt', 'at', encoding='utf-8') as f:
                        f.writelines(i)
                    s += 1
                # 敏感文件攻击检测
                if re.search(file, uri, re.I):
                    with open('./log/file.txt', 'at', encoding='utf-8') as f:
                        f.writelines(i)
                    e += 1
                # webshell连接攻击检测
                if re.search(webshell, uri, re.I):
                    with open('./log/webs.txt', 'at', encoding='utf-8') as f:
                        f.writelines(i)
                    w += 1
            if x > 0:
                ip_list = []
                print('存在xss攻击：' + str(x) + '次')
                with open('./log/xss.txt', 'rt', encoding='utf-8') as f:
                    for i in f:
                        n = i.split()
                        ip = n[0]
                        ip_list.append(ip)

                # print(ip_list)
                ip_new = list(set(ip_list))
                print("攻击ip：")
                for i in range(len(ip_new)):
                    print(ip_new[i])
                with open('./log/xss.txt', 'rt', encoding='utf-8') as f:
                    print("详细攻击日志：")
                    for i in f:
                        # 利用splitlines()去除换行符
                        print(i.splitlines())
                # os.remove(r'../plug/logs/log/xss.txt')
            if c > 0:
                ip_list = []
                print('存在命令执行攻击：' + str(c) + '次')
                with open('./log/comm.txt', 'rt', encoding='utf-8') as f:
                    for i in f:
                        n = i.split()
                        ip = n[0]
                        ip_list.append(ip)

                # print(ip_list)
                ip_new = list(set(ip_list))
                print("攻击ip：")
                for i in range(len(ip_new)):
                    print(ip_new[i])
                with open('./log/comm.txt', 'rt', encoding='utf-8') as f:
                    print("详细攻击日志：")
                    for i in f:
                        print(i.splitlines())
            if s > 0:
                ip_list = []
                print('存在sql注入攻击：' + str(s) + '次')
                with open('./log/sqlinj.txt', 'rt', encoding='utf-8') as f:
                    for i in f:
                        n = i.split()
                        ip = n[0]
                        ip_list.append(ip)

                ip_new = list(set(ip_list))
                print("攻击ip：")
                for i in range(len(ip_new)):
                    print(ip_new[i])
                with open('./log/sqlinj.txt', 'rt', encoding='utf-8') as f:
                    print("详细攻击日志：")
                    for i in f:
                        print(i.splitlines())
            if e > 0:
                ip_list = []
                print('存在敏感文件攻击：' + str(e) + '次')
                with open('./log/file.txt', 'rt', encoding='utf-8') as f:
                    for i in f:
                        n = i.split()
                        ip = n[0]
                        ip_list.append(ip)

                ip_new = list(set(ip_list))
                print("攻击ip：")
                for i in range(len(ip_new)):
                    print(ip_new[i])
                with open('./log/file.txt', 'rt', encoding='utf-8') as f:
                    print("详细攻击日志：")
                    for i in f:
                        print(i.splitlines())
                if w > 0:
                    ip_list = []
                    print('存在webshell连接攻击：' + str(w) + '次')
                    with open('./log/webs.txt', 'rt', encoding='utf-8') as f:
                        for i in f:
                            n = i.split()
                            ip = n[0]
                            ip_list.append(ip)

                    ip_new = list(set(ip_list))
                    print("攻击ip：")
                    for i in range(len(ip_new)):
                        print(ip_new[i])
                    with open('./log/webs.txt', 'rt', encoding='utf-8') as f:
                        print("详细攻击日志：")
                        for i in f:
                            print(i.splitlines())
