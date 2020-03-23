# Text Strings
# ------------
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

# Let’s try some characters, beginning with a plain ASCII letter:`
unicode_test('A')

# ASCII punctuation:
unicode_test('$')

# A Unicode currency character:
unicode_test('\u00a2')

# Another Unicode currenc character:
unicode_test('\u20ac')

# The only problem you could potentially run into is limitations in the font you’re using to display text.
unicode_test('\u2603')

# Suppose that we want to save the word café in a Python string.
# One way is to copy and paste it from a file or website and hope that it works:
place = 'café'
print(place)

# This worked because I copied and pasted from a source that used UTF-8 encoding
# (which you’ll see in a few pages) for its text.

# How can we specify that final é character? If you look at character index for E, you see
# that the name E WITH ACUTE, LATIN SMALL LETTER has the value 00E9.
# Let’s check with the name() and lookup() functions that we were just playing with.
# First give the code to get the name:
unicode_test('\u00e9')

# Next, give the name to look up the code:

# NOTE
# ----
# The names listed on the Unicode Character Name Index page were reformatted to make them sort nicely for display.
# To convert them to their real Unicode names (the ones that Python uses), remove the comma
# and move the part of the name that was after the comma to the beginning.
# Accordingly, change E WITH ACUTE, LATIN SMALL LETTER to LATIN SMALL LETTER E WITH ACUTE:
import unicodedata

value = unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')


# Now, we can specify the string café by code or by name:
place = 'caf\u00e9'
print(place)

place = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
print(place)

# In the preceding snippet, we inserted the é directly in the string, but we can also build a string by appending:
u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)


drink = 'Gew' + u_umlaut + 'rztraminer'
print(drink)
print('Now I can finally have my', drink, 'in a', place)

# The string len function counts Unicode characters, not bytes:
print(len('$'))
print(len('\U0001f47b'))
print('\U0001f47b')


# Encode and decode with UTF-8(UTF-8 인코딩과 디코딩)
# -------------------------------------------------

# UTF-8 동적 인코딩
# ----------------
# 유니코드 한 문자당 1 ~ 4바이트 사용
# - 1byte : 아스키코드
# - 2byte : 키릴 문자를 제외한 대부분의 파생된 라틴어
# - 3byte : 기본 다국어 평면의 나머지
# - 4byte : 아시아 언어 및 기호를 포함한 나머지


# Encoding(인코딩)
# ---------------
# 문자열을 바이트로 인코딩. 문자열 encode() 함수의 첫번째 인자는 인코딩 이름:
# 1. 'ascii':         : Good old seven-bin ASCII
# 2. 'utf-8'          : Eight-bit variable-length encoding, and what you almost always want to use
# 3. 'latin-1'        : Also known as ISO 8859-1
# 4. 'cp-1252'        : A common Windows encoding
# 5. 'unicode-escape' : Python Unicode literal format, \uxxxx or \Uxxxxxxxx

# You can encode anything as UTF-8. Let’s assign the Unicode string '\u2603' to the name snowman:
snowman = '\u2603'
print(len(snowman))
ds = snowman.encode('utf-8')   # utf-8은 가변길이 인코딩
print(ds)
print(len(ds))       # Retrun: 3

# Now, len() returns the number of bytes (3) because ds is a bytes variable.

# You can use encodings other than UTF-8, but you’ll get errors if the Unicode string can’t be handled by
# the encoding. For example, if you use the ascii encoding, it will fail unless your Unicode characters
# happen to be valid ASCII characters as well:
try:
    ds = snowman.encode('ascii')   # 유니코드 문자가 유효한 ascii문자가 아니기 때문에 에러
except UnicodeEncodeError as e:
    print('[Exception Occured]:', e)


# The encode() function takes a second argument to help you avoid encoding exceptions.
# Its default value, which you can see in the previous example, is 'strict';
# it raises a UnicodeEncodeError if it sees a non-ASCII character.
# There are other encodings. Use 'ignore' to throw away anything that won’t encode:

# 알수 없는 문자를 인코딩 하지 않음  ~ 'ignore'
print(snowman.encode('ascii', 'ignore'))

# Use 'replace' to substitute ? for unknown characters:
# 알 수 없는 문자를 ?로 대체 ~ 'replace'
print(snowman.encode('ascii', 'replace'))

# Use 'backslashreplace' to produce a Python Unicode character string, like unicode-escape:
# backslashreplace 는 유니코드 이스케이프 처럼 파이썬 유니코드 문자의 문자열을 만듬 ~ 'backslashreplace'
print(snowman.encode('ascii', 'backslashreplace'))

# You would use this if you needed a printable version of the Unicode escape sequence.
# The following produces character entity strings that you can use in web pages:
# xmlcharrefreplace 는 유니코드 이스케이프 시퀀스를 출력할 수 있는 문자열로 만듬
print(snowman.encode('ascii', 'xmlcharrefreplace'))


