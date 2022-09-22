from crud import CRUDCategory
import asyncio
from schemas import CategorySchema
from requests import Session
from aiohttp import ClientSession
# category = CRUDCategory.get(category_id=1)
# print(category)
# category.parent_id = None
# CRUDCategory.update(category=category)
# print(CRUDCategory.get(category_id=1))
# CRUDUser.add(user=UserSchema(username='Tim', hashed_password='jkjhkjkj34jkjkljk31413412', email="tatayt@gmail.com"))
# user = CRUDUser.get(user_id=7)
# print(user)
# CRUDArticle.add(article=ArticleSchema(category_id=1, title='Timka', body='jkjhkjkj34jkjkljk31413412', author_id=7))
# article = CRUDArticle.get_all
# print(article)


# async def foo():
#     res = await CRUDCategory.get_all()
# #     # category = await CRUDCategory.get(category_id=1)
# #     # category.parent_id = None
# #     # await CRUDCategory.update(category=category)
#     print(res)

# asyncio.run(foo())
# category = CRUDCategory.get(category_id=2)
# category.parent_id = 2
# print(category)
# CRUDCategory.update(category=category)
# CRUDCategory.add(category=CategorySchema(name='Junk', parent_id=3))
# print(CRUDCategory.get_all())

def get_response():
    with Session() as session:
        response = session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
            # params={
            #     "params_name": "value"
            # }
            # headers={
            #     "Accept-Language": "ru",
            # }
            # json={}
        )
        # print(response.json)
        print(response.text.split('sellIso'), sep='         ')
        # print(response.headers)
        # print(response.url)
        # print(response.status_code)


async def a_get_response():
    async with ClientSession() as session:
        response = await session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
            # params={
            #     "params_name": "value"
            # }
            # headers={
            #     "Accept-Language": "ru",
            # }
            # json={}
        )
        # print(response.json)
        # print(response.text)
        # print(response.headers)
        # print(response.url)
        await asyncio.sleep(3)
        print(response.status)


async def main_():
    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(a_get_response()) for _ in range(10)]
    for task in tasks:
        await task

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main_())
get_response()
