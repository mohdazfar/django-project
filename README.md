USAGE:
I have used POSTMAN to validate my GET and POST requests.

Task - Part 1: Accept a REST request which contains fields described below, validates them (type, content,
etc.), and then saves the data to database. Application must return an identifier for the newly
created cart as a response.

POST /products
{
"item_id" : "101600511",
"item_price" : 155.00,
"item_name": "GARMIN FORERUNNER 15 HRM SI/MU JUOKSUKEL",
"manufacturing_country_id": "7"
}

Task - Part 2: Accept a REST request which contains the identifier field, fetches the cart content from
database with it, and returns the cart content as a response.

GET /products?id={ID}
GET /products?id={Item_ID}
