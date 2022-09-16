
import matplotlib
import matplotlib.pyplot as plt

##########
# ・.txt ではなく、.tx と最後のtだけ読み込まれない問題についての解決策
##########
datalist = ['3,30,100.txt','3,30,200.txt']
for l in datalist:
    data = l
    print(data) #確認用

##########
# 2つのデータを1つのグラフ上に重ねて描画する
##########
plt.title("data")
plt.xlabel("x")
plt.ylabel("y")

#1つ目のデータを用意して、描画する
x_list = [1,20]
y_list = [10,20]
c1 = 'blue'
plt.plot(x_list, y_list, c=c1)

#2つ目のデータを用意して、描画する
y_list.reverse() #リストを逆順にしている
c2 = 'green'
plt.plot(x_list, y_list, c=c2)

plt.savefig("3,30,x.png")
