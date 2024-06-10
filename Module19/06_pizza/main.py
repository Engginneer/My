# TODO я тут использовал default_dict вместо dict, если хочешь, почитай про него и используй, чаще всего использую его, он очень удобный

from collections import defaultdict
from pprint import pprint

my_dict = defaultdict(int)

print(my_dict['жопа'])

my_dict['crackers'] += 100
my_dict['something'] = 'Hello'

pprint(dict(my_dict))  # Pretty print не любит кастомные словари
