from django.contrib import admin
from .models import ImageModel


# Register your models here.
@admin.register(ImageModel)
class AdminImages(admin.ModelAdmin):
    Display_List = ['ID', 'Image', 'Date']
