import numpy
from test_mpu import MPU6050
from time import sleep
from ctrl_motor import motor_ctrl

class env_robo_class:
    def __init__(self):
        self.mpu = MPU6050()
        self.compute_action = motor_ctrl()
        self.pitch , self.Gx = 0,0
        self.speed = 0
        self.vd=0
    def observation_space(self,act):
        self.pitch , self.Gx = mpu.observation()
        self.speed= compute_action.controller(act)
        
        return np.array([[self.pitch, self.Gx, self.speed]])
    def step(self,act):
        state=self.observation_space(act)
        reward=self._compute_reward()
        done = self._compute_done()
        self._envStepCounter += 1
        
        return state,reward,done,{}
    
    def _compute_reward(self):
        
        # could also be pi/2 - abs(cubeEuler[0])
        return (1 - self.pitch) * 0.1 -  abs(self.speed - self.vd) * 0.01
    def _compute_done(self):
        # Adjust according to optimal pitch
        return self.pitch> .9 or self._envStepCounter >= 1500
    def reset(self):
        self.vt = 0
        self.speed = 0
        self._envStepCounter = 0
        self.pitch , self.Gx = 0,0


