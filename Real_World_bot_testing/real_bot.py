import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.optimizers import Adam
from ctrl_motor import motor_ctrl
#from rl.agents.dqn import DQNAgent
#from rl.policy import BoltzmannQPolicy
#from rl.memory import SequentialMemory
from test_mpu import MPU6050
from time import sleep 
#import balance_bot

#ENV_NAME = 'balancebot-v0'

# Get the environment and extract the number of actions.
#env = gym.make(ENV_NAME)+
#np.random.seed(123)
#env.seed(123)
#nb_actions = env.action_space.n
nb_actions = 9

model = Sequential()
model.add(Flatten(input_shape=(1,) + (3,)))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

# Finally, we configure and compile our agent. You can use every built-in Keras optimizer and
# even the metrics!

model.load_weights('new/dqn_balancebot-v0_weights_solvedstable3.0_stand.h5f')

env = MPU6050()
compute_action = motor_ctrl()
speed = 0

while(True):
    pitch , Gx = env.observation()
    action = model.predict(np.array([[[pitch, Gx, speed]]]))
    print(action)
    act = np.argmax(action)
    print(act)
    speed = compute_action.controller(act)
    print("speed " , speed)
    sleep(0.04)
    
