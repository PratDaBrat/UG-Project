X,Y = 10, 10    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.01        #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 3

EPISODES = 20000
MOVE_PENALTY = -1
ENEMY_PENALTY = -100
STAT_PENALTY = -5
FOOD_REWARD = 10

epsilon = 0.85
EPS_DECAY = 0.998

SHOW_EVERY = 100
MAX_STEPS = 60

LEARNING_RATE = 0.3 #0.2
DISCOUNT = 0.95
