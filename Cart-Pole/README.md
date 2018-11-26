## Overview

### Details
* Name: CartPole-v0  
* Category: Classic Control
 * [Environment Page](https://gym.openai.com/envs/CartPole-v0)  

### Training
Clone the repository:
```
git clone https://github.com/GopiKishan14/Self_Balancing_Bot.git
```
Navigate to Cart-Pole directory and run the script:
```
cd Self_Balancind_Bot/Cart-Pole
python dqn_cartpole.py
```

### Description
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The pendulum starts upright, and the goal is to prevent it from falling over by increasing and reducing the cart's velocity.

### Source
This environment corresponds to the version of the cart-pole problem described by Barto, Sutton, and Anderson 


## Environment

### Observation
Type: Box(4)

Num | Observation | Min | Max
---|---|---|---
0 | Cart Position | -2.4 | 2.4
1 | Cart Velocity | -Inf | Inf
2 | Pole Angle | ~ -41.8&deg; | ~ 41.8&deg;
3 | Pole Velocity At Tip | -Inf | Inf

### Actions
Type: Discrete(2)

Num | Action
--- | ---
0 | Push cart to the left
1 | Push cart to the right

Note: The amount the velocity is reduced or increased is not fixed as it depends on the angle the pole is pointing. This is because the center of gravity of the pole increases the amount of energy needed to move the cart underneath it

### Reward
Reward is 1 for every step taken, including the termination step

### Starting State
All observations are assigned a uniform random value between ±0.05

### Episode Termination
1. Pole Angle is more than ±12°
2. Cart Position is more than ±2.4 (center of the cart reaches the edge of the display)
3. Episode length is greater than 200

### Solved Requirements
Considered solved when the average reward is greater than or equal to 195.0 over 100 consecutive trials.
