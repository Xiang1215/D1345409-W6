#旋轉數字
x=input('輸入 : x=')
X=x
a=0
x_list=[]
a_list=[]
b_list=[]
ans=''
for i in range(len(x)):
    x=int(x)
    x_list.append(x%10)
    x=(x-x%10)//10
x_list.reverse()
for i in range(len(x_list)):
    if all(x in [0, 1, 8] for x in x_list):
        for i in range(len(x_list)):
            if x_list[i] == 0:  
                x_list[i] = 0   
            elif x_list[i] == 1:  
                x_list[i] = 1
            elif x_list[i] == 8:  
                x_list[i] = 8
        for i in range(len(x_list)):
            a=a+(x_list[i])*10**(len(x_list)-1-i)
        print('輸出 : true')
        print('解釋 : 旋轉 180 度後,',X,'變成 ',a,', 與原數字一致。')
        break
    elif all(x in [6, 9] for x in x_list):
        for i in range(len(x_list)): 
            if x_list[i] == 6:  
                x_list[i] = 9   
            elif x_list[i] == 9:  
                x_list[i] = 6
            else :
                x_list[i]=x_list[i]
        for i in range(len(x_list)):
            a=a+(x_list[i])*10**(len(x_list)-1-i)
        print('輸出 : false')
        print('解釋 : 旋轉 180 度後,',X,'變成 ',a,', 與原數字不同。')
        break
    elif all(x in [2, 3, 4, 5, 7] for x in x_list):
        for i in range(len(x_list)): 
            if x_list[i] in [2,3,4,5,7]:
                a_list.append(x_list[i])
                if (i+1)-len(x_list)!=0:
                    ans=ans+(str(a_list[i])+'和')
                else:
                    ans=ans+(str(a_list[i]))
        print('輸出 : false')
        print('解釋 :', ans, '在旋轉後無法形成有效的數字。')
        break
    else:
        for i in range(len(x_list)):
            if x_list[i] in [2,3,4,5,7]:
                b_list.append(x_list[i])
        for j in range(len(b_list)):
            if (j+2)-len(x_list)!=0:
                ans=ans+str(b_list[j])+'和'
            else:
                ans=ans+str(b_list[j])
        print('輸出 : false')
        print('解釋 :', ans, '不能形成有效的數字。')
        break