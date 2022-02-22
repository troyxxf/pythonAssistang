

def encryption(num):
    if num==".":
        num=0
    newNum = []

    for i in str(num):
        if(i=="."):
            break
        if int(i):
            newNum.append(str(10 - int(i) * 7 % 10))
        else:
            newNum.append(str(0))
    return int(''.join(newNum))
def decryption(num):
    oldNum = []
    [oldNum.append(str(int(i) * 7 % 10)) for i in str(num)]
    # print int(''.join(oldNum))
    return int(''.join(oldNum))


print("start")
get_data=[]
with open("data.txt","r",encoding='utf-8') as f:
    for line in f:
        # print(line)
        lili=line.split()
        # print(lili)
        get_data.append(lili)
xuehao=input("Please input your studentID:")
xuehao=encryption(xuehao)
print(xuehao)
flag=0
for i in range(1,len(get_data)):
    if(get_data[i][0]==str(xuehao)):
        get_data[i][0] = "studentID:",decryption(get_data[i][0])
        get_data[i][2] = "score:",decryption(get_data[i][2])
        get_data[i][3] = decryption(get_data[i][3])
        get_data[i][5] = decryption(get_data[i][5])
        get_data[i][6] = decryption(get_data[i][6])
        get_data[i][7] = decryption(get_data[i][7])
        get_data[i][8] = decryption(get_data[i][8])
        get_data[i][9] = decryption(get_data[i][9])
        get_data[i][10] = decryption(get_data[i][10])
        get_data[i][11] = decryption(get_data[i][11])
        print(get_data[i][0],get_data[i][1],get_data[i][2])
        flag=1
if flag==0:
    print("not found studentID")



