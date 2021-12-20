red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

sorts = []

# @sorts.append
def bubble(data):
    n = len(data)
    for i in range(n):
        for j in range(n-i-1):
            if(i):
                data[-i][1] = green
            data[j][1] = red
            data[j+1][1] = blue

            yield(data)

            if (data[j][0] > data[j+1][0]):
                data[j], data[j+1] = data[j+1], data[j]
                yield(data)

            data[j][1] = white
            data[j+1][1] = white

    data[0][1] = green
    data[1][1] = green
    yield(data)

# @sorts.append
def selection(data):
    n = len(data)
    for i in range(n-1):
        smallpos = i
        for j in range(i+1, n):
            if data[j][0] < data[smallpos][0]:
                smallpos = j
                
            data[i][1] = red
            data[j][1] = red
            data[smallpos][1] = blue

            yield(data)

            data[i][1] = white
            data[j][1] = white
            data[smallpos][1] = white

        data[i][1] = red
        data[smallpos][1] = blue

        data[i], data[smallpos] = data[smallpos], data[i]

        yield(data)

        data[smallpos][1] = white
        data[i][1] = green
    
    data[n-1][1] = green

    yield(data)

# @sorts.append
def insertion(data):
    n = len(data)
    data[0][1] = green

    for i in range(1, n):
        x = data[i][0]
        j = i-1
        data[i][1] = red
        yield(data)
        data[j+1][1] = green
        while(j>=0 and x<data[j][0]):
            data[j+1][0] = data[j][0]
            data[j] = [x, red]
            yield(data)
            data[j][1] = green
            j -= 1
        data[j+1][0] = x
    
    yield(data)
