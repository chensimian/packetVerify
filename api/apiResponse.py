from django.http import JsonResponse
import json

def is_json(str):
    try:
        json.loads(str)
        return True
    except json.JSONDecodeError:
        return False

class UnifiedResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not any([request.path.startswith('/api/'), request.path.startswith('/controller/')]):
            return self.get_response(request)
        # 如果响应已经是一个JsonResponse，则不进行处理
        # if isinstance(response, JsonResponse):
        #     return response
        # 定义统一的响应格式
        unified_response = {
            'code': response.status_code,
            'message': response.reason_phrase,
            'data': json.loads(response.content.decode('utf-8')) if is_json(response.content.decode('utf-8')) else response.content.decode('utf-8'),
        }
        # 将原始响应替换为统一的JsonResponse
        new_response = JsonResponse(unified_response)
        # 将原始响应的状态码和其他头信息复制到新的JsonResponse中
        new_response.status_code = response.status_code
        for header, value in response.items():
            new_response[header] = value
        # print(unified_response.get('data'))
        return new_response
