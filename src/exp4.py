from random import random

chainList = []
chainList1 = []
chainList2 = []
ope_num = 20000

i = 0

input_file = open('/Users/chuyang/Desktop/input/input9.txt', 'w')

while i < ope_num:
    i += 1
    ope = int(random() * 10) % 5 + 1

    if ope == 1:
        num = int(random() * 10000000)
        input_file.write('1 '+str(num)+'\n')
        chainList.insert(0, num)

    if ope == 2:
        if random() > 0.7:
            continue
        listSize = len(chainList)
        if listSize == 0:
            continue
        remove_num = chainList[int(random() * ope_num) % listSize]
        input_file.write('2 '+str(remove_num)+'\n')
        chainList.remove(remove_num)
    if ope == 3:
        listSize = len(chainList)
        if listSize == 0:
            continue
        if random() > 0.5:
            find_num = chainList[int(random() * ope_num) % listSize]
            input_file.write('3 '+str(find_num)+'\n')
        else:
            input_file.write('3 '+str(int(random() * 10000000))+'\n')
    if ope == 4:
        listSize = len(chainList)
        if listSize == 0:
            continue
        input_file.write('4\n')
    if ope == 5:
        listSize = len(chainList)
        if listSize == 0:
            continue
        input_file.write('5\n')

listSize1 = int(random()*1000) + 1
listSize2 = int(random()*1000) + 1

input_file.write('6\n'+str(listSize1)+' ')
for j in range(0, listSize1):
    item = int(random() * 10000000)
    chainList1.append(item)
chainList1.sort()
for j in range(0, listSize1):
    input_file.write(str(chainList1[j]) + ' ')
input_file.write('\n')

input_file.write(str(listSize2) + ' ')
for j in range(0, listSize2):
    item = int(random() * 10000000)
    chainList2.append(item)
chainList2.sort()
for j in range(0, listSize2):
    input_file.write(str(chainList2[j]) + ' ')
input_file.write('\n')


input_file.close()
