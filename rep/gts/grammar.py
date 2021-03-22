# Basic setting and running

## initialize and set car/ course type

from gym_gts import GTSApi
with GTSApi(ip="192.168.124.34") as gts_api:
  num_cars=1,
  gts_api.set_race(
    tires="SH",
    ar_codes=3298,
    bops={"enable": True, "power": 105, "weight": 100},
    course_code=351
  )
  
  
  
  # other settings
if car_name == 'ttcoup':  
  car_codes = 3298  
  bops={"enable": True, "power": 105, "weight": 100}  
elif car_name == 'mazda':  
  car_codes=2148  
  bops=[{"enable": False, "power": 100, "weight": 100, "slot": car_id}  
  for car_id in range(num_cars)]  
elif car_name == 'demio':   
  car_codes=3383  
  bops=[{"enable": True, "power": 124, "weight": 119, "slot": car_id}  
for car_id in range(num_cars)]

if track_name == 'fuji':  
  course_code = 837  
elif track_name == 'tokyo':  
  course_code = 351  
elif track_name == 'brands':  
  course_code = 119  

## interact with gym
import gym
from gym_gts import StepSendingTimeoutException, StepPerceptionTimeoutException

num_simulations = 1000000000

with gym.make(
    'gym_gts:gts-v0', 
    ip="192.168.124.34",  # TODO: set your PlayStation's IP-address
    #done_function=example_done_function, 
    #reward_function=example_reward_function,
    min_frames_per_action=1
) as env:
  
  # pick observations
    env.feature_keys = ['lap_count','pos', 'rot','velocity', 'angular_velocity',
            'current_lap_time_msec','frame_count', 'course_v',  'steering', 'throttle', 'brake','is_hit_wall',
            'shift_position','front_g','side_g','vertical_g', 'course_off_time', 'slip_angle', ] #keep slip angle at the end
    env.standardize_observations = False
    max_off_course = 2 # maximum time (s) off course before simulation is ended
    
    for simulation in range(num_simulations):
      sum_ob=[]
      observations = env.reset()
      # get states
      # observations[0],env.feature_keys
      for t in range(20000):  
            try:
            observations, rewards, dones, info = env.step([[steer,thr]])
            
            sum_ob.append(observations)
            
            if t%100==0:
                    print('time step',t)
                
            except (StepSendingTimeoutException, StepPerceptionTimeoutException):
                print("TIMEOUT")
                
                
                
                
