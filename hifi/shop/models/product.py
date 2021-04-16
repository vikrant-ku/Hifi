from django.db import models
from django_resized import ResizedImageField
from colorfield.fields import ColorField  #pip install django-colorfield
from django.conf import settings
User = settings.AUTH_USER_MODEL


LABEL_CHOICES =(
    ("Sale", "Sale"),
    )

RATING_CHOICES = (
        ('NA', 'New Arrival' ),
        ('BS', 'Best Seller'),
)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/category/')
    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name

class Sub_category_type(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default="")

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    sr_no = models.SlugField(unique=True)
    subcat_type = models.ForeignKey(Sub_category_type, on_delete=models.CASCADE, null=True, blank=True)
    lable = models.CharField(max_length=15, choices=LABEL_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    discount = models.IntegerField(default=0)
    type = models.CharField(max_length=7, choices=RATING_CHOICES, null=True, blank=True)
    description =models.TextField(default="")
    rating = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class product_color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = ColorField(null=True, blank=True)
    image1 = ResizedImageField(size=[700, 900], quality=75, crop=['middle', 'center'], upload_to='media/product/')
    image2 = ResizedImageField(size=[700, 900], quality=75, crop=['middle', 'center'], upload_to='media/product/', null=True, blank=True)
    image3 = ResizedImageField(size=[700, 900], quality=75, crop=['middle', 'center'], upload_to='media/product/', null=True, blank=True)
    image4 = ResizedImageField(size=[700, 900], quality=75, crop=['middle', 'center'], upload_to='media/product/', null=True, blank=True)

    def __str__(self):
        return self.color

class product_size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)

class product_image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = ResizedImageField(size=[700, 900], quality=75, crop=['middle', 'center'], upload_to='media/product/')


# class Cart(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True)  # Non-logged in user can also create a cart
#     products = models.ManyToManyField(Product, blank=True)  # Cart can be blank
#     subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)  # stores the total of cart
#     total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)  # stores the final price
#     updated = models.DateTimeField(auto_now=True)  # Last updated time
#     timestamp = models.DateTimeField(auto_now_add=True)  # Created time



