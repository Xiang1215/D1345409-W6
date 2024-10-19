#計算成績平均
tot = 0
t = 0

while True:
    n = input('請輸入成績（輸入-1結束）: ')
    if n.isdigit():
        n = int(n)
        tot += n
        t += 1
    elif n == '-1':
        if t == 0:
            print('沒有輸入任何成績')
        else:
            avg = tot / t
            print('平均成績為:', "{:.2f}".format(avg))
        break
    else:
        
        if n.isalnum():
            print('請輸入有效數字')
        else:
            print('成績不能為負數,請重新輸入.')