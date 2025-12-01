import matplotlib.pyplot as plt
info = []
x = []
y = []
f = open("opendata.stat.txt", mode = "r", encoding = "utf-8")
for line in f:
    array = line.split(",")
    if array[0] == "Средняя пенсия" and array[1] == "Забайкальский край" and array[2] >= "2018-01-01" and array[2] <= "2019-12-31":
        info.append(array)

info.sort(key = lambda x: x[2])
sum = 0
for elm in info:
    sum += int(elm[3])
    date = elm[2].split("-")
    x.append(int(date[1]))
    y.append(int(elm[3]))

print(sum / len(info))

plt.plot(x, y)
plt.title("Средняя пенсия за 2018 год")
plt.xticks(x)
plt.show()
f.close()