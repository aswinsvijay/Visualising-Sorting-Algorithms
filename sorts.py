import copy

from main import n

#bubble sort
def bubble(data):
    datalist = list()

    for i in range(n):
        for j in range(n-i-1):
            if(i):
                data[-i][1] = 'green'
            data[j][1] = 'red'
            data[j+1][1] = 'blue'

            datalist.append(copy.deepcopy(data))

            if (data[j][0] > data[j+1][0]):
                data[j] , data[j+1] = data[j+1] , data[j]
                datalist.append(copy.deepcopy(data))

            data[j][1] = 'white'
            data[j+1][1] = 'white'

    data[0][1] = 'green'
    data[1][1] = 'green'
    datalist.append(copy.deepcopy(data))

    return datalist

#selection sort
def selection(data):
    datalist = list()

    for i in range(n-1):
        smallpos = i
        for j in range(i+1,n):
            if data[j][0] < data[smallpos][0]:
                smallpos = j
                
            data[i][1] = 'red'
            data[j][1] = 'red'
            data[smallpos][1] = 'blue'

            datalist.append(copy.deepcopy(data))

            data[i][1] = 'white'
            data[j][1] = 'white'
            data[smallpos][1] = 'white'

        data[i][1] = 'red'
        data[smallpos][1] = 'blue'

        data[i] , data[smallpos] = data[smallpos] , data[i]

        datalist.append(copy.deepcopy(data))

        data[smallpos][1] = 'white'
        data[i][1] = 'green'
    
    data[n-1][1] = 'green'

    datalist.append(copy.deepcopy(data))

    return datalist

#insertion sort
def insertion(data):
    datalist = list()

    data[0][1] = 'green'

    for i in range(1,n):
        x = data[i][0]
        j = i-1
        data[i][1] = 'red'
        datalist.append(copy.deepcopy(data))
        data[j+1][1] = 'green'
        while(j>=0 and x<data[j][0]):
            data[j+1][0] = data[j][0]
            data[j] = [x,'red']
            datalist.append(copy.deepcopy(data))
            data[j][1] = 'green'
            j -= 1
        data[j+1][0] = x
    
    datalist.append(copy.deepcopy(data))

    return datalist