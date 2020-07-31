# Scanunauthorized 批量检测各种未授权访问漏洞
###功能
* redis未授权
* Hadoop未授权
* docker未授权
* CouchDB未授权
* ftp未授权
* zookeeper未授权
* elasticsearch未授权
* memcached未授权
* mongodb未授权
* rsync未授权
* mysql未授权
* jenkins未授权
* target未授权
* jboss的未授权访问
检测速度快, 支持批量, 多线程, 使用python3编写。

把整理好的ip放到当前host.txt文本中，使用Python3运行该项目即可。

# 安装-运行
```
pip3 install -r requirements.txt
```
把ip整理好，放到url.txt文本中，运行该项目。
```
python3 Scanunauthorized.py
```
# 结果
打开success.txt文件查看
```
114.80.200.78:11211 memcached未授权
114.80.200.78:873 可能存在rsync未授权,需要手工确认
111.230.246.100:6379 redis未授权
118.24.98.227:6379 redis未授权
61.172.242.251:6379 redis未授权
61.172.242.251:9200 elasticsearch未授权
106.12.106.116:2181 zookeeper未授权
212.64.25.171:6379 redis未授权
111.230.146.171:6379 redis未授权
49.235.151.3:6379 redis未授权
119.81.65.227:6379 redis未授权
64.227.68.159:27017 mongodb未授权
58.177.150.27:6379 redis未授权
118.24.109.25:2181 zookeeper未授权
118.24.108.205:6379 redis未授权
64.227.68.159:6379 redis未授权
118.24.108.205:2181 zookeeper未授权
106.54.239.198:6379 redis未授权
49.232.65.110:9200 elasticsearch未授权
222.134.23.2:2181 zookeeper未授权
35.232.223.85:6379 redis未授权
106.54.11.77:6379 redis未授权
182.254.136.127:6379 redis未授权
49.232.194.199:2181 zookeeper未授权
23.225.102.211:873 可能存在rsync未授权,需要手工确认
116.196.104.110:9200 elasticsearch未授权
111.230.72.192:6379 redis未授权
103.1.49.115:27017 mongodb未授权
61.164.121.35:2181 zookeeper未授权
103.142.139.80:6379 redis未授权
68.183.21.83:873 可能存在rsync未授权,需要手工确认
118.89.119.250:6379 redis未授权
34.64.157.217:6379 redis未授权

```
