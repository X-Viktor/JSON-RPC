from django.conf.urls import url

from .views import user_rpc_view

urlpatterns = [
    url('', user_rpc_view, name='api-rpc'),
]
