import redis
r = redis.Redis()

class person:
    def __init__(self,username,name):
        self.name=name
        self.username=username

print("Welcome to Redis Message Server")

user_name=input("Insert username: ")
name=input("Insert your first and last name: ")
my_person=person(user_name,name)
#print(my_person.name)

r.hset("RedisMS:"+my_person.username,"name",my_person.name)
options="1)Send message;\n2)Check messages;\n3)Follow users;\n4)Quit;\n"
opt=input(options)
while opt!="4":
    if(opt=="1"):
        message=input("Message to send: ")
        r.lpush("RedisMSmessageList:"+my_person.username,message)
    elif(opt=="2"):
        following=r.hget("RedisMS:"+my_person.username,"following")
        if(following is None):
            print("Não está a seguir ninguem atualmente.Experimente seguir alguém.")
        else:
            following_formated= str(following,'utf-8')
            following_list=following_formated.split(";")
            for user in following_list:
                message_list=r.lrange("RedisMSmessageList:"+user,0,-1)
                print("--Mensagens do "+user+" :")
                message_list_formated=[ str(msg,'utf-8') for msg in message_list]
                for msg in message_list_formated:
                    print("- "+msg)

                


    elif(opt=="3"):
        all_users=r.keys("RedisMS:*")
        print("--Users Available--")
        all_users_formated=[ str(user,'utf-8')[8:] for user in all_users]
        for user in all_users_formated:
            if(user!=my_person.username):
                print(user)
        message=input("Insert the username of the person you want to follow: ")
        following=r.hget("RedisMS:"+my_person.username,"following")
        if(following is None):
            r.hset("RedisMS:"+my_person.username,"following",message)
        else:
            #print(following)
            following_formated= str(following,'utf-8')
            following_list=following_formated.split(";")
            if(message in following_list):
                print("You already follow this user!")
            
            else:
                following_formated+=";"+message
                r.hset("RedisMS:"+my_person.username,"following",following_formated)
            
        #print(all_users)
    opt=input(options)



