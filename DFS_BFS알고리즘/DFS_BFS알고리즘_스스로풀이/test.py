cities=[]
for i in range(5):
    cities.append([i+1,-1])#도시 종류들을 저장한다. 나중에 지어나갈 때 쓴다.
    #-1은 k값의 초기값(아직 k 값이 결정 되지 않음)

cities[0][1]=0

print(cities)