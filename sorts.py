import copy

from config import n

def bubble(data):
    datalist = list()

    for i in range(n):
        for j in range(n-i-1):
            data[j][1] = 'red'
            data[j+1][1] = 'red'

            datalist.append(copy.deepcopy(data))

            if (data[j][0] > data[j+1][0]):
                data[j] , data[j+1] = data[j+1] , data[j]

            data[j][1] = 'white'
            data[j+1][1] = 'white'

    data[0][1] = 'white'
    data[1][1] = 'white'
    datalist.append(copy.deepcopy(data))

    return datalist