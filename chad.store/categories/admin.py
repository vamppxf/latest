from django.contrib import admin
from categories.models import Category, CategoryImage

admin.site.register(CategoryImage)

class CategoryImageInLine(admin.StackedInline):
    model = CategoryImage
    extra = 0 

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInLine]

