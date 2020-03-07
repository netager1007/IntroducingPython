# Unicode
# -------
# 유니코드 식별자(ID) 혹은 문자에 대한 이름(name)을 안다면, 이문자를 파이썬 문자열에
# 사용할 수 있다.
# - 4자리 16진수와 그 앞에 \u는 유니코드의 기본 평면 256개 중 하나의 문자를 지정한다.
#   첫 번째 두 숫자는 평면 번호다(00에서 FF까지). 평면 00은 아스키코드고, 평면 안의
#   문자 위치는 아스키코드의 번호와 같다
# - 높은 평면의 문자일수록 비트수가 더 필요하다. 파이썬의 이스케이프 시퀀스는 \U고,
#   8자리의 16진수를 사용한다. 숫자에 남는 공간이 있다면 왼쪽에 0을 채운다.
# - 모든 문자는 표준 이름 \N{name}으로 지정할 수 있다. 유니코드 문자 이름 인덱스
#   (The Unicode Character Names Index)페이지에서 표준 이름 리스트를 참조
# - lookup() : 대/소문자를 구분하지 않는 인자를 취하고, 유니코드 문자를 반환한다.
# - name() : 인자로 유니코드 문자를 취하고, 대문자 이름을 반환한다.

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u2603')
unicode_test('\u00e9')

import unicodedata
value = unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')
print('value: ', value)
place ='caf\u00e9'
print(place)

place = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
print(place)

u_umlaut = '\N{LATIN SMALL LETTER U WITH ACUTE}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'
print(drink)
print('Now I can finally have my', drink, 'in a', place)

print(len('$'))
print(len('\U0001f47b'))
print('\U0001f47b')


# UTF-8 인코딩과 디코딩
# -------------------

# UTF-8 동적 인코딩
# ----------------
# 유니코드 한 문자당 1 ~ 4바이트 사용
# - 1byte : 아스키코드
# - 2byte : 키릴 문자를 제외한 대부분의 파생된 라틴어
# - 3byte : 기본 다국어 평면의 나머지
# - 4byte : 아시아 언어 및 기호를 포함한 나머지


# 인코딩
# -----
# 문자열을 바이트로 인코딩. 문자열 encode() 함수의 첫번째 인자는 인코딩 이름
# 'ascii', 'utf-8', 'latin-1', 'cp-1252', 'unicode-escape'

snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')   # utf-8은 가변길이 인코딩
print(ds)
print(len(ds))

#ds = snowman.encode('ascii')   # 유니코드 문자가 유효한 ascii문자가 아니기 때문에 에러

# 알수 없는 문자를 인코딩 하지 않음
print(snowman.encode('ascii', 'ignore'))

# 알 수 없는 문자를 ?로 대체
print(snowman.encode('ascii', 'replace'))

# backslashreplace 는 유니코드 이스케이프 처럼 파이썬 유니코드 문자의 문자열을 만듬
print(snowman.encode('ascii', 'backslashreplace'))

# xmlcharrefreplace 는 유니코드 이스케이프 시퀀스를 출력할 수 있는 문자열로 만듬
print(snowman.encode('ascii', 'xmlcharrefreplace'))

# 디코딩
# -----
# 인코딩 과정을 거꾸로 하여 유니코드 문자열을 얻을 수 있음.
place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
print(len(place_bytes))

# utf-8 방식으로 디코딩
place2 = place_bytes.decode('utf-8')
print(place2)

# 다른 방식으로 디코딩: ascii
#place3 = place_bytes.decode('ascii')   # 에러발생. ascii는 0xc3바이트 값은 유효하지 않음
                                       # ascii는 128(16진수 80)에서 255(16진수 FF) 사이
                                       # 에 있는 값의 일부 8비트 문자 셋의 인코딩만 유효

place4 = place_bytes.decode('latin-1')
print(place4)

place5 = place_bytes.decode('windows-1252')
print(place5)

