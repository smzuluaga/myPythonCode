# https://www.codewars.com/kata/57675f3dedc6f728ee000256/solutions/python
# Build Tower Advanced - Build Tower by the following given arguments: 
# number of floors (integer and always greater than 0)
#block size (width, height) (integer pair and always greater than (0, 0))

def tower_builder(f, block_size):
    w, h = block_size[0], block_size[1]
    pattern =[]
    
    def floor_builder(floor):
        for i in range (1, h+1):
            if floor == 1:
                pattern.append('{}'.format(('*' * w).center(w+((f-1)*(w*2)))))
            if floor > 1:
                pattern.append('{}'.format(('*' * (pattern[-h].count('*')+(w*2))).center(w+((f-1)*(w*2)))))
                 
    for j in range(1,f+1):
        floor_builder(j)
    return pattern


print(tower_builder(3,(4,2)))
""" print(tower_builder(6,(2,1))) """