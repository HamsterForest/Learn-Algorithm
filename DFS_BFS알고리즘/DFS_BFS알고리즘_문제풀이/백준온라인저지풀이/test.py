length=4
num=[1,2,3,4]
number=0
for j in range(length):
            number+=num[j]*(10**(length-1))
            print(number)
            length-=1
print(2**3)
print(number)