import time
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('drf')

class RequestDateMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):

        if hasattr(request, 'start_time'):
            date_time = time.time() - request.start_time
            # 获取request的参数

            log_data = {
                'path': request.path,
                'method': request.method,
                'params': dict(request.GET),
                'data': dict(request.POST),
                'time': f'{date_time:.3f}s'
            }
            logger.info(f'API Request: {log_data}')

        return response

