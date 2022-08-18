# ALogFry
基于python实现的web日志分析工具

python3 ALogFry.py


存在xss攻击：4次
攻击ip：
198.104.32.12
12.182.23.13
127.0.0.1
详细攻击日志：
['127.0.0.1 - - [06/Jul/2022:18:10:35 +0800] "GET /xss-labs/level1.php?name=%3CScRiPt%3Ealert(\'XSS\');%3C/ScRiPt%3E HTTP/1.1" 200 502']
['12.182.23.13 - - [06/Jul/2022:18:11:21 +0800] "GET /xss-labs/level2.php?keyword=%3CScRiPt%3Ealert(\'XSS\');%3C/ScRiPt%3E HTTP/1.1" 200 704']
['198.104.32.12 - - [06/Jul/2022:18:22:21 +0800] "GET /xss-labs/level2.php?keyword=%3CScRiPt%3Ealert(\'XSS\');%3C/ScRiPt%3E HTTP/1.1" 200 704']
['127.0.0.1 - - [06/Jul/2022:18:30:18 +0800] "GET /xss-labs/level2.php%22%3E%3CScRiPt%3Ealert(\'XSS\');%3C/ScRiPt%3E HTTP/1.1" 403 2208']
存在命令执行攻击：4次
攻击ip：
12.231.21.1
127.0.0.1
详细攻击日志：
['127.0.0.1 - - [06/Jul/2022:18:24:55 +0800] "GET /xss-labs/level2.php?keyword=wget%20http://www.test.com HTTP/1.1" 200 716']
['12.231.21.1 - - [06/Jul/2022:18:26:59 +0800] "GET /xss-labs/level2.php?keyword=test(whoami) HTTP/1.1" 200 716']
['127.0.0.1 - - [06/Jul/2022:18:27:20 +0800] "GET /xss-labs/level2.php?keyword=ifconfig HTTP/1.1" 200 716']
['127.0.0.1 - - [06/Jul/2022:18:33:21 +0800] "GET /xss-labs/level2.php?keyword=ipconfig HTTP/1.1" 200 712']
存在sql注入攻击：2次
攻击ip：
192.52.2.134
127.0.0.1
详细攻击日志：
['127.0.0.1 - - [06/Jul/2022:18:30:18 +0800] "GET /xss-labs/level2.php?keyword=1%20select%20id%20from%20test HTTP/1.1" 200 712']
['192.52.2.134 - - [06/Jul/2022:18:30:18 +0800] "GET /xss-labs/level2.php?keyword=2%20union%20select(1,2,3) HTTP/1.1" 200 712']
