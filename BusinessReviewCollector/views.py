import requests
from urllib.parse import unquote
from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup


def business_endpoint(request, business_name):
    business_name = unquote(business_name)
    business_url = 'https://www.lendingtree.com/reviews/business/' + business_name

    try:
        if request.method == "GET":
            response = requests.get(business_url)
            if response.status_code == 200:
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                reviews_element = soup.find('span', {'class': 'reviews'})

                business_data = {
                    'name': business_name,
                    'address': reviews_element.text if reviews_element else 'N/A',
                }
                return JsonResponse(business_data)
            else:
                return HttpResponse('Failed to fetch business data.', status=500)

        else:
            return HttpResponse('Method not allowed.', status=405)

    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return HttpResponse(error_message, status=500)
