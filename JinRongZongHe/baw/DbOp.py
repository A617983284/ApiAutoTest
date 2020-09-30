'''
跟业务相关的数据库操作
'''
from JinRongZongHe.caw.Mysql import Mysql

class DbOp:
    def delete_user(self,db,mobilephone):
        mysql=Mysql()
        # db={"ip":"192.168.150.52","post":"3306","name":"apple","user":"root","pwd":"123456"}
        conn=Mysql().connect(db)
        print(conn)
        Mysql().execute(conn,f"delete from member where mobilephone={mobilephone};")
        Mysql().disconnect(conn)