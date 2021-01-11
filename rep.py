import random

def daletou():
    ''' 大乐透模拟选号 '''

    seq1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    seq2 = [1,2,3,4,5,6,7,8,9,10,11,12]
    l_front  = []
    l_behind = []
    ll = []
        
    for i in range(5):
        front = random.choice(seq1)
        seq1.remove(front)
        l_front.append(front)

    for i in range(2):
        behind = random.choice(seq2)
        seq2.remove(behind)
        l_behind.append(behind)

    l_front.sort()
    l_behind.sort()

    for i in l_front:
        i = int(i)
        i = '%02d' %i
        ll.append(i)

    ll.append('+')

    for i in l_behind:
        i = int(i)
        i = '%02d' %i
        ll.append(i)

    return ll
