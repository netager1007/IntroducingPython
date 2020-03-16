blist = [1,2,3,255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)

print(the_bytes[1])
# the_bytes[1] = 3   # Error Occured
print(type(the_bytes))
print(the_byte_array[1])

the_byte_array[1] = 120
print(the_byte_array[1])

the_bytes = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))

print(the_bytes)
print(the_byte_array)

import struct
valid_png_header = b"\x89PNG\r\n\x1a\n"
data = b'\x89PNG\r\n\x1a\n\x00\x00\rlHDR' + b"\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0"
if data[:8] == valid_png_header :
    print('abc')
    width, height = struct.unpack(">2L", data[16,24])
    print("valid PNG, width", width, "height", height)
else:
    print("Not a valid PNG")

print(struct.pack(">L", 154))
print(struct.pack(">L", 141))

print(bytes(154))