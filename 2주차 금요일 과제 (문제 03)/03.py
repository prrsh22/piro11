dwarf=[]

for i in range(9):
    dwarf.append(int(input()))

found=0

for i in range(len(dwarf)-1):
    for j in range(i+1,len(dwarf)): # i의 오른쪽에 있는 원소들 모두
        if sum(dwarf)-dwarf[i]-dwarf[j]==100:
            del dwarf[i]
            del dwarf[j-1]
            found=1
            break
    if found==1:
        break

dwarf.sort()

for i in range(len(dwarf)):
    print(dwarf[i])
