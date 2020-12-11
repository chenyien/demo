
def plotmirror(line, horv, loc):
    for j in line:
        if horv == 'h':
            j[1] += 2*(float(loc) - float(j[1]))
            j[3] += 2*(float(loc) - float(j[3]))
        else:
            j[0] += 2*(float(loc) - float(j[0]))
            j[2] += 2*(float(loc) - float(j[2]))
    for i, aline in enumerate(line):  # 輸出最後結果
        print("Line%d: %0.3f %0.3f %0.3f %0.3f" %
              (i, aline[0], aline[1], aline[2], aline[3]))


line = []
tmp = 0
flag = True
while flag == True:
    line_1 = input()
    if line_1 == "LINESTOP":  # 遇到LINESTOP則座標輸入停止
        flag = False
    else:
        line.append([])  # 填入座標
        for i in line_1.split(','):
            line[tmp].append(float(i))
        tmp += 1
horv, loc = input().split(',')
horv, loc = horv, float(loc)  # 改成小數來計算

plotmirror(line, horv, loc)  # 執行上面定義的函數
