#!/usr/bin/env python
# coding: utf-8

import requests


headers={'Content-type': 'application/json; charset=UTF-8',}
data={'title': 'foo', 'body': 'bar', 'userId': 1}

#API post call
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data, headers=headers)

if response.status_code in [200, 201]:
    print("post call success")
    print(f"response: {response.json()}")
else:
    print("post call not success")


headers={'Content-type': 'application/json; charset=UTF-8',}
data={"id":1, 'title': 'foo', 'body': 'bar', 'userId': 1}

#API put call
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=data, headers=headers)

if response.status_code in [200, 201]:
    print("put call success")
    print(f"response: {response.json()}")
else:
    print("put call not success")


#API delete call
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code in [200, 201]:
    print("delete call success")
else:
    print("delete call not success")

#API get call
response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code in [200, 201]:
    print("get call success")
    print(f"response: {response.json()}")
else:
    print("get call not success")


#API get call
response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")

if response.status_code in [200, 201]:
    print("get call success")
    print(f"response: {response.json()}")
else:
    print("get call not success")

#API get call
response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")

if response.status_code in [200, 201]:
    print("get call success")
    print(f"response: {response.json()}")
else:
    print("get call not success")


#API get call
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code in [200, 201]:
    print("get call success")
    print(f"response: {response.json()}")
else:
    print("get call not success")

import threading
import requests

#load testing
def load_test(thread_number, url, http_method, payload=None, headers=None):
    
    if http_method == "get":
        
        response = requests.get(url)

        if response.status_code in [200, 201]:
            print("get call success")
            print(f"response: {response.json()}")
        else:
            print("get call not success")
    
    elif http_method == "post":
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            print("post call success")
            print(f"response: {response.json()}")
        else:
            print("post call not success")
        
    elif http_method == "put":
        
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            print("put call success")
            print(f"response: {response.json()}")
        else:
            print("put call not success")
            
    elif http_method == "delete":
        
        response = requests.delete(url)
        
        if response.status_code in [200, 201]:
            print("delete call success")
            print(f"response: {response.json()}")
        else:
            print("delete call not success")
    
    print(f"Thread number: {thread_number}")

    return
          
threads = []
number_users = 10
          
url = "https://jsonplaceholder.typicode.com/posts"
http_method = "post"
payload = {'title': 'foo', 'body': 'bar', 'userId': 1}
headers = {'Content-type': 'application/json; charset=UTF-8',}

for i in range(number_users):
    t = threading.Thread(target=load_test, args=(i,url,http_method,payload,headers))
    threads.append(t)
    t.start()
