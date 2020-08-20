from starlette.routing import Route

import views


routes = [
    Route('/hello_world', views.HelloWoldView, methods=['GET']),
    Route('/proxies/{numProxies}', views.GetProxiesView, methods=['GET']),
    Route('/fetch/{maxAgeDays}/{category}/{output}/{method}', views.FetchURLView, methods=['POST']),
]
