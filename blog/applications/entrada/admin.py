from django.contrib import admin
from .models import Entry
from .models import Category
from .models import Tag

# Register your models here.
admin.site.register(Category)
admin.site.register(Entry)
admin.site.register(Tag)

