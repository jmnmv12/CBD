import redis
r = redis.Redis()

# Pushing all users
txt =input("Search for ('Enter' for quit):") #FIXME change to normal input
if(txt!=''):
    for user in sorted(r.keys(txt+"*")):
        print(str(user,'utf-8'))
else:
    print("Bye Bye!!")