import gym
import gym_connect_four
import time
from gym_connect_four import RandomPlayer, ConnectFourEnv
env = gym.make("ConnectFour-v0")



""" 
action = 0
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)

action = 1
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)

action = 2
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)

action = 3
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)

action = 4
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)

action = 5
state = env.reset()
next_state, reward, done, info = env.step(action)
print(action, next_state)
""" 

def swap_payers(current_player):
    if current_player == 1:
        return -1
    return 1

player_1 = 0
player_2 = 0
for episode in range(100):
    print("Episode ", episode)
    if episode % 2 == 0:
        current_player = 1
    else:
        current_player = -1

    episode_reward = 0
    state = env.reset()
    while True:
        action = env.action_space.sample()
        # import pdb; pdb.set_trace()
        next_state, reward, done, info = env.step(action)
        episode_reward += reward
        #env.render()
        #time.sleep(1)
        state = next_state
        current_player = swap_payers(current_player) 
        #print("reward ", reward)
        if done:
            if current_player == -1:
                player_1 += 1
            else:
                player_2 +=1
            #print("current player", current_player)
            #print("episode reward ", episode_reward)
            break


print("player 1: {} player 2: {} ".format(player_1, player_2))



