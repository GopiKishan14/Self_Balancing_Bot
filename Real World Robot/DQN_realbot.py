
import numpy as np
import random
import tensorflow as tf
import matplotlib.pyplot as plt
import balance_bot
import random
#env=gym.make('balancebot_v0')

from env_robo import env_robo_class
import tensorflow.contrib.slim as slim
env=env_robo_class()
from collections import deque
class Memory:
    
    def __init__(self, buffer_size = 60000):
        self.buffer = []
        self.buffer_size = buffer_size
    
    def add(self,experience):
        if len(self.buffer) + len(experience) >= self.buffer_size:
            self.buffer[0:(len(experience)+len(self.buffer))-self.buffer_size] = []
        self.buffer.extend(experience)
    
    def sample(self,size):
        
        
        return np.reshape(np.array(random.sample(self.buffer,size)),[size,5])

class Q_Network():
    def __init__(self ,learning_rate=0.0008,
                 state_size=3,
                 action_size=9,
                 hidden_size=16,
                 name='QNetwork'):
        
        self.inputs = tf.placeholder(shape=[None,state_size],dtype=tf.float32)
        self.actions=tf.placeholder(dtype=tf.int32,shape=[None])
        
        self.Temp = tf.placeholder(shape=None,dtype=tf.float32)
        
        self.actions_onehot=tf.one_hot(self.actions,action_size,dtype=tf.float32)
        self.fc1 = tf.layers.dense(self.inputs , hidden_size , activation=tf.nn.relu , kernel_initializer=tf.contrib.layers.xavier_initializer()) #, kernel_regularizer=tf.contrib.layers.l2_regularizer(0.01))
        self.fc2 = tf.layers.dense(self.fc1, hidden_size , activation=tf.nn.relu , kernel_initializer=tf.contrib.layers.xavier_initializer())
        
        self.Q_out = tf.layers.dense(self.fc2 , action_size , activation=None)
        
        self.predict = tf.argmax(self.Q_out,1)
        
        self.Q_dist = tf.nn.softmax(self.Q_out/self.Temp)
        
        #Below we obtain the loss by taking the sum of squares difference between the target and prediction Q values.
        
        
        
        self.Q = tf.reduce_sum(tf.multiply(self.Q_out, self.actions_onehot), reduction_indices=1)
        
        self.nextQ = tf.placeholder(shape=[None,9],dtype=tf.float32)
        self.loss = tf.reduce_sum(tf.square(self.nextQ - self.Q_out))
        self.updateModel = tf.train.AdamOptimizer(learning_rate).minimize(self.loss)


gamma = .995 #Discount factor.
num_episodes = 30000 #Total number of episodes to train network for.
batch_size = 32 #Size of training batch
startE = 1 #Starting chance of random action
endE = .08 #Final chance of random action
anneling_steps = 600000 #How many steps of training to reduce startE to endE.
pre_train_steps = 9000
tf.reset_default_graph()
q_net = Q_Network()
#target_net = Q_Network()
init = tf.initialize_all_variables()
trainables = tf.trainable_variables()

jList = []

rList = []

mem=Memory()

saver=tf.train.Saver()
with tf.Session() as sess:
    sess.run(init)
    
    #    saver = tf.train.import_meta_graph("Self_Balancing_Bot/balancebot-project/model_fukc.ckpt")
    #    saver.restore(sess,tf.train.latest_checkpoint('./'))
    #
    
    
    e = startE
    stepDrop = (startE - endE)/anneling_steps
    total_steps = 0
    
    for i in range(num_episodes):
        s = env.reset()#call your function""
#        s=np.array([0.,0.,0.]) do a motor action to give a velocity and stand again to middle then get the actual position
""" """
    print (i)
    rAll = 0
        d = False
        j = 0
        while j < 1500:
            j+=1
            
            
            #Choose an action probabilistically, with weights relative to the Q-values.
            Q_d,allQ = sess.run([q_net.Q_dist,q_net.Q_out],feed_dict={q_net.inputs:[s],q_net.Temp:e})
            a = np.random.choice(Q_d[0],p=Q_d[0])
            a = np.argmax(Q_d[0] == a)
            
            #Get new state and reward from environment
            s1,r,d,_ = env.step(a)
            
            mem.add(np.reshape(np.array([s,a,r,s1,d]),[1,5]))
            
            if e > endE and total_steps > pre_train_steps:
                e -= stepDrop
            
            if total_steps > pre_train_steps and total_steps % 2 == 0:
                #Double-DQN training algorithm
                trainBatch = mem.sample(batch_size)
                Q1 = sess.run(q_net.predict,feed_dict={q_net.inputs:np.vstack(trainBatch[:,3])})
                Q2 = sess.run(q_net.Q_out,feed_dict={q_net.inputs:np.vstack(trainBatch[:,3])})
                Q3=sess.run(q_net.Q_out,feed_dict={q_net.inputs:np.vstack(trainBatch[:,0])})
                end_multiplier = -(trainBatch[:,4] - 1)
                doubleQ = Q2[range(batch_size),Q1]#max acc. to my model
                
                targetQ = trainBatch[:,2] + (gamma*doubleQ * end_multiplier)
                
                for (i,j)in zip(range(batch_size),trainBatch[:,1]):
                    Q3[i,j]=targetQ[i]
                #                Q3[range(batch_size),np.array(trainBatch[:,1])]=targetQ
                
                _ = sess.run(q_net.updateModel,feed_dict={q_net.inputs:np.vstack(trainBatch[:,0]),q_net.nextQ:Q3})
            
            
            s=s1
            rAll += r
            
            total_steps += 1
            if d == True:
                break
            jList.append(j)
            rList.append(rAll)
    if i % 50 == 0 and i != 0:
        r_mean = np.mean(rList[-100:])
        
        
            print("Mean Reward: " + str(r_mean) + " Total Steps: " + str(total_steps) + " t: " + str(e)+"episode:"+str(i))
        
        if i%10==0:
            
            save_path = saver.save(sess, "hello")

