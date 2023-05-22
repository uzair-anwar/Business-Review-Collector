from django.http import JsonResponse, HttpResponse


def business_endpoint(request):
    if request.method == "GET":
        business_data = {
            'name': 'Example Business',
            'address': '123 Main St',
            'phone': '555-1234'
        }
        return JsonResponse(business_data)
    else:
        return HttpResponse('Method not allowed.', status=405)
