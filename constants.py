X,Y = 50, 50    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1        #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 10

EPISODES = 5000
MOVE_PENALTY = -1
ENEMY_PENALTY = -20
STAT_PENALTY = -5
FOOD_REWARD = 5

epsilon = 0.85
EPS_DECAY = 0.998

SHOW_EVERY = 200
MAX_STEPS = 500

# LEARNING_RATE = 0.2
DISCOUNT = 0.95
