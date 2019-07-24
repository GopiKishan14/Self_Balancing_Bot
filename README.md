# Self Balancing Bot
```
This project aimes at stabalising a two wheeled robot (naturally in unequilibrium)
using Reinforcement Learning.
It is completed under the guidance and mentorship of Artificial Intelligence 
and Electronic Society(ArIES) of IIT Roorkee.
```

## Description
This project is completed under two phases.
1. Software Phase
2. Hardware Phase

### Sofware Phase
In this phase, a vitual bot is created using ROS URDF by defining its body structure, 
joints and their degree of freedom. PyBullet is used to simulate physics (gravity, friction, etc.)
The checkboard environment is selected as default env. in pyBullet. The simulation is
made accordingly to match real world scenerio (like g=9.8m/s^2)
Q-learning is used as Learning algorithm for the agent implemented using deep Q-Network, a
deep neural network.

### Hardware Phase
After software phase, a trained weights is obtained to be deployed and fine tuned in the real world.
Two 12V DC motors are used of 18000 RPM is used in wheels.L298N motor driver is used for DC motor control.
MPU-9250 is used for sensing purposes. <br/>
It has two chips: <br/>
* *The MPU-6500, which contains a 3-axis gyroscope, a 3-axis accelerometer, and a Digital Motion Processor* <br/>
* *The AK8963, a 3-axis digital compass.* <br/>
<br/>
Raspberry pi3 B+ model is used as motherboard with rasbian as operating system. All codes are written in python3

## Installation and Set Up

## Testing

## Learning Experience (Take Aways)

## Learning Resources

## Feedback

All kinds of feedback (code style, bugs, comments etc.) is welcome. Please open an [*Issue*](https://github.com/GopiKishan14/Self_Balancing_Bot/issues) on this Repository.

## Contribution Guidelines

If you are familiar with basics of contributing to github repositories, feel free to skip this section. For total beginners who landed up here, before contributing, take a look at the [blog-post](https://channelcs.github.io/best-practices-in-a-collaborative-environment.html) to get started. Peace out!
