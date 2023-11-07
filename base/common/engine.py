import json

from django.http import QueryDict


class RequestEngine(object):
    @staticmethod
    def get_request_data(request):
        try:
            data = None
            if request:
                request_meta = getattr(request, 'META', None)
                request_method = getattr(request, 'method', None)
                if request_meta.get('CONTENT_TYPE') == 'application/json':
                    data = json.loads(request.body).copy()
                if request_meta.get('CONTENT_TYPE').startswith("multipart/form-data"):
                    data = request.POST.copy()
                elif request_method == 'GET':
                    data = request.GET().copy()
                    data = data.dict()
                elif request_method == 'POST':
                    data = request.POST.copy()
                    data = data.dict()

                if not data:
                    request_body = getattr(request, 'body', None)
                    if request_body:
                        data = json.load(request_body)
                    else:
                        data = QueryDict

            return data
        except Exception as e:
            print(e)
            return {'code': '100.000.010', 'message': 'Error while processing request'}
