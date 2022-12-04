input = [0,0,4]

climbed_per_day = input[0] 
fell_per_night = input[1]      
Height = input[2] 
days = 0
net_climbed_per_day = (climbed_per_day) - (fell_per_night)


def snail_climbed():
    if climbed_per_day == Height: # if the initial height is equal to one days worth
            time = Height/climbed_per_day
            return print(int(time))
    while net_climbed_per_day > 0:
        time = Height/net_climbed_per_day
        if time > 0:
            return print(int(time))
    return print("FAIL")
            
#snail_climbed()


def snail_climbing():
    distance = climbed_per_day
    time = 1
    if net_climbed_per_day > 0:
        while distance < Height:
            distance += net_climbed_per_day
            time += 1
        return print(int(time))
    else:
        return print('Fail')
#hello again 


def snail_climbing1():
    distance = climbed_per_day
    time = 1
    if net_climbed_per_day > 0:
        while distance < Height:
            distance += net_climbed_per_day
            time += 1
        return print(int(time))
    else:
        return print('Fail')



def median_arrays():
    arr1 = [1,3,5,8]
    arr2 = [2,4,6]
    arr_comb = arr1 + arr2
    arr_comb.sort()
    number_of_terms = int((len(arr_comb))) 
    if number_of_terms % 2 == 0:
        term1 = int((number_of_terms) /2)
        term2 = term1 + 1
        median = (arr_comb[term1-1] + arr_comb[term2-1]) / 2
    else:
        term = int((number_of_terms) / 2) + 1
        median = arr_comb[term-1]  
    return print(median)


def reverse_string():

    #str = "hello world"
    #str = str[::-1]

    #str = "hello world"
    #rev = ""
    #for i in reversed(str)
    #rev += i


    
    #return print(rev)


    example_str = "Hello World!"
    reversed_str = ""
    for i in reversed(example_str):
        reversed_str += i

    return print(reversed_str)


def Knapsack():

    val = [50,100,150,200]
    wt = [8,16,32,40]
    W = 64
    



    return

def test():
    array = [2,3,4,5,6,7,8,9]
    x = array[0:8]

    return print(x1)
test()




