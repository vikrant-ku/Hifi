from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models.product import Category, Subcategory, Sub_category_type, Product, product_size, product_color,product_image
from .models.contact import Contact_Us, Subscribers
from .models.user import Profile, Billing


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SubcatAdmin(admin.ModelAdmin):
    list_display = ( 'name','category')
    list_filter = ('name','category', )
    search_fields = ('name','category__name',)
    prepopulated_fields = {'slug': ('category','name')}

class Subcat_Type_Admin(admin.ModelAdmin):
    list_display = ( 'name','subcategory')
    list_filter = ('name','subcategory', )
    search_fields = ('name','subcategory__name',)
    prepopulated_fields = {'slug': ('subcategory', 'name')}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory','subcat_type')
    list_filter = ('category', 'subcategory','subcat_type')
    search_fields = ('name','category__name', 'subcategory__name', 'sr_no', 'subcat_type')
    # list_editable = ('lable', 'type')

class product_colorAdmin(admin.ModelAdmin):
    search_fields = ('product__sr_no', 'product__name')

class Product_sizeAdmin(admin.ModelAdmin):
    list_display = ('product','size')




admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcatAdmin)
admin.site.register(Sub_category_type, Subcat_Type_Admin)
admin.site.register(Product,ProductAdmin)
admin.site.register(product_image)
admin.site.register(product_color,product_colorAdmin)
admin.site.register(product_size, Product_sizeAdmin)
admin.site.register(Profile)
admin.site.register(Billing)
admin.site.register(Contact_Us)
admin.site.register(Subscribers)