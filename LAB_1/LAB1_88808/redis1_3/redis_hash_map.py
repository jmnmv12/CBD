import redis
r = redis.Redis()

# Pushing all users
users=["Ana","Pedro","Maria","Luis"]
idades=[19,18,20,56]
for idx,val in enumerate(users):

    r.hmset("USERS:"+str(idx),{"name":val,"idade":idades[idx]})

for idx,val in enumerate(users):
    print (r.hgetall("USERS:"+str(idx)))