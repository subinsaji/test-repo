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

    arr1 = [1,3,5]
    arr2 = [2,4,6]

    arr_comb = arr1 + arr2
    arr_comb.sort()


    median_term = len(arr_comb)/2

    if median_term % 2 == 0:
        term1 = arr_comb[len(arr_comb)/2]
        term2 = arr_comb[(len(arr_comb)/2) + 1]
        median = (term1+term2)/2

    else:
        median = arr_comb[len(arr_comb)]

    return print(median)

median_arrays()

