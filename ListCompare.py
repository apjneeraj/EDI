
def Largest(a,b,c):
    if a>max(b,c):
        return -1
    elif a <= min(b,c):
        return min(b,c)
    else:
        return max(b,c)


def uniquerelation(list1,list2,len_input):

    list3=[]
    for i in range(len_input):
        if len(list3)==0:
            if list1[i] > list2[i]:
                list3.append(list2[i])
            else:
                list3.append(list1[i])
        else:
            x = Largest(list3[i-1],list1[i],list2[i])
            if x is not -1:
                list3.append(x)
            else:

                return 'NO'

    return 'YES'

Test_cases = int(input())
for noTC in range(Test_cases):
    Len = int(input())


    seq1=input().split()
    seq1=[int(i) for i in seq1]

    seq2=input().split()
    seq2=[int(i) for i in seq2]

    x=uniquerelation(seq1,seq2,Len)
    print(x)
