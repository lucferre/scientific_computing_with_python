import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        [self.contents.extend([x]*y) for (x, y) in kwargs.items()]
    def draw(self, n):
        balls_drawn = []
        if n <= len(self.contents):
            for i in range(n):
                ball_drawn = random.choice(self.contents)
                self.contents.remove(ball_drawn)
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''Performs a probability experiment.
    
    Arguments:
    -hat: object
    -expected_balls: dictionary that contains the colors and times they are to be extracted
    -num_balls_drawn: number of balls to draw out in each experiment
    -num_experiments
    
    Return:
    -float (probability)
    '''
    m = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        # For each experiment, draw out a sample of n balls from the hat
        balls_drawn = hat_copy.draw(num_balls_drawn)
        match = True
        for key, value in expected_balls.items():
            # if there are less balls of at least one color than indicated in expected_balls,
            # turn match to False and continue to next experiment
            if balls_drawn.count(key) < value:
                match = False
                continue
        if match:
            m += 1
    return m/num_experiments