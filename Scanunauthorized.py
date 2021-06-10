# coding=utf-8
import ftplib, threading, requests, pymongo, pymysql, socket
import psycopg2
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import time

R = threading.Lock()


def file_write(text):
    global R
    R.acquire()
    f = open('success.txt', 'a', encoding='utf-8').write(text + '\n')
    R.release()


def redis(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 6379))
        s.send(bytes("INFO\r\n", 'UTF-8'))
        result = s.recv(1024).decode()
        if "redis_version" in result:
            print(ip + ":6379 redis未授权")
            file_write(ip + ":6379 redis未授权")
        s.close()
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


def mongodb(ip):
    try:
        conn = pymongo.MongoClient(ip, 27017, socketTimeoutMS=4000)
        dbname = conn.list_database_names()
        print(ip + ":27017 mongodb未授权")
        file_write(ip + ":27017 mongodb未授权")
        conn.close()
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


def memcached(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 11211))
        s.send(bytes('stats\r\n', 'UTF-8'))
        if 'version' in s.recv(1024).decode():
            # print(s.recv(2048).decode())
            print(ip + ":11211 memcached未授权")
            file_write(ip + ":11211 memcached未授权")
        s.close()
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def elasticsearch(ip):
    try:
        url = 'http://' + ip + ':9200/_cat'
        r = requests.get(url, timeout=5)
        if '/_cat/master' in r.content.decode():
            print(ip + ":9200 elasticsearch未授权")
            file_write(ip + ":9200 elasticsearch未授权")
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


def zookeeper(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 2181))
        s.send(bytes('envi', 'UTF-8'))
        data = s.recv(1024).decode()
        s.close()
        if 'Environment' in data:
            print(ip + ":2181 zookeeper未授权")
            file_write(ip + ":2181 zookeeper未授权")
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


def ftp(ip):
    try:
        ftp = ftplib.FTP()
        ftp.connect(ip, 21, timeout=5)  # 连接的ftp sever和端口
        ftp.login('anonymous', 'Aa@12345678')
        print(str(ip) + ":21 FTP未授权")
        file_write(str(ip) + ":21 FTP未授权")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def CouchDB(ip):
    try:
        url = 'http://' + ip + ':5984' + '/_utils/'
        r = requests.get(url, timeout=5)
        if 'couchdb-logo' in r.content.decode():
            print(ip + ":5984 CouchDB未授权")
            file_write(ip + ":5984 CouchDB未授权")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def docker(ip):
    try:
        url = 'http://' + ip + ':2375' + '/version'
        r = requests.get(url, timeout=5)
        if 'ApiVersion' in r.content.decode():
            print(ip + ":2375 docker api未授权")
            file_write(ip + ":2375 docker api未授权")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def Hadoop(ip):
    try:
        url = 'http://' + ip + ':50070' + '/dfshealth.html'
        r = requests.get(url, timeout=5)
        if 'hadoop.css' in r.content.decode():
            print(ip + ":50070 Hadoop未授权")
            file_write(ip + ":50070 Hadoop未授权")
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


def rsync_access(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 873))
        s.send(bytes("", 'UTF-8'))
        result = s.recv(1024).decode()
        # print(result)
        if "RSYNCD" in result:
            print(ip + ":873 可能存在rsync未授权,需要手工确认")
            file_write(ip + ":873 可能存在rsync未授权,需要手工确认")
        s.close()
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def mysql_Empty_pwd(ip):
    try:
        conn = pymysql.connect(host=ip, user='root', password='', charset='utf8', autocommit=True)
        print(ip + ":3306 存在mysql空口令漏洞")
        file_write(ip + ":3306 存在mysql空口令漏洞")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def jenkins(ip):
    try:
        url = 'http://' + ip + ':8080' + '/systemInfo'
        r = requests.get(url, timeout=8, verify=False)
        if 'jenkins.war' in r.content.decode() and 'JENKINS_HOME' in r.content.decode():
            print(ip + ":8080 发现jenkins 未授权")
            file_write(ip + ":8080 发现jenkins 未授权")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def jboss(ip):
    try:
        url = 'http://' + ip + ':8080' + '/jmx-console/HtmlAdaptor?action=displayMBeans'
        r = requests.get(url, timeout=8, verify=False)
        if 'JBoss JMX Management Console' in r.content.decode() and r.status_code == 200 and 'jboss' in r.content.decode():
            print(ip + ":8080 发现jboss未授权访问")
            file_write(ip + ":8080 发现jboss未授权访问")
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)


def postgres(ip):
    try:
        conn = psycopg2.connect(database="postgres", user="postgres", password="", host=ip, port="5432")
        print(ip + ":5432 存在postgres未授权")
        file_write(ip + ":5432 存在postgres未授权")
    except Exception as e:
        # print(e)
        pass
    finally:
        pass
        bar.update(1)


# 目前支持：redis,Hadoop,docker,CouchDB,ftp,zookeeper,elasticsearch,memcached,mongodb,rsync_access,mysql,target,jenkins,target,jboss的未授权访问，检测速度快

if __name__ == '__main__':
    print("""********************************************************************                                                                                                                                                                                                                                                                                     
作者微信：f==
********************************************************************""")
    time.sleep(2)
    ipfile = open('host.txt', 'r', encoding='utf-8').read().split('\n')
    bar = tqdm(total=len(ipfile) * 14)
    pool = ThreadPoolExecutor(500)
    for target in ipfile:
        target = target.strip()
        pool.submit(redis, target)
        pool.submit(Hadoop, target)
        pool.submit(docker, target)
        pool.submit(CouchDB, target)
        pool.submit(ftp, target)
        pool.submit(zookeeper, target)
        pool.submit(elasticsearch, target)
        pool.submit(memcached, target)
        pool.submit(mongodb, target)
        pool.submit(rsync_access, target)
        pool.submit(mysql_Empty_pwd, target)
        pool.submit(jenkins, target)
        pool.submit(jboss, target)
        pool.submit(postgres, target)
