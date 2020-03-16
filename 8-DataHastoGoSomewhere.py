import csv
villains = [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'], ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld']]

with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

import csv
with open('villains', 'rt') as fin:    # context manager
    cin = csv.reader(fin)
    vallains1 = [row for row in cin]   # This uses a list comprehension
    print(vallains1)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

import csv
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blogeld'},
    ]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print(len(root))
print(len(root[0]))

# JSON(Javascript Object Notation)

menu = \
    {
        "breakfast": {
                "hours": "7-11",
                "items": {
                        "breakfast burritos": "$6.00",
                        "pancakes": "$4.00"
                        }
                    },
        "lunch": {
                "hours": "11-13",
                "items": {
                        "hamburger": "$5.00"
                         }
                },
        "dinner": {
                "hours": "3-10",
                "items": {
                        "spaghetti": "$8.00"
                        }
                }
    }

print(menu)

import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)