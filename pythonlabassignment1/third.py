n=int(input("enter till which number of keys you want"))
dict={}
for i in range(1, n + 1):
        dict[i] = i * i
print(dict)