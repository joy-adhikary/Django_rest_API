# django theke admin ke import korlam karon admin er power diye e kaj korbo amra 
from django.contrib import admin

# models theke kon table er upr kaj korbo oita ke import kore nilam . ( .models dilam karon models ak repotei roise )
from .models import Joy
from .models import Joy1

# admin.site.register mane hocche ami django admin dashboard tehke ei table take manage korte parbo like crud oparetin korty parbo .
admin.site.register(Joy)

admin.site.register(Joy1)