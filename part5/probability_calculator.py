import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if sum(value for key,value in kwargs.items()) == 0:
            print('0 balls so not possible to initialize')
            return None
        self.contents = [f'{key}' for key, value in kwargs.items() for _ in range(value)]
    
    def draw(self, n):
        list = []
        if n > len(self.contents):
            list = copy.deepcopy(self.contents[:])
            self.contents.clear()
            return list

        for _ in range(n):
            self.contents.remove(removed := random.choice(self.contents))
            list.append(removed)
        return list[:]
    
    def __str__(self):
        return f'{self.contents}'
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expecteddraw = [f'{key}' for key, value in expected_balls.items() for _ in range(value)]
    M=0
    for _ in range(num_experiments):
        value = True
        balsltodraw = copy.deepcopy(hat)
        drawnballs = balsltodraw.draw(num_balls_drawn)
        for ball in expecteddraw:
            try:
                drawnballs.remove(ball)
            except:
                value = False
                break
        if(value):
            M+=1 
    return M/num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)