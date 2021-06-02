def function (x1, x2):
    function = (10*(x1 - x2)**2 + (x1 - 1)**2)**(1/4)
    return function

def sort(sortf):
    for row in sortf:
        sortf.sort(key=lambda row: row[2])
    return sortf

best = []
good = []
worst = []
sortf = []
i = 0

point1 = [int(input("x1 = ")), int(input("y1 = "))]
point1.append(function(point1[0], point1[1]))
point2 = [int(input("x2 = ")), int(input("y2 = "))]
point2.append(function(point2[0], point2[1]))
point3 = [int(input("x3 = ")), int(input("y3 = "))]
point3.append(function(point3[0], point3[1]))
count_iter_func = 3

print("Перша точка: [", point1[0], ",", point1[1], "] із значенням в ній", point1[2])
print("Друга точка: [", point2[0], ",", point2[1], "] із значенням в ній", point2[2])
print("Третя точка: [", point3[0], ",", point3[1], "] із значенням в ній", point3[2])

sortf.append(point1)
sortf.append(point2)
sortf.append(point3)

sort(sortf)

best = sortf[0]
good = sortf[1]
worst = sortf[2]

while (i < 40):
    print()
    print("Ітерація №", i + 1)
    print("Наразі:")
    print("best = [", best[0], ",", best[1], "] із значенням", best[2])
    print("good = [", good[0], ",", good[1], "] із значенням", good[2])
    print("worst = [", worst[0], ",", worst[1], "] із значенням", worst[2])
    point_c = [(good[0] + best[0])/2, (good[1] + best[1])/2]
    print("Середина відрізку навпроти найгіршої точки:", point_c)

    point_r = [2*point_c[0] - worst[0], 2*point_c[1] - worst[1]]
    point_r.append(function(point_r[0], point_r[1]))
    count_iter_func += 1
    print("Віддзеркалене значення відносно середини відрізку: [", point_r[0], ",", point_r[1], "] із значенням в ній", point_r[2])

    if (point_r[2] < best[2]):
        point_e = [2*point_r[0] - point_c[0], 2*point_r[1] - point_c[1]]
        point_e.append(function(point_e[0], point_e[1]))
        count_iter_func += 1
        if (point_e[2] < best[2]):
            worst = point_e
        else:
            worst = point_r
    if (best[2] < point_r[2] < good[2]):
        worst = point_r
    if (worst[2] > point_r[2] > good[2]):
        worst_prom = worst
        worst = point_r
        point_r = worst_prom
        point_s = [0.5*worst[0] + 0.5*point_c[0], 0.5*worst[1] + 0.5*point_c[1]]
        point_s.append(function(point_s[0], point_s[1]))
        count_iter_func += 1
        print(point_s)
        if (point_s[2] < worst[2]):
            worst = point_s
        if (point_s[2] > worst[2]):
            good = [good[0] + (best[0] - good[0])/2, good[1] + (best[1] - good[1])/2]
            worst = [worst[0] + (best[0] - worst[0])/2, worst[1] + (best[1] - worst[1])/2]
    elif (point_r[2] > worst[2]):
        point_s = [0.5 * worst[0] + 0.5 * point_c[0], 0.5 * worst[1] + 0.5 * point_c[1]]
        point_s.append(function(point_s[0], point_s[1]))
        count_iter_func += 1
        print(point_s)
        if (point_s[2] < worst[2]):
            worst = point_s
        if (point_s[2] > worst[2]):
            good = [good[0] + (best[0] - good[0]) / 2, good[1] + (best[1] - good[1]) / 2]
            worst = [worst[0] + (best[0] - worst[0]) / 2, worst[1] + (best[1] - worst[1]) / 2]

    sortf = []
    sortf.append(best)
    sortf.append(good)
    sortf.append(worst)

    sort(sortf)
    print(sortf)

    best = sortf[0]
    good = sortf[1]
    worst = sortf[2]
    i = i + 1
    print("Кількість разів обрахування функції для ітерації №", i, "дорівнює", count_iter_func)


