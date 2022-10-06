

class TestData():
    def __init__(self) -> None:
        self.count = 0
        self.list = ['2 3',400,410,420,400,400,400,300,300,300]
    def get_data(self):
        ret = self.list[self.count]
        self.count+=1
        return ret
cl_data = TestData()

def input():
    ret= cl_data.get_data()
    return ret

n,m = input().split(' ')
n=int(n)#人数
m=int(m)#課題曲の長さ

tensu=[100]*n #n人のカラオケの点数(初期値は100)

kadaikyoku=[] #課題曲の正しい音程

# ontei=[[0]*m]*n #n人の歌った音程
# 上記では同じオブジェクトが入っているため、期待通りの動作とならない。
ontei = [[0] * m for _ in range(n)]

#課題曲の音程(2行目からm+1行目までをリストに格納)
for i in range(m):
    x=input()
    x=int(x)
    kadaikyoku.append(x)

#n人の音程を2次元配列に格納
#ここから
for j in range(n):
    for i in range(m):
        x=input()
        x=int(x)
        ontei[j][i]=x
        print('ontei({},{}).id = {}'.format(j,i, id(ontei[j][i]) ))
        print('ontei({},{}) = {}'.format(j,i, ontei[j][i]))#値確認用(1)
#ここまでがおかしい?

print('*****')
print('id(ontei) = {}'.format(id(ontei)))
for i in range(n):
    print('id(ontei[{}]) = {}'.format(i, id(ontei[i])))
print('*****')
#値確認用(2)
for j in range(n):
    for i in range(m):
        print('ontei({},{}).id = {}'.format(j,i, id(ontei[j][i]) ))
        print('ontei({},{}) = {}'.format(j,i, ontei[j][i]))

#点数減算処理(0点以下になった場合は0点として処理は終了)
for j in range(n):
    for i in range(m):
        if tensu[j]<=0:
            tensu[j]=0
            break
        
        sa=ontei[j][i]-kadaikyoku[i]
        if -5<=sa and sa<=5:
            continue
        elif -10<=sa and sa<=10:
            tensu[j]-=1
        elif -20<=sa and sa<=20:
            tensu[j]-=2
        elif -30<=sa and sa<=30:
            tensu[j]-=3
        else:
            tensu[j]-=5
            
tensu.sort(reverse=True)
print(tensu[0])#最高点を表示