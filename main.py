from BelHard57.schemas import CategorySchema, UserSchema, ArticleSchema
from crud import CRUDCategory, CRUDUser, CRUDArticle
category = CRUDCategory.get(category_id=1)
print(category)
# category.parent_id = None
# print(CRUDCategory.get(category_id=1))
# CRUDUser.add(user=UserSchema(username='Tim', hashed_password='jkjhkjkj34jkjkljk31413412', email="tatayt@gmail.com"))
user = CRUDUser.get(user_id=7)
print(user)
CRUDArticle.add(article=ArticleSchema(category_id=1, title='Timka', body='jkjhkjkj34jkjkljk31413412', author_id=7))
article = CRUDArticle.get_all
print(article)
