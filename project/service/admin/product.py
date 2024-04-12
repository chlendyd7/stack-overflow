import datetime
from django.contrib import admin

from service.models.product import Category, Product, ProductImage

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields=('image','order')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    fieldsets=[
        (
            None, {
            'fields':('name','content','sale_started_at','sale_ended_at','price',),
            }
        ),
        # TODO manytomany admin 추가
        # (
        #     'category',{
        #         'fields':('name',),
        #         'classes': ('collapse',),
        #     }
        # )
    ]
    inlines = [ProductImageInline]


    def delete_model(self, request, obj):
        obj.removed_at = datetime.datetime.now()
        obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude=('removed_at',)
    pass
