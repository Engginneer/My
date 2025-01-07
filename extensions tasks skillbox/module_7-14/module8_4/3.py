def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    elif isinstance(data, (int, float, str)):
        template = template or dict()
        template[data] = data
        return template



def data_preparation(old_list):
    new_list = []

    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)
    return new_list


data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
data_new = data_preparation(data)
print(data)
print(data_new)
