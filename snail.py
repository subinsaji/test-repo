input = [3,4,3]

climbed_per_day = input[0] 
fell_per_night = input[1]      
Height = input[2] 
days = 0
net_climbed_per_day = climbed_per_day-fell_per_night


def snail_climbed():


    while net_climbed_per_day > 0:
        
        time = Height/net_climbed_per_day
        

        if climbed_per_day == Height:
            return print("1")

        elif time > 0:
            return print(time)

        
    return print("FAIL")


snail_climbed()