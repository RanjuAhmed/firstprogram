import requests
"""Get সার্ভার থেকে data আনার জন্য ব্যবহার হয়।"""
# url="https://www.google.com/"
# l=requests.get(url)
# # print(l.text)
# # print(l.status_code)#200 আসলেই success
# # print(l.json())
"""Post সার্ভারে নতুন data পাঠানোর জন্য ব্যবহার হয়।"""
# data = {"title": "My Post", "body": "Hello World", "userId": 1}
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# print(response.status_code)   # সাধারণত 201 = Created
# print(response.json())        # সার্ভার কি রিটার্ন করলো

"""Put সার্ভারে থাকা data পুরোপুরি আপডেট করার জন্য। """
# update = {"title": "Updated Title", "body": "Updated Body"}
# response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update)

# print(response.json())
 
"""Delete সার্ভার থেকে data মুছে ফেলার জন্য।"""
# response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)   # সাধারণত 200 বা 204
