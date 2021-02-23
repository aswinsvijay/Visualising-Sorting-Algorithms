import copy

from main import n

#bubble sort
def bubble(data):
    for i in range(n):
        for j in range(n-i-1):
            if(i):
                data[-i][1] = 'green'
            data[j][1] = 'red'
            data[j+1][1] = 'blue'

            yield(data)

            if (data[j][0] > data[j+1][0]):
                data[j] , data[j+1] = data[j+1] , data[j]
                yield(data)

            data[j][1] = 'white'
            data[j+1][1] = 'white'

    data[0][1] = 'green'
    data[1][1] = 'green'
    yield(data)

#selection sort
def selection(data):
    for i in range(n-1):
        smallpos = i
        for j in range(i+1,n):
            if data[j][0] < data[smallpos][0]:
                smallpos = j
                
            data[i][1] = 'red'
            data[j][1] = 'red'
            data[smallpos][1] = 'blue'

            yield(data)

            data[i][1] = 'white'
            data[j][1] = 'white'
            data[smallpos][1] = 'white'

        data[i][1] = 'red'
        data[smallpos][1] = 'blue'

        data[i] , data[smallpos] = data[smallpos] , data[i]

        yield(data)

        data[smallpos][1] = 'white'
        data[i][1] = 'green'
    
    data[n-1][1] = 'green'

    yield(data)

#insertion sort
def insertion(data):
    data[0][1] = 'green'

    for i in range(1,n):
        x = data[i][0]
        j = i-1
        data[i][1] = 'red'
        yield(data)
        data[j+1][1] = 'green'
        while(j>=0 and x<data[j][0]):
            data[j+1][0] = data[j][0]
            data[j] = [x,'red']
            yield(data)
            data[j][1] = 'green'
            j -= 1
        data[j+1][0] = x
    
    yield(data)
