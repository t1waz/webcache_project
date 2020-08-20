import asyncio

import aiohttp

import settings
from common.common import RequestData
from collections import namedtuple


class MongoDBService:
    pass


class RequestService:
    RESPONSE_DATA = namedtuple('ResponseData', ('request_data', 'response', 'error'))
    SEMAPHORE_VALUE = 1000
    SESSION_TIMEOUT = aiohttp.ClientTimeout(total=settings.SESSION_TIMEOUT)

    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self._q = asyncio.Semaphore(self.SEMAPHORE_VALUE)

    @staticmethod
    def validate_request_data(request_data):
        if not isinstance(request_data, RequestData):
            return False

        return True

    async def handle_request(self, request_data, session):
        if not self.validate_request_data(request_data):
            return None

        response_data = {
            'request_data': request_data,
            'response': None,
            'error': None,
        }
        method_to_call = getattr(session, request_data.method, None)
        try:
            async with self._q as q, method_to_call(
                    **request_data.session_call_arguments) as response:
                response_data['response'] = response
        except Exception as e:
            response_data['error'] = e

        return self.RESPONSE_DATA(**response_data)

    @classmethod
    async def handle_request_datas(cls, request_datas):
        service = cls()
        async with aiohttp.ClientSession(timeout=cls.SESSION_TIMEOUT) as session:
            return await asyncio.gather(*[
                asyncio.ensure_future(service.handle_request(session=session,
                                                             request_data=request_data))
                for request_data in request_datas])

# for testing, REMOVE IN FUTURE
# loop = asyncio.get_event_loop()
# data = RequestData(url='http://google.com', method='get', headers={}, payload={})
# print(loop.run_until_complete(RequestService.handle_request_datas(request_datas=[data, data])))