# Decoding(디코딩)
# ---------------
# We decode byte strings to Unicode strings. Whenever we get text from some external source (files, databases,
# websites, network APIs, and so on), it’s encoded as byte strings. The tricky part is knowing which encoding was
# actually used, so we can run it backward and get Unicode strings.
# The problem is that nothing in the byte string itself says what encoding was used. I mentioned the perils
# of copying and pasting from websites earlier. You’ve probably visited websites with odd characters
# where plain old ASCII characters should be.
# Let’s create a Unicode string called place with the value 'café':

# 인코딩 과정을 거꾸로 하여 유니코드 문자열을 얻을 수 있음.
place = 'caf\u00e9'
print(place)
print(type(place))

place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
print(len(place_bytes))


# Notice that place_bytes has five bytes. The first three are the same as ASCII (a strength of UTF-8),
# and the final two encode the 'é'. Now, let’s decode that byte string back to a Unicode string:
# utf-8 방식으로 디코딩
place2 = place_bytes.decode('utf-8')
print(place2)

# This worked because we encoded to UTF-8 and decoded from UTF-8. What if we told it to decode
# from some other encoding?
try:
    place3 = place_bytes.decode('ascii')   # 에러발생. ascii는 0xc3바이트 값은 유효하지 않음
                                           # ascii는 128(16진수 80)에서 255(16진수 FF) 사이
                                           # 에 있는 값의 일부 8비트 문자 셋의 인코딩만 유효
except UnicodeDecodeError as e:
    print('[Exception Occured]:', e)

# The ASCII decoder threw an exception because the byte value 0xc3 is illegal in ASCII.
# There are some 8-bit character set encodings in which values between 128 (hex 80) and 255 (hex FF) are legal
# but not the same as UTF-8:
place4 = place_bytes.decode('latin-1')
print(place4)

place5 = place_bytes.decode('windows-1252')
print(place5)


# Format
# ------
# Python has two ways of formatting strings, loosely called old style and new style.
# Both styles are supported in Python 2 and 3 (new style in Python 2.6 and up).
# Old style is simpler, so we’ll begin there.

# Old style with %
# ----------------
# The old style of string formatting has the form string % data.
# Inside the string are interpolation sequences.
# Table 7-2 illustrates that the very simplest sequence is a % followed
# by a letter indicating the data type to be formatted.
# Table 7-2. Conversion types
# 1. %s : string
# 2. %d : decimal integer
# 3. %x : hex integer
# 4. %o : octal integer
# 5. %f : decimal float
# 6. %e : exponential float
# 7. %g : decimal or exponential float
# 8. %% : a literal %

# integer
print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 42)

# float
print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)

# integer an a literal %
print('%d%%' % 100)

#Some string and integer interpolation:
actor = 'Richard Gere'
cat = 'Chester'
weight = 28

print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight))

n = 42
f = 7.03565
s = 'string cheese'

print('%d %f %s' % (n, f, s))

# Set a minimum field width of 10 characters for each variable, and align them to the right,
# filling unused spots on the left with spaces:
print('%10d %10f %10s' % (n, f, s))

# Use the same field width, but align to the left:
print('%-10d %-10f %-10s' % (n, f, s))

# This time, the same field width, but a maximum character width of 4, and aligned to the right.
# This setting truncates the string, and limits the float to 4 digits after the decimal point:
# Important : 소수점은 반올림, 문자는 2글자만 출력
print('%.4d %.4f %.4s' % (n, f, s))

# The same song as before, but right-aligned:
print('%-.4d %-.4f %-.4s' % (n, f, s))

# Finally, get the field widths from arguments rather than hard-coding them:
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))


# New style formatting with {} and format
# ---------------------------------------
# Old style formatting is still supported. In Python 2, which will freeze at version 2.7, it will be supported
# forever. However, new style formatting is recommended if you’re using Python 3.
# The simplest usage is demonstrated here:
n = 42
f = 7.03565
s = 'string cheese'

print('first: {} {} {}'.format(n, f, s))

# Old-style arguments needed to be provided in the order in which their % placeholders appeared in the string.
# With new-style, you can specify the order:
print('second: {2} {0} {1}'.format(n,f,s))

# The arguments can be a dictionary or named arguments, and the specifiers can include their names:
print('{n} {f} {s}'.format(n=42, f=7.03565, s='string cheese'))

# In this next example, let’s try combining our three values into a dictionary, which looks like this:
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

# In the following example, {0} is the entire dictionary, whereas {1} is the string 'other' that
# follows the dictionary:
print('third: {0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))

# These examples all printed their arguments with default formats. Old-style allows a type specifier
# after the % in the string, but new-style puts it after a :. First, with positional arguments:
print('{0:d} {1:f} {2:s}'.format(n, f, s))

# In this example, we’ll use the same values, but as named arguments:
print('{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese'))

