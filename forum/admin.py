from django.contrib import admin

from .models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    pass

# @admin.register(UselessModel)
# class UselessAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Model2)
# class Model2Admin(admin.ModelAdmin):
#     pass

# @admin.register(Model3)
# class Model3Admin(admin.ModelAdmin):
#     pass
