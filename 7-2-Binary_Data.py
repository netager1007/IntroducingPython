# 이진 데이터
# ----------
# 엔디안(컴퓨터 프로세서가 데이터를 바이트로 나누는 방법) 과 정수에 대한 사인비트(Sign Bit)
# 개념을 알아야 함.
# 데이터를 추출하거나 변경하는 바이너리 파일 형식과 네트우크 패킷을 배워야 함.


# 바이트와 바이트 배열
# - 바이트는 튜플처럼 불변(immutable)
# - 바이트 배열은 바이트이 리스트처럼 변경 가능(mutable)
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

print(b'\x61')
print(b'\x01abc\xff')

# the_bytes[1] = 127         # 오류발생 : bytes 변수가 불변. 바꾸려 하면 에러
print(the_bytes[1])

the_byte_array = bytearray(blist)
print(the_byte_array)
the_byte_array[1] = 127
print(the_byte_array)
print(the_byte_array[1])

the_bytes = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))
print(the_bytes)
print(the_byte_array)

# 이진 데이터 변환하기 : struct
# unpack()에서 >LL 은 입력한 바이트 시퀀스를 해석하고, 파이썬 데이터 형식으로 만들어 주는
# 형식 문자열.
# >는 정수가 빅엔디안(big-endian) 형식으로 저장되었다는 것을 의미
# 각각의 L은 4바이트의 부호 없는 긴 정수(Unsigned long integer)를 지정

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\rlHDR' + \
       b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[15:23])  # width : 16~19, height : 20~23
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print('width: ', data[15:19])
print('height: ', data[19:23])
print(0x9a)
print(0x8d)

# pack()
import struct
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))