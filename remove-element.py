a = list(map(int, raw_input().split(" ")))
b = int(raw_input().strip(" "))

print list(filter(lambda x: x!=b, a))