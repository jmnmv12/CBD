import redis
r = redis.Redis()
#Insert full names for auto-complete search
with open("female-names.txt") as file:
    for line in file:
        r.set(line.strip("\n"),"")
        

