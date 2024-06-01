name = 'Электроэнцефалограмма'
print(name[0])
print(name[-1])
a = len(name)//2
if a//2 == 0:
    print(name[a-1:])
else:
    print(name[a:])
print(name[::-1])
print(name[1::2])