import gym
import numpy as np

env = gym.make("FetchReach-v1")
for i in range(100):
    print("---------------------------------------- New Env Set ")
    env.reset(target_in_the_air=True, target_range=0.05, distance_threshold=.2)
    next_obs = None
    done = False
    reward_sum = 0
    while not done:
        obs = next_obs
        action = env.action_space.sample()
        env.render()
        next_obs, reward, done, info = env.step(action)
        reward_sum += reward
        if done:
            print(action, reward, done)
            print(info)
            print("===================================================== Total reward", reward_sum)
            print()
            break

env.close()

'''
""Initializes a new Fetch environment.

        Args:
            model_path (string): path to the environments XML file
            n_substeps (int): number of substeps the simulation runs on every call to step
            gripper_extra_height (float): additional height above the table when positioning the gripper
            block_gripper (boolean): whether or not the gripper is blocked (i.e. not movable) or not
            has_object (boolean): whether or not the environment has an object
            target_in_the_air (boolean): whether or not the target should be in the air above the table or on the table surface
            target_offset (float or array with 3 elements): offset of the target
            obj_range (float): range of a uniform distribution for sampling initial object positions
            target_range (float): range of a uniform distribution for sampling a target
            distance_threshold (float): the threshold after which a goal is considered achieved
            initial_qpos (dict): a dictionary of joint names and values that define the initial configuration
            reward_type ('sparse' or 'dense'): the reward type, i.e. sparse or dense
        """
'''
