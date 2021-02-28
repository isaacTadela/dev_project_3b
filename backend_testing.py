import requests
import pymysql


id, user_name, new_user_name = 85, 'anton', 'mama'

host, port = '127.0.0.1', 5000

    
try:
    res = requests.post(f'http://{host}:{port}/users/{id}', json={"user_name": user_name})
    print("post response for adding user -", res.json())

    res = requests.post(f'http://{host}:{port}/users/{id}', json={"user_name": user_name})
    print("post response for adding added user -", res.json())

    res = requests.get(f'http://{host}:{port}/users/{id}')
    print("get response for anton -", res.json())

    res = requests.get(f'http://{host}:{port}/users/58')
    print("get response for nobady -", res.json())

    res = requests.put(f'http://{host}:{port}/users/{id}', json={"user_name": new_user_name})
    print("put response for anton to mama-", res.json())

    res = requests.put(f'http://{host}:{port}/users/58', json={"user_name": new_user_name})
    print("put response for nobady -", res.json())

    res = requests.delete(f'http://{host}:{port}/users/{id}')
    print("delete response for tony -", res.json())

    res = requests.delete(f'http://{host}:{port}/users/{id}')
    print("delete response for tony second time -", res.json())

except Exception as e:
    print("test failed", e)
    raise Exception(e)
