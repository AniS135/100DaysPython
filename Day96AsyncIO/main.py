import time
import asyncio
import requests

async def function1():
    print("func 1")
    URL = "https://images.unsplash.com/photo-1549740425-5e9ed4d8cd34?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    response = requests.get(URL)
    open("Day96AsyncIO\instagram1.jpg", "wb").write(response.content)
    

async def function2():
    print("func 2")
    URL = "https://images.unsplash.com/photo-1549740425-5e9ed4d8cd34?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    response = requests.get(URL)
    open("Day96AsyncIO\instagram2.jpg", "wb").write(response.content)
    

async def function3():
    print("func 3")
    URL = "https://images.unsplash.com/photo-1549740425-5e9ed4d8cd34?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    response = requests.get(URL)
    open("Day96AsyncIO\instagram3.jpg", "wb").write(response.content)
    

async def main():
    # task = asyncio.create_task(function1())
    await function1()
    await function2()
    await function3()
    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3())
    # print(L)

asyncio.run(main())