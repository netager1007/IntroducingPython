def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value=%s, name=%s, value2=%s' %(value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')


import unicodedata
name = unicodedata.name('\u00e9')
value2 = unicodedata.lookup(name)
value3 = unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')
place = 'caf\u00e9'
print(len('$'))
print('len unicode: ', len('\u0001f47b'))
print(place)
print(value2)
print(value3)

name1= unicodedata.name('\u2603')
print(name1)

snowman = '\u2603'
print(len(snowman))
print(snowman)
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)

ds1 = snowman.encode('ascii', 'ignore')
print(len(ds1))
print(ds1)

ds2 = snowman.encode('ascii', 'replace')
print(len(ds2))
print(ds2)

ds3 = snowman.encode('ascii', 'backslashreplace')
print(len(ds3))
print(ds3)

ds4 = snowman.encode('ascii', 'xmlcharrefreplace')
print(len(ds4))
print(ds4)



# 디코딩(decoding)

place = 'caf\u00e9'
place_bytes = place.encode('utf-8')
print('place_types: ', place_bytes)
print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
print(place2)

#place3 = place_bytes.decode('ascii')
#print(place3)

place4 = place_bytes.decode('latin-1')
print(place4)

