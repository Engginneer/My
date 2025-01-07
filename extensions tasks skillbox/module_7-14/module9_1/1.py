import os

name_file = 'admin.bat'

print(f'Абсолютный путь к папке: {os.path.abspath(os.path.join('Skillbox', 'access', name_file))}')
print(f'Относительный путь к папке: {os.path.join('Skillbox', 'access', name_file)}')
