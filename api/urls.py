from django.conf.urls import url
from modernrpc.views import RPCEntryPoint

urlpatterns = [
    url('', RPCEntryPoint.as_view()),
]
