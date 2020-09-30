'''
数据库操作
'''
import pymysql

class Mysql:
    def connect(self, db):
        '''
        连接数据库
        :param db: 字典格式 db={"ip":"192.168.150.52","post":"3306","name":"future","user":"root","pwd":"123456"}
        :return:
        '''
        ip=db["ip"]
        port=int(db["port"])
        name=db["name"]
        user=db["user"]
        pwd=db["pwd"]
        try:
            conn=pymysql.connect(host=ip,port=port,user=user,password=pwd,charset="utf8",database=name)
            print(f"连接数据库{ip}·{port}成功")
            return conn
        except Exception as e:
            print(f"连接数据库异常·异常信息为{e}")
    def execute(self,conn,sql):
        '''

        :param conn:
        :param sql:
        :return:
        '''
        try:
            cursor=conn.cursor()  #获取游标
            cursor.execute(sql)#使用游标执行sql
            conn.commit()
            cursor.close()#释放游标
            print(f"执行sql语句{sql}")
        except Exception as e:
            print(f"执行数据库语句异常·异常信息为{e}")
    def disconnect(self,conn):
        '''
        断开数据库
        :param conn:
        :return:
        '''
        try:
            conn.close()
        except Exception as e:
            print(f"断开数据库异常·异常信息为{e}")
if __name__ == '__main__':
    db={"ip":"192.168.150.52","post":"3306","name":"apple","user":"root","pwd":"123456"}
    conn=Mysql().connect(db)
    print(conn)
    Mysql().execute(conn,"delete from member where mobilephone=13227011051;")
    Mysql().disconnect(conn)