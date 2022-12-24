from matplotlib import pyplot


open_1 = []
high_1 = []
low_1 = []
close_1 = []

open_2 = []
high_2 = []
low_2 = []
close_2 = []

open_3 = []
high_3 = []
low_3 = []
close_3 = []

open_4 = []
high_4 = []
low_4 = []
close_4 = []

f = open('SPFB.RTS-12.18_180901_181231.csv')
title = f.readline()
a = f.read()
a = a.split('\n')
a.pop()
for i in a:
    i = i.split(",")
    if '06/09' in i[2]:
        open_1.append(int(float(i[4])))
        high_1.append(int(float(i[5])))
        low_1.append(int(float(i[6])))
        close_1.append(int(float(i[7])))

for i in a:
    i = i.split(",")
    if '08/10' in i[2]:
        open_2.append(int(float(i[4])))
        high_2.append(int(float(i[5])))
        low_2.append(int(float(i[6])))
        close_2.append(int(float(i[7])))

for i in a:
    i = i.split(",")
    if '06/11' in i[2]:
        open_3.append(int(float(i[4])))
        high_3.append(int(float(i[5])))
        low_3.append(int(float(i[6])))
        close_3.append(int(float(i[7])))

for i in a:
    i = i.split(",")
    if '06/12' in i[2]:
        open_4.append(int(float(i[4])))
        high_4.append(int(float(i[5])))
        low_4.append(int(float(i[6])))
        close_4.append(int(float(i[7])))

pyplot.boxplot([open_1, high_1, low_1, close_1,
                open_2, high_2, low_2, close_2,
                open_3, high_3, low_3, close_3,
                open_4,  high_4, low_4, close_4])
pyplot.show()
