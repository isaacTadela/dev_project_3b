import requests
import pymysql


id, user_name = 5, "dan5"
host, remotemysql, port, sqlPort, user, passwd, db = '127.0.0.1', 'remotemysql.com', 5000, 3306, '9hkyb0ebUg', 'Q9XsNQ9fQw', '9hkyb0ebUg'

try:
    res = requests.post(f'http://{host}:{port}/users/{id}', json={"user_name": f'{user_name}'})
    print("post response -", res.json())

    res = requests.get(f'http://{host}:{port}/users/{id}')
    print("get response -", res.json())
    
    # Establishing a connection to DB 
    conn = pymysql.connect(host=remotemysql, port=sqlPort, user=user, passwd=passwd, db=db,
            cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM {db}.users WHERE user_id = {id};")
    data = cursor.fetchall()
    user_name = data[0]['user_name']
    print("DB response -", user_name)
except IndexError as ie:
    print("DB response - No such id", ie)
except pymysql.err.IntegrityError as ie:
    print("DB response - Duplicate entry for PRIMARY key",ie)        
except ( RuntimeError, pymysql.err.OperationalError ) as oe:
    print("DB error - Can't connect to MySQL server", oe)
    raise Exception(oe)
except Exception as e:
    print("test failed",e)
    raise Exception(e)