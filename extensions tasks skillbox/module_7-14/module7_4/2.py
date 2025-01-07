server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for key, value in server_data.items():
    print(f'{key}:')
    for key_2, value_2 in value.items():
        print(f'  {key_2}: {value_2}')
