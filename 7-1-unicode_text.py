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

# 포맷 : format
print('%s' % 42)
print('%d' % 42)

n = 42
f = 7.03
s = 'string'
s1 = 'string cheese'

print('%d %f %s %s' % (n, f, s, s1))
print('%10d %10f %10s %10s' % (n, f, s, s1))
print('%-10d %-10f %-10s %-10s' % (n, f, s, s1))
print('%.4d %.4f %.4s %.4s' % (n, f, s, s1))
print('%*.*d %*.*f %*.*s %*.*s' % (10,4,n, 10, 4, f, 10, 4, s, 10, 4, s1))

print('first: {} {} {}'.format(n,f,s))
print('secode: {2} {0} {1}'.format(n,f,s))
d = {'n':42, 'f':4.03, 's':'string cheese'}
print('third: {0[n]} {0[f]} {0[s]}'.format(d, 'other'))

print('{0:d} {1:f} {2:s}'.format(n, f, s))
print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))
print('{2:>10s} {0:>10d} {1:>10f}'.format(n, f, s))
print('{:>10d} {:>10f} {:>10s}'.format(n, f, s))

print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))
print('{0:^20s}'.format('Big Sale'))
