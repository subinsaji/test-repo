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



snail_climbing()