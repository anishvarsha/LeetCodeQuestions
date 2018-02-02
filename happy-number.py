def number(num):
    k = []
    while(num>0):
        k.append(num%10)
        num = num/10
    k = k[::-1]
    sq = 0
    for i in k:
        sq+=i*i
    print sq
    return sq

su = 3
while(su>2):
   su = number(su)