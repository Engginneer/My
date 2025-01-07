input_obj = {1: 3}


if isinstance(input_obj, float):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "float", его айди: {id(input_obj)}')
elif isinstance(input_obj, str):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "str", его айди: {id(input_obj)}')
elif isinstance(input_obj, tuple):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "tuple", его айди: {id(input_obj)}')
elif isinstance(input_obj, bool):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "bool", его айди: {id(input_obj)}')
elif isinstance(input_obj, list):
    print(f'Объект "{input_obj}" - является объектом изменяемым типа "list", его айди: {id(input_obj)}')
elif isinstance(input_obj, int):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "int", его айди: {id(input_obj)}')
elif isinstance(input_obj, dict):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "dict", его айди: {id(input_obj)}')
elif isinstance(input_obj, set):
    print(f'Объект "{input_obj}" - является объектом неизменяемым типа "set", его айди: {id(input_obj)}')