# The other options (minimum field width, maximum character width, alignment, and so on) are also supported.
# Minimum field width 10, right-aligned (default):
print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))

# Same as the preceding example, but the > characters make the right-alignment more explicit:
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))

# Minimum field width 10, left-aligned:
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))

# Minimum field width 10, centered:
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))

# There is one change from old-style: the precision value (after the decimal point) still means the
# number of digits after the decimal for floats, and the maximum number of characters for strings,
# but you can’t use it for integers:
# Integer에서는 소수점 이하 표현을 사용할 수 없음.
try:
    print('{0:>10.4d} {1:>10.4f} {2:10.4s}'.format(n, f, s))
except ValueError as e:
    print('[Exception Occured]:', e)

print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))

# The final option is the fill character. If you want something other than spaces to pad your output
# fields, put it right after the :, before any alignment (<, >, ^) or width specifiers:
print('{0:!^20s}'.format('Big Sale'))


# Match with Regular Expressions
# ------------------------------
# result = re.match('You', 'Young Frank')
# 'You' : pattern, 'Young Frank' : source
# match() : Checks whether the source begins with the pattern.

# For more complex matches, you can compile your pattern first to speed up the match later:
import re
you_pattern = re.compile('You')

# Then, you can perform your match against the compiled pattern:
result = you_pattern.match('Young Frank')

# match() is not the only way to compare the pattern and source.
# Here are several other methods you can use:
# 1. search()   : returns the first match, if any.
# 2. findall()  : returns a list of all non-overlapping matches, if any.
# 3. split()    : splits source at matches with pattern and returns a list of the string pieces.
# 4. sub()      : takes another replacement argument, and changes all parts of source that are matched by
#                 pattern to replacement.

# Exact match with match()
# ------------------------
import re

source = 'Young Frankenstein'
m = re.match('You', source)    # match starts at the beginning of source

if m:       # match return an object; do this to see what matched
    print('[Pattern: You, Source: Young Frankenstein]:', m.group())
print('Result m:', m)

m = re.match('^You', source)    # start anchor does the same
if m:
    print('[Pattern: ^You, Source: Young Frankenstein]:', m.group())
print('Result m:', m)

# How about 'Frank'?
m = re.match('Frank', source)    # Doesn't Start with 'Frank'
if m:                            # m = None, None is not True and False
    print('[Pattern: Frank, Source: Young Frankenstein]:', m.group())
print('Result m:', m)

# Let’s change the pattern:
m = re.match('.*Frank', source)     # .  : \n을 제외한 모든 단일 문자, any single character.
                                    # *  : 선행문자를 0개 이상 찾음, any number of the preceding thing.
                                    # .* : Mean any number of characters(even 0)
if m:
    print('[Pattern: .*Frank, Source: Young Frankenstein]:', m.group())
print('Result m:', m)


# First match with search()
# -------------------------
# You can use search() to find the pattern 'Frank' anywhere in the source string 'Young Frankenstein',
# without the need for the .* wildcards:
m = re.search('Frank', source)
if m:
    print('search()[Pattern: Frank, Source: Young Frankenstein]:', m.group())
print('Result m:', m)


# All matches with findall() ~ Not use m.group()
# ----------------------------------------------
m = re.findall('n', source)
if m:
    print('findall()[Pattern: n, Source: Young Frankenstein]:', m)
print('Result m:', m)

# How about 'n' followed by any character?
m = re.findall('n.', source)       # Return: List Type
if m:
    print('findall()[Pattern: n., Source: Young Frankenstein]:', m)
print('Result m:', m)

# Notice that it did not match that final 'n'.
# We need to say that the character after 'n' is optional with ?:
m = re.findall('n.?', source)       # Return: List Type
if m:
    print('findall()[Pattern: n.?, Source: Young Frankenstein]:', m)
print('Result m:', m)

# Split at matches with split()
# -----------------------------
# The example that follows shows you how to split a string into a list by a pattern rather than a simple
# string (as the normal string split() method would do):
m = re.split('n', source)       # Return: List Type
if m:
    print('split()[Pattern: n, Source: Young Frankenstein]:', m)
print('Result m:', m)

# Replace at matches with sub()
# -----------------------------
# This is like the string replace() method, but for patterns rather than literal strings:
m = re.sub('n', '?', source)    # 매칭되면 replace
print('sub()[Pattern: n, Replace: ?, Source: Young Frankenstein]:', m)

m = re.sub('v', '?', source)    # 매칭 안되면 원래 source 반환
print('sub()[Pattern: n, Replace: ?, Source: Young Frankenstein]:', m)



import os
os.exit()




