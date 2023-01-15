
from django.contrib import admin
from django.urls import path
from restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all',views.Items),
    path('item/<int:id>',views.item)
]




# jodi brower theke json format a data dekhty cai tahole ei ta use korte pari . just sdu function like all,item er majhe format=none kore dite hobe 
# urlpatterns = format_suffix_patterns(urlpatterns)
# api er format tkn hbe amn : http://127.0.0.1:8000/item/2.json