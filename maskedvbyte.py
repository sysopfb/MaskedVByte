import struct

continueBit = 0x80
dataMask = 0x7f
dataBits = 7


def readInt(data):
	out = None
	temp = data
	out = 0
	iterations = 0
	bits = 0
	for val in temp:
		iterations += 1
		val = ord(val)
		t = ((val & dataMask) << bits)
		out |= t
		if (val & continueBit) == 0:
			break
		bits += dataBits
	
	return (out,iterations)

def compressInt(i):
	out = ""
	while i > 0x7f:
		temp = i & 0xff
		i =  i >> dataBits
		temp |= 0x80
		out += struct.pack('<B', temp)
	
	i &= 0x7f
	out += struct.pack('<B', i)
	return out

if __name__ == "__main__":
	test = "\xa4\xfcH"
	a = readInt(test)
	if a[0] == 0x123e24:
		print("Decompression test success")
	test2 = compressInt(0x123e24)
	if test2 == test:
		print("Compression test success")
