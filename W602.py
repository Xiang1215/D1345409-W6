#簡單計算器
n=input('選擇運算符號 (+, -, *, /) :')
a=int(input('請輸入第一個數字 :'))
if a==-999:
    print('程式結束')
else:
    b=int(input('請輸入第二個數字 :'))
    if b ==-999:
        print('程式結束')
    while a>=0 or b>=0:
        if a>=1 or b >=1:
            if n =='+':
                print('結果: ',a,'+',b,'=',a+b)
                break
            elif n =='-':
                print('結果: ',a,'-',b,'=',a-b)
                break
            elif n =='*':
                print('結果: ',a,'*',b,'=',a*b)
                break
            else :
                if a==0 or b==0:
                    print('不能除以0,請重新輸入.')
                else:
                    print('結果: ',a,'/',b,'=',a/b)
                    
                break
        else:
            break