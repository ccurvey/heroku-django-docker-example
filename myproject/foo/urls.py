from django.conf.urls import url

import views

app_name = 'foo'
urlpatterns = (
    url('^testme$', views.testme, name="testme"),
    )
