## Python 与 MySQL的交互



连接数据库，执行sql语句


```python
import pymysql
db=pymysql.connect('localhost','root','**','**')
##ip,user,secret,database
cursor=db.cursor()

sql="""insert into secret(Web,
        username, secret, mail)
     values ('**','**','**','')"""
###执行sql语句，添加数据等
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()

```

将本地数据存储在mysql


```python
import pandas as pd
import pymysql
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://usrname:secret@ip/database_name?charset=utf8")
data=pd.read_csv('**')
data.to_sql(name = '**',con = engine,if_exists = 'replace',index = False,index_label = False)
```

将Mysql下download到本地


```python
import pandas as pd
import pymysql
dbconn=pymysql.connect(
  host="localhost",
  database="sven",
  user="**",
  password="**",
  port=3306,
  charset='utf8'
 )
sqlcmd='select * from secret'
data=pd.read_sql(sqlcmd,dbconn)
data.to_csv('',index=False)
```

