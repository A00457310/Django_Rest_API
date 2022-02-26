#Assignment Rest api using python and django framework
--------
Set Up
--------
Install below library..

1. $ pip install django
2. $ pip install django_rest_framework
3. $ pip install pymysql



-----------------------
Application end points
-----------------------
This application uses Django framework for developing the resp api for getting and creating the entries in the hotel details tables.
Sample object for hotel 
{
	"id": int,
	"hotel_name": string,
	"address": string,
	"rating": string,
	"capacity": string
}
Function bases views 
1. GET:  http://127.0.0.1:8000/app/hotels/ To get the list of hotels saved in the database table.
2. POST:  http://127.0.0.1:8000/app/hotels/  To save the hotel object in db.
3. GET : http://127.0.0.1:8000/app/hotels/{id} To get the detail of a particular hotel by using primary key  id.
4. PUT:  http://127.0.0.1:8000/app/hotels/{id} To update the hotel details with hotel id and request body as hotel object.
5. DELETE :   http://127.0.0.1:8000/app/hotels/{id} To delete the hotel from the database.
