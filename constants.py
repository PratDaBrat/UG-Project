X, Y = 15, 15    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.15         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
AGENTS = 1
FOOD = 2

EPISODES = 20000
MOVE_PENALTY = -50
ENEMY_PENALTY = -400
STAT_PENALTY = -200
FOOD_REWARD = 100

epsilon = 0.85
EPS_DECAY = 0.9999998

STATS_EVERY = 100
SHOW_EVERY = 6000
MAX_STEPS = 180

LEARNING_RATE = 0.11	 #0.2
DISCOUNT = 0.8
