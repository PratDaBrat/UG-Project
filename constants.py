X,Y = 15, 15    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.05        #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 10

EPISODES = 1000
MOVE_PENALTY = -1
ENEMY_PENALTY = -100
STAT_PENALTY = -5
FOOD_REWARD = 10

epsilon = 0.85
EPS_DECAY = 0.998

SHOW_EVERY = 1
MAX_STEPS = 50

LEARNING_RATE = 0.3 #0.2
DISCOUNT = 0.95
