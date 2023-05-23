# Business Review Web Service

This is a Python-based web service that collects reviews from business URLs. It utilizes the LendingTree website
(https://www.lendingtree.com/reviews/business) to extract review data. The service accepts requests with business URLs
and retrieves information such as the review title, content, author, star rating, date of review, and any other relevant details.

## Installation

To use this web service, follow these steps:

#### Clone the repository:

    git clone https://github.com/uzair-anwar/Business-Review-Collector.git

#### Navigate to the project directory:


    cd Business-Review-Collector

#### Install the required dependencies:

    pip install -r requirements.txt

#### Create Database and table:

     python3 manage.py makemigration
     python3 manage.py migrate

## Usage

 * To get reviews for a business, use the following request:

       GET http://localhost:8000/business/<business_url>

 * For example, to get reviews for OnDeck, you would use the following request:

       GET https://localhost:8000/reviews/business/https://www.lendingtree.com/reviews/business/ondeck/51886298


 * The response will be a JSON object with the following properties:

  * `reviews`: A list of reviews. Each review has the following properties:
      * `title`: The title of the review.
      * `content`: The content of the review.
      * `author`: The author of the review.
      * `star_rating`: The star rating of the review.
      * `date_of_review`: The date of the review.

## Error handling

The following errors may occur:

* `400 Bad Request`: The request was malformed.
* `404 Not Found`: The business URL was not found.
* `500 Internal Server Error`: An unexpected error occurred.

## Testing

To run the tests, use the following command:

    python3 manage.py test

## Database
   * SQlite

## License

This API is licensed under the MIT License.
