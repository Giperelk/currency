from time import time
from currency.models import RequestResponseLog
from currency.choices import RateRequestResponseLogChoices


class RequestResponseLogTimeMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        start = time()
        response = self.get_response(request)
        end = time()
        milliseconds = int((end - start)*1000)
        method = RateRequestResponseLogChoices.__dict__[f'{request.method}']
        rrl = RequestResponseLog(path=request.path, request_method=method, time=milliseconds)
        rrl.save()

        return response
