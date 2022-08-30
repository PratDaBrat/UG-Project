X,Y = 10, 10    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.05        #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 3

EPISODES = 1000
MOVE_PENALTY = -2
ENEMY_PENALTY = -10
STAT_PENALTY = -20
FOOD_REWARD = 100

epsilon = 0.75
EPS_DECAY = 0.9998

STATS_EVERY = 100
SHOW_EVERY = 100
MAX_STEPS = 100

LEARNING_RATE = 0.2 #0.2
DISCOUNT = 0.95
