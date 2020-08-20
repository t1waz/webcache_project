from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse


class FetchURLView(HTTPEndpoint):
    """"
    endpoint documentation
    """
    @staticmethod
    async def validate_request_params(request_params):
        pass

    async def get(self, request):
        pass


class GetProxiesView(HTTPEndpoint):
    """"
    endpoint documentation
    """
    @staticmethod
    async def validate_request_params(request_params):
        pass

    async def get(self, request):
        pass


class HelloWoldView(HTTPEndpoint):
    """"
    just simple endpoint to check if service is alive
    using curl or something.
    """
    async def get(self, request):
        return JSONResponse({'hello': 'world'})
