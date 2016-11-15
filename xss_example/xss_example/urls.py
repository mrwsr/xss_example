from django.conf.urls import url
from xss_example import views

urlpatterns = [
    url(r'^xss/submit', views.xss_submit),
    url(r'^xss/response', views.xss_response),
]
