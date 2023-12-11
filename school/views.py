from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from base.common.engine import get_request_data
from school.Backend.search_engine import Search


class SchoolEndpoints(object):
    @csrf_exempt
    def search_user(self, request):
        try:
            data = get_request_data(request)
            return JsonResponse(Search().search_bar(request=request, **data), safe=False)

        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "999.999.999"})


