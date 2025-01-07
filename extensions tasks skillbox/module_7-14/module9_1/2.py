import os


def print_path(path_inp):
    print(f'Содержимое директории {path_inp}: ')
    #print(os.listdir(path_inp))
    for elem in os.listdir(path_inp):
        path = os.path.join(path_inp, elem)
        print('     ', path)


name_folder = 'training'

path_for = os.path.abspath(os.path.join('..', '..', '..', '..', name_folder))
#print(path_for)
print_path(path_for)
