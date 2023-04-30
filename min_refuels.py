def min_refills(distance, tank, stops):
    # write your code here
    refuel = 0
    curr_tank  = tank
    #i = 0
    prev_stop = 0
    #print(stops)
    stops.append(distance)
    #print(stops)
    for i in range(len(stops)-1):
        dist = stops[i] - prev_stop
        #print(dist)
        curr_tank = curr_tank - dist
        if curr_tank < 0:
            return -1
        if dist <= tank and (stops[i+1]-stops[i]) > curr_tank:
            curr_tank = tank
            refuel+=1
            #print(refuel,stops[i])
        prev_stop = stops[i]
        if i == (len(stops)-2):
            if stops[i+1] - prev_stop > curr_tank:
                return -1
    return refuel


l = [100,200,300,400]
res = min_refills(700,200, l)
print(res)
