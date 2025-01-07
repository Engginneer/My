
object_input = [100, 200, 300, 'буква', 0, 2, 'а']

list_output = []
for index, char in enumerate(object_input):
    if index % 2 == 0:
        list_output.append(char)

print(list_output)