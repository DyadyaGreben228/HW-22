#1

#import requests
#import os
#import json
#
## URL для загрузки данных
#url = "https://jsonplaceholder.typicode.com/posts"
#
## Загрузка данных с сайта
#response = requests.get(url)
#posts = response.json()
#
## Создание новой папки для сохранения файлов
#os.makedirs("json_files", exist_ok=True)
#
## Сохранение каждого поста в отдельный файл
#for post in posts:
#    file_name = f"json_files/post_{post['id']}.json"
#    with open(file_name, 'w') as file:
#        json.dump(post, file, indent=4)  # Сохранение данных с отступами для читаемости
#
#print("Все ок")


#2
#import aiohttp
#import asyncio
#import os
#import json
#
#async def fetch_post(session, post_id):
#    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#    async with session.get(url) as response:
#        post = await response.json()
#        file_name = f"json_files_async/post_{post_id}.json"
#        with open(file_name, 'w') as file:
#            json.dump(post, file, indent=4)
#        print(f"Post {post_id} saved.")
#
#async def fetch_all_posts():
#    os.makedirs("json_files_async", exist_ok=True)
#    async with aiohttp.ClientSession() as session:
#        tasks = []
#        for post_id in range(1, 101):
#            task = asyncio.ensure_future(fetch_post(session, post_id))
#            tasks.append(task)
#        await asyncio.gather(*tasks)
#
#
#loop = asyncio.get_event_loop()
#loop.run_until_complete(fetch_all_posts())
#
#print("Все ок")







