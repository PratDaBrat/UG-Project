X, Y = 10, 10    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
AGENTS = 1
FOOD = 2

EPISODES = 6000
MOVE_PENALTY = -50
ENEMY_PENALTY = -400
STAT_PENALTY = -200
FOOD_REWARD = 100

epsilon = 0.65
EPS_DECAY = 0.999998

STATS_EVERY = 100
SHOW_EVERY = 3000
MAX_STEPS = 180

LEARNING_RATE = 0.2	 #0.2
DISCOUNT = 0.85
