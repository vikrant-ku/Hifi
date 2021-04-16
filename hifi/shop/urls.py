from django.urls import path
from .views import index, contact_us, store, register_user, login, Logout,Product_view, temp, cart, profile, billing, Change_password, delete_billing, edit_billing

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact_us, name="contact_us"),
    path('store', store, name="store"),
    path('cart', cart, name="cart"),
    path('profile', profile, name="profile"),
    path('profile/addresses',billing, name="addresses"),
    path('profile/addresses/delete/<int:pk>', delete_billing, name="delete_addresses"),
    path('profile/addresses/edit/<int:pk>', edit_billing, name="edit_addresses"),
    path('temp', temp, name="temp"),
    path('product-view',Product_view, name="product_view"),
    path('signup', register_user, name="register_user"),
    path('login', login, name="login"),
    path('logout',Logout , name="logout"),
    path('profile/change-password', Change_password, name="Change_password"),

]