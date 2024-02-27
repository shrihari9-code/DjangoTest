from django.contrib import admin
from products.models import Product, Sku

class SkuInline(admin.StackedInline):
    model = Sku
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "managed_by", "edited_at")
    ordering = ("-id",)
    search_fields = ("name",)
    list_filter = ("is_refrigerated", "category")
    fields = (
        ("name", "price"),
        ("category", "is_refrigerated"),
        "description",
        "ingredients",
        ("id", "created_at", "edited_at"),
        "managed_by",
    )
    autocomplete_fields = ("category", "managed_by")
    readonly_fields = ("id", "created_at", "edited_at")
    inlines = (SkuInline,)

class ProductInline(admin.StackedInline):
    model = Product
    extra = 0
    ordering = ("-id",)
    readonly_fields = ("name", "price", "is_refrigerated")
    fields = (readonly_fields,)
    show_change_link = True
    
@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'measurement_unit', 'selling_price', 'platform_commission', 'cost_price', 'status', 'markup_percentage')
    list_filter = ('status',)
    search_fields = ('product__name',)



