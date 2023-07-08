def DFS(familyInform, startFam, destinationFam, chon):
        familyInform[startFam][0] = 1

        for fam in familyInform[startFam][1]:
            if fam == destinationFam:
                print(chon+1)
                exit(0)

            if familyInform[fam][0] == 0:
                DFS(familyInform, fam, destinationFam, chon+1)

# 1. 입력
n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

# 2. 사람들과 연결 표현
familyInform = [None]

for i in range(n):
   familyInform.append([0, []])

for i in range(m):
   fam1, fam2 = map(int, input().split())
   familyInform[fam1][1].append(fam2)
   familyInform[fam2][1].append(fam1)

#print("가족 연결정보 확인", familyInform)

# 3. DFS
DFS(familyInform, target1, target2, 0)
print(-1)