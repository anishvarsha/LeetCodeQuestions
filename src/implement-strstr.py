haystack = raw_input()
needle = raw_input().strip(" ")

if (len(haystack) == 0 and len(needle)==0) or len(needle)==0:
    return 0

h = list(map(str, haystack.split(" ")))
if needle not in h:
    return -1
p = 0
for i in range(len(h)):
    if h[i] == needle:
        p = i
        return p
        break
if p != 0:
    return p
        