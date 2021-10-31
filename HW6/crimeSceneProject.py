fhand=open("crime_scene.txt")
wlimit=0
tlimit=0
linelist=[]
N=0
evidences=[]
for line in fhand:
    linelist=line.rstrip().split()
    if len(linelist) == 2:
        wlimit=int(linelist[0])
        tlimit = int(linelist[1])
    elif len(linelist)==1:
        N=int(linelist[0])
    else:
        evidences.append(linelist)
#print(wlimit,tlimit,N)
#print(evidences)
fhand.close()

def fw(remaining_wlimit, i):
    if i == N:
        return 0 , []
    if remaining_wlimit-int(evidences[i][1])>=0:
        col_value,col_list=fw(remaining_wlimit-int(evidences[i][1]), i+1)
        col_value+=int(evidences[i][3])
        col_list.append(int((evidences[i][0])))
    else:
        col_value = 0
        col_list  = []

    col_value_nottaken,col_list_nottaken=fw(remaining_wlimit, i+1)

    if col_value>col_value_nottaken:
        return col_value,col_list
    else:
        return col_value_nottaken,col_list_nottaken

def ft(remaining_tlimit, i):
    if i == N:
        return 0 , []
    if remaining_tlimit-int(evidences[i][2]) >= 0:
        col_value,col_list=ft(remaining_tlimit-int(evidences[i][2]), i+1)
        col_value+=int(evidences[i][3])
        col_list.append(int((evidences[i][0])))
    else:
        col_value = 0
        col_list  = []

    col_value_nottaken,col_list_nottaken=ft(remaining_tlimit, i+1)

    if col_value>col_value_nottaken:
        return col_value,col_list
    else:
        return col_value_nottaken,col_list_nottaken


def fwt(remaining_wlimit,remaining_tlimit, i):
    if i == N:
        return 0 , []
    if remaining_wlimit-int(evidences[i][1]) >= 0 and remaining_tlimit-int(evidences[i][2]) >=0:
        col_value,col_list=fwt(remaining_wlimit-int(evidences[i][1]),remaining_tlimit-int(evidences[i][2]), i+1)
        col_value+=int(evidences[i][3])
        col_list.append(int(evidences[i][0]))
    else:
        col_value = 0
        col_list  = []

    col_value_nottaken,col_list_nottaken=fwt(remaining_wlimit,remaining_tlimit, i+1)

    if col_value>col_value_nottaken:
        return col_value,col_list
    else:
        return col_value_nottaken,col_list_nottaken

w_limited_evidences=list(fw(wlimit,0))
t_limited_evidences=list(ft(tlimit,0))
wt_limited_evidences=list(fwt(wlimit,tlimit,0))


def my_quick_sort(lst):
    if (len(lst) <= 1):
        return lst
    pivot = lst[0]
    i = 1
    j = len(lst) - 1
    while (True):
        if (j < i):
            break
        if (lst[i] <= pivot):
            i += 1
            continue
        elif (lst[j] >= pivot):
            j -= 1
            continue
        lst[i], lst[j] = lst[j], lst[i]
    lst[0], lst[j] = lst[j], lst[0]
    lst[0:j] = my_quick_sort(lst[0:j])
    lst[j + 1:] = my_quick_sort(lst[j + 1:])
    return lst

my_quick_sort(w_limited_evidences[1])
my_quick_sort(t_limited_evidences[1])
my_quick_sort(wt_limited_evidences[1])


sol1=open("solution_part1.txt","w")
sol1.write(f"{w_limited_evidences[0]}"+"\n"+f"{' '.join(str(elem) for elem in w_limited_evidences[1])}")
sol1.close()
sol2=open("solution_part2.txt","w")
sol2.write(f"{t_limited_evidences[0]}"+"\n"+f"{' '.join(str(elem) for elem in t_limited_evidences[1])}")
sol2.close()
sol3=open("solution_part3.txt","w")
sol3.write(f"{wt_limited_evidences[0]}"+"\n"+f"{' '.join(str(elem) for elem in wt_limited_evidences[1])}")
sol3.close()






