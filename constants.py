X, Y = 12, 12    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.2         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 3

EPISODES = 6000
MOVE_PENALTY = -50
ENEMY_PENALTY = -400
STAT_PENALTY = -200
FOOD_REWARD = 100

epsilon = 0.65
EPS_DECAY = 0.9999998

STATS_EVERY = 50
SHOW_EVERY = 2000
MAX_STEPS = 120

LEARNING_RATE = 0.2	 #0.2
DISCOUNT = 0.85
