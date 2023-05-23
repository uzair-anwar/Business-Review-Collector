import requests
from urllib.parse import unquote
from django.http import JsonResponse, HttpResponse
from bs4 import BeautifulSoup


def business_endpoint(request, business_name):
    business_name = unquote(business_name)
    try:
        if request.method == "GET":
            response = requests.get(business_name)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                reviews = soup.find_all('div', class_='mainReviews')
                reviews_data = []

                for review in reviews:
                    review_title = review.find('p', class_="reviewTitle").text
                    review_content = review.find('p', class_="reviewText").text
                    review_consumerName = review.find(
                        'p', class_="consumerName").text.strip()
                    review_consumerName = " ".join(review_consumerName.split())
                    review_date = review.find(
                        'p', class_="consumerReviewDate").text
                    review_star = review.find(
                        'div', class_="numRec").text.strip()
                    review_star = " ".join(review_star.split())[1]
                    reviews_data.append({
                        "title": review_title,
                        "content": review_content,
                        "consumerName": review_consumerName,
                        "date": review_date,
                        "star": review_star
                    })

                return JsonResponse(reviews_data, safe=False)
        else:
            return HttpResponse('Method not allowed.', status=405)

    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return HttpResponse(error_message, status=500)
