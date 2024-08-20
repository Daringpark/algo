# 학점 계산기

list_GPA = [['D+', 'D0', 'D-'], ['C+', 'C0', 'C-'], ['B+', 'B0', 'B-'], ['A+', 'A0', 'A-']]

n = len(list_GPA)
x = input()
for i in range(n) :
    m = len(list_GPA[i])
    for j in range(m) :
        if x in list_GPA[i][j] :
            res = i + 1.0
            if j > 1 :
                res -= 0.3
            elif j <= 0 : 
                res += 0.3
        elif x == 'F' :
            res = 0.0
print(res)

## 처리 시간 -, 코드 길이 -
# dictionary 활용이네 >> Hash
scores = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7,
          'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
score = input()
print(scores[score])