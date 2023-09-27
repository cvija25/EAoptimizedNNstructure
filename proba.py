import gym
import numpy

def simple_rule_policy(obs):
    pos = obs[0]
    print(pos)
    return 1 if pos > 0 else 3 

env = gym.make('LunarLander-v2',render_mode='human')
obs = env.reset()

totals = []
for episode in range(10):
    episode_rewards = 0
    obs = env.reset()[0]
    for step in range(400):
        action = simple_rule_policy(obs)
        print(action)
        obs, reward, terminated, truncated, info = env.step(action)
        episode_rewards += reward
        if terminated:
            break
    totals.append(episode_rewards)
print(totals)

#while True:
env.render()