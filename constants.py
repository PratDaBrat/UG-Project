X, Y = 10, 10    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 2

EPISODES = 3500
MOVE_PENALTY = -5
ENEMY_PENALTY = -30
STAT_PENALTY = -40
FOOD_REWARD = 100

epsilon = 0.65
EPS_DECAY = 0.9998

STATS_EVERY = 100
SHOW_EVERY = STATS_EVERY
MAX_STEPS = 150

LEARNING_RATE = 0.2	 #0.2
DISCOUNT = 0.95
