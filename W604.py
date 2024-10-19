#回文數
x=input('輸入: x= ')
x_list=[]
X=int(x)
a=0
t=0
if x.isdigit(): 
    if X%10!=0 and X==a :
        for i in range(len(x)):
            x=int(x)
            x_list.append(x%10)
            x=(x-x%10)//10
        x_list.reverse()

        for i in range(len(x_list)):
                a=a+(x_list[i])*10**(len(x_list)-1-i)                 
        
        print('輸出: true')
        print('解釋:',X,'從左到右讀為',X,'從右到左讀為',a,'。')
    
    else:
        while X%10==0:
                X=X//10
                t+=1        
        for i in range(len(str(X))):
            x_list.append(X%10)
            X=(X-X%10)//10

        for i in range(len(x_list)):
                a=a+(x_list[i])*10**(len(x_list)-1-i)
        a=(str('0')*t)+str(a)
        print('輸出: false')
        print('解釋: 從右向左讀取',a,'。因此它不是回文。')
else:
    n=int(x)*-1
    for i in range(len(x)-1):
        x_list.append(n%10)
        n=(n-n%10)//10
    x_list.reverse()

    for i in range(len(x_list)):
        a=a+(x_list[i])*10**(len(x_list)-1-i)
    
    a=str(a)+str('-')+str('。')
    print('輸出: false')
    print('解釋: 從左到右,讀取的是',X,'從左到右,變成',a,'因此它不是回文。')