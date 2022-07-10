X,Y = 40, 40    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.05        #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 80

EPISODES = 3000
MOVE_PENALTY = -1
ENEMY_PENALTY = -100
STAT_PENALTY = -5
FOOD_REWARD = 10

epsilon = 0.85
EPS_DECAY = 0.998

SHOW_EVERY = 1
MAX_STEPS = 200

LEARNING_RATE = 0.7 #0.2
DISCOUNT = 0.95
