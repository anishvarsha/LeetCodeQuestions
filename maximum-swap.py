num = map(int, list(raw_input()))


def magic(number):
    return int(''.join(str(i) for i in number))


print num
val = map(int, num)
sortedVal = list(num)
sortedVal.sort()
sam = num.index(sortedVal[0])
lar = num.index(sortedVal[-1])
temp = num[sam]
num[sam] = num[lar]
num[lar] = temp
fin = magic(num)
print fin