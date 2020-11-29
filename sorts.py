import copy

from config import n

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

def selection(data):
    datalist = list()

    for i in range(n-1):
        smallpos = i
        for j in range(i+1,n):
            data[i][1] = 'red'
            data[j][1] = 'red'
            data[smallpos][1] = 'red'

            datalist.append(copy.deepcopy(data))

            data[i][1] = 'white'
            data[j][1] = 'white'
            data[smallpos][1] = 'white'

            if data[j][0] < data[smallpos][0]:
                smallpos = j

        data[i] , data[smallpos] = data[smallpos] , data[i]

        data[i][1] = 'red'
        data[smallpos][1] = 'red'

        datalist.append(copy.deepcopy(data))

        data[i][1] = 'white'
        data[smallpos][1] = 'white'
    
    data[n-2][1] = 'white'
    data[n-1][1] = 'white'

    datalist.append(copy.deepcopy(data))

    return datalist