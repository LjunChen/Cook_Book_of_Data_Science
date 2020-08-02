连接数据库，直接sql语句


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
engine = create_engine("mysql+pymysql://root:KAYLEE@localhost/sven?charset=utf8")
data=pd.read_csv('**')
data.to_sql(name = '**',con = engine,if_exists = 'replace',index = False,index_label = False)
```

    C:\Users\Sven\Anaconda3\envs\study\lib\site-packages\pymysql\cursors.py:170: Warning: (3719, "'utf8' is currently an alias for the character set UTF8MB3, but will be an alias for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.")
      result = self._query(query)
    C:\Users\Sven\Anaconda3\envs\study\lib\site-packages\pymysql\cursors.py:170: Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...' for column 'VARIABLE_VALUE' at row 1")
      result = self._query(query)
    

在Mysql下download数据


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
#data.to_csv('C:/Users/Sven/Desktop/secret.csv',index=False)
```


```python

```
