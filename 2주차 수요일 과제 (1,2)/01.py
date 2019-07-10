bunch=list(input('단어를 입력하시오: ').split())

minlen=len(bunch[0])

common=''

for i in range(len(bunch)):
    if len(bunch[i])<minlen:
        minlen=len(bunch[i])


for j in range(minlen):
    if j!=0:
        if count!=len(bunch):
            break
    count=0
    for i in range(len(bunch)):
        if bunch[i][j]==bunch[0][j]:
            count+=1
        if i==len(bunch)-1:
            if count==len(bunch):
                common+=bunch[i][j]
                
print(common)
