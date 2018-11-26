# Deep Reinforcement Learning for Keras
[![Build Status](https://api.travis-ci.org/keras-rl/keras-rl.svg?branch=master)](https://travis-ci.org/keras-rl/keras-rl)
[![Documentation](https://readthedocs.org/projects/keras-rl/badge/)](http://keras-rl.readthedocs.io/)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/keras-rl/keras-rl/blob/master/LICENSE)
[![Join the chat at https://gitter.im/keras-rl/Lobby](https://badges.gitter.im/keras-rl/Lobby.svg)](https://gitter.im/keras-rl/Lobby)

<table>
  <tr>
    <td><img src="/assets/breakout.gif?raw=true" width="200"></td>
    <td><img src="/assets/cartpole.gif?raw=true" width="200"></td>
    <td><img src="/assets/pendulum.gif?raw=true" width="200"></td>
  </tr>
</table>

## What is it?

`keras-rl` implements some state-of-the art deep reinforcement learning algorithms in Python and seamlessly integrates with the deep learning library [Keras](http://keras.io).

Furthermore, `keras-rl` works with [OpenAI Gym](https://gym.openai.com/) out of the box. This means that evaluating and playing around with different algorithms is easy.

Documentation is available [online](http://keras-rl.readthedocs.org).


## Installation

- Install Keras-RL from Pypi (recommended):

```
pip install keras-rl
```

- Install from Github source:

```
git clone https://github.com/GopiKishan14/Self_Balancing_Bot.git
cd Self_Balancing_Bot/Cart-Pole
python setup.py install
```

## Examples

If you want to run the examples, you'll also have to install:
- **gym** by OpenAI: [Installation instruction](https://github.com/openai/gym#installation)
- **h5py**: simply run `pip install h5py`


Once you have installed everything, you can try out a simple example:
```bash
python examples/dqn_cartpole.py
```
This is a very simple example and it should converge relatively quickly, so it's a great way to get started!
It also visualizes the game during training, so you can watch it learn. How cool is that?

Some sample weights are available on [keras-rl-weights](https://github.com/matthiasplappert/keras-rl-weights).

If you have questions or problems, please file an issue or, even better, fix the problem yourself and submit a pull request!

## Citation

```bibtex
@misc{plappert2016kerasrl,
    author = {Matthias Plappert},
    title = {keras-rl},
    year = {2016},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/keras-rl/keras-rl}},
}
```

## References
1. *https://backyardrobotics.eu/*
6. *Continuous Deep Q-Learning with Model-based Acceleration*, Gu et al., 2016
10. *Reinforcement learning: An introduction*, Sutton and Barto, 2011
