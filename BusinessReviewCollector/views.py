import datetime
import requests
from urllib.parse import unquote
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from .models import Review


@csrf_exempt
def business_endpoint(request, business_url):
    business_url = unquote(business_url)
    try:
        if request.method == "GET":
            response = requests.get(business_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                reviews = soup.find_all('div', class_='mainReviews')
                reviews_data = []

                for review in reviews:
                    review_title = review.find('p', class_="reviewTitle").text
                    review_content = review.find('p', class_="reviewText").text
                    review_auther = review.find(
                        'p', class_="consumerName").text.strip()
                    review_auther = " ".join(review_auther.split())
                    review_date = review.find(
                        'p', class_="consumerReviewDate").text
                    date = datetime.datetime.strptime(
                        review_date, "Reviewed in %B %Y").date()
                    review_star = review.find(
                        'div', class_="numRec").text.strip()
                    review_star = " ".join(review_star.split())[1]
                    reviews_data.append({
                        "title": review_title,
                        "content": review_content,
                        "consumerName": review_auther,
                        "date": date,
                        "star": review_star
                    })
                    review_obj = Review(
                        title=review_title,
                        content=review_content,
                        auther=review_auther,
                        date=date,
                        stars=float(review_star)
                    )
                    review_obj.save()

                return JsonResponse(reviews_data, safe=False, status=200)
            else:
                return HttpResponse('Failed to retrieve data from the business URL.', status=403)
        else:
            return HttpResponse('Invalid request method.', status=400)
    except requests.exceptions.RequestException as e:
        error_message = f'An error occurred while making the request: {str(e)}'
        return HttpResponse(error_message, status=500)
    except (ValueError, KeyError) as e:
        error_message = f'An error occurred while parsing the data: {str(e)}'
        return HttpResponse(error_message, status=500)
    except Exception as e:
        error_message = f'An error occurred: {str(e)}'
        return HttpResponse(error_message, status=500)
