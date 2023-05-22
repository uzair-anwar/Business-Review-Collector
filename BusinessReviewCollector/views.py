import requests
from urllib.parse import unquote
from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup


def business_endpoint(request, business_name):
    business_name = unquote(business_name)
    print(business_name)
    business_url = f'https://www.lendingtree.com/reviews/business/{business_name}'

    try:
        if request.method == "GET":
            response = requests.get(business_url)
            if response.status_code == 200:
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                reviews_element = soup.find('span', {'class': 'reviews'})
                reviews = reviews_element.text.strip() if reviews_element else 'N/A'
                business_data = {
                    'name': business_name,
                    'reviews': reviews,
                }
                return JsonResponse(business_data)
            else:
                rerror_message = 'An error occurred.'
                return HttpResponse(error_message, status=500)

        else:
            return HttpResponse('Method not allowed.', status=405)

    except Exception as e:
        error_message = 'An error occurred.'
        return HttpResponse(error_message, status=500)
