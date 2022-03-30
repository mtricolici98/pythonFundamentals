# Project Ideas

The method of interaction with the service should be through the internet, so you can use a Web API (using flask), or if
you want, you can create a bot in a chat application.

The project ideas in this list should act as guidelines, you should feel free to add any other functionality you think
is necessary.

# Email Service [HARD]

## Description

Create an email subscription web service that will allow a user (customer) to create mailing lists, and send emails.

## Tools necessary

* Sending [emails](https://realpython.com/python-send-email/)
* Database connection and working with users. [Look here](/lessons/lesson_21)
  and [here](https://medium.com/@anubabajide/rest-api-authentication-in-flask-481518a7479b)
* [Flask APIs](lessons/lesson_18)
  also [here](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask)

## Functionality

### As a user I would like to be able to

* register as a customer
* login as a customer
* create a mailing list as a customer
* add a subscriber to the mailing list
* send message to the entire mailing list
* remove subscribers from the mailing list
* list all his mailing lists
* list all users for his mailing list

## Example:

Customer Tekwill creates a mailing list called &quot;Python Fundamentals students&quot;.

Customer adds some users to the mailing list

Customer sends request to send a message to all in the &quot;Python Fundamentals students&quot; mailing list

All users registered in the &quot;Python Fundamentals students&quot; list receive an email message

# Currency Conversion Service [MEDIUM]

## Description

Create a web service that would allow users to calculate exchange rates for currencies

Use an existing data source (for example an existing API) to get all the conversion rates.

The service should provide the following functionality:

- Get list of currencies available
- Get rate from currency -> to currency
- Convert amount from currency -> to currency
- Get rate delta from day to day for conversion rate
    - Rate delta is rate today - rate yesterday
    - From currency -> To currency
- Get list of previous conversions made by the user

# Weather Service [EASY]

Create a web service to get current and forecast weather data. The service should not use any authentication (so no user
is involved). The service should however store information about the requests.

The service should provide the following functionality:

- Get current weather for location
- Get forecast weather for location

If the user requests weather data without a location (without a City/Country), the service should try to identify the
location from the user IP

The service should also log the request, and keep a record for:

- Which IP the request came from, and what was the request body

The service should also check the following:

- If more than 5 requests came from the same IP in the span of 1 minute, the service should automatically decline any
  request and return an error

Example endpoints:

[GET] /forecast

[GET] /weather

Where **location** is an optional query argument. If the query argument is not present, identify by IP.

Convert this service into a bot on whatever platform you want.
