from .jsonrpc import JsonRpc, publicmethod
from django.urls import reverse_lazy
from django.http.response import HttpResponse


class UserRpcMethods:
    url = reverse_lazy("api-rpc")

    @publicmethod
    def add(x, y):
        return x + y

    @publicmethod
    def sub(x, y):
        return x - y

    @publicmethod
    def sayHello(*args):
        return "hello "


def user_rpc_view(request):
    rpc = JsonRpc(UserRpcMethods())
    response = rpc.handle_request(request)

    return HttpResponse(response.json, mimetype='application/json')
