max_bit = 2**32
max_bit_complement = -2**32

(a, b) = map(int, raw_input().split(" "))
print a, b

while(b!=0):
	if b==max_bit:
		return a ^ max_bit_complement

	carry = a & b
	a = a ^ b
	b = carry << 1
print a
