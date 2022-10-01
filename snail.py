
input = [3,2,11]

climbed_per_day = input[0] 
fell_per_night = input[1]      
Height = input[2] 
days = 0
net_climbed_per_day = climbed_per_day-fell_per_night


def snail_climbed():
    
    time = Height/(net_climbed_per_day)

