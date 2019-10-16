import redis
import re
r = redis.Redis()

# Pushing all users
txt = input("Search for ('Enter' for quit):")
if(txt!=''):

    
   
    keys = r.zrange("N_names", desc=True, start=0, end=-1)
    keys = [str(key, 'utf-8') for key in keys if re.search(f"^{txt}", str(key, 'utf-8'))]
    for key in keys:
        print(key)

   


       
else:
    print("Bye Bye!!")