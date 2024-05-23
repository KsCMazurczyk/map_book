# name: str = input("Enter your name: ")
# print(f'WITAJ {name}')

data_of_users: list = [
    {'name': 'Julia', 'Surname': 'Szklarzi', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Norbi', 'Surname': 'Szeli', 'posts': 3, 'location': 'Rzeszów'},
    {'name': 'Kacper', 'Surname': 'Chujcik', 'posts': 0, 'location': 'Legnica'},
    {'name': 'Seba', 'Surname': 'Dudek', 'posts': 10, 'location': 'Siedlce'},
]
print(f'Witaj {data_of_users[0]['name']}')
def read(users: list)->None:
    """
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'Twój Znajomy: {user['name']}, opublikował: {user["posts"]} postów')
read(data_of_users)