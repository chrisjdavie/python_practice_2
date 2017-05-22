
from itertools import groupby

for k, g in groupby('AAAABBBCCDAABBB'):
    print(k, list(g))

print()

for k, g in groupby('AaaABbBccdAabBB', key=lambda x: x.lower()):
    print(k, list(g))

beers = [ { 'name': 'hobgoblin', 'type': 'Ale' },
          { 'name': 'blacksheep', 'type': 'Ale' },
          { 'name': 'bud', 'type': 'larger' },
          { 'name': 'aspel', 'type': 'cider' },
          { 'name': 'corona', 'type': 'larger' },
          { 'name': 'IPA', 'type': 'Ale' } ]

for k, g in groupby(beers, key = lambda x: x['type']):
    print(k, list(g))

