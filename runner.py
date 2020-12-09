import gym


env = gym.make("FetchPickAndPlace-v1")
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()
