def is_correct(*soap):
    count = 0
    bill = []
    summ = 0
    for file in soap:
        correct = True
        with open(file, 'r') as f:
            try:
                for i in f.readline().split():
                    summ = 1/int(i) + summ
            except:
                correct = False
        if correct :
            bill.append(summ)
        else:
            count+=1
    answer = (summ, count)
    print(answer)    
is_correct('i.txt', 'l.txt')