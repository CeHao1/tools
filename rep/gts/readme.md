# Basic setting and running

## initialize and set car/ course type
from gym_gts import GTSApi  
with GTSApi(ip="192.168.124.34") as gts_api:  
  num_cars=1,  
  tires="SH",  
  car_codes=3298,  
  bops={"enable": True, "power": 105, "weight": 100},  
  course_code=351  
  
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
