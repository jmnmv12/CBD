import redis
r = redis.Redis()
r.flushdb()

# Pushing all users
users=["Ana","Pedro","Maria","Luis","Joao"] #FIXME See encoding
for s in users:

    r.lpush("USERS",s.encode("utf-8"))

#Reading all keys
keys_redis=r.keys("*")
for k in keys_redis:
    print ("All keys: "+str(k,'utf-8'))

#Reading all members of USERS
users_members=r.lrange("USERS",0,-1)
for k in users_members:
    print ("Members of USERS: "+str(k,'utf-8'))