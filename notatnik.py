import requests
from bs4 import BeautifulSoup
import psycopg2

db_params = psycopg2.connect(
    user="postgres", database="postgres", host="localhost", port="5432", password="geoinformatyka"
)


def get_coordinates(nazwa_miejscowosci) -> list:
    url: str = f'https://pl.wikipedia.org/wiki/{nazwa_miejscowosci}'
    response = requests.get(url)
    # print(response)
    # print(response.text)
    response_html = BeautifulSoup(response.text, 'html.parser')

    # print(response_html)
    response_html_lat = response_html.select('.latitude')[1].text.replace(',', '.')
    response_html_lng = response_html.select('.longitude')[1].text.replace(',', '.')
    print(response_html_lat)
    print(response_html_lng)
    return [response_html_lat, response_html_lng]


# get_coordinates()

def create_user(db_params) -> None:
    name: str = input('Enter your name:')
    surname: str = input('Enter your surname:')
    posts: int = int(input('Enter number of your posts:'))
    location: str = input('Enter your location:')
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    longitude, latitude = get_coordinates(location)
    cursor = db_params.cursor()
    sql = f"INSERT   INTO public.users( name, surname, posts, location, coords) VALUES('{name}', '{surname}', {posts}, '{location}', 'SRID=4326;POINT({latitude} {longitude})');"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()


# create_user(db_params)

def read_db(db_params) -> None:
    cursor = db_params.cursor()
    sql = f"SELECT * FROM public.users"
    cursor.execute(sql)
    users = cursor.fetchall()
    cursor.close()
    for user in users:
        print(user)


# read_db(db_params)


def remove_user_db(db_params) -> None:
    cursor = db_params.cursor()
    sql = f"DELETE FROM public.users WHERE name = '{input('Who do you want to delete?')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()


# remove_user_db(db_params)


def update_db(db_params) -> None:
    new_name: str = input('New name:')
    new_surname: str = input('New surname:')
    new_posts: int = int(input('New number of your posts:'))
    new_location: str = input('Enter your new location:')
    longitude, latitude = get_coordinates(new_location)
    cursor = db_params.cursor()
    cursor = db_params.cursor()
    sql = f"UPDATE public.users SET name='{new_name}', surname='{new_surname}', posts='{new_posts}', location='{new_location}', coords='SRID=4326;POINT({latitude} {longitude})' WHERE name = '{input('Who do you want to update?')}';"
    cursor.execute(sql)
    db_params.commit()
    cursor.close()

update_db(db_params)