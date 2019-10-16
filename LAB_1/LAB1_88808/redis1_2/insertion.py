my_dict={}

with open("female-names.txt") as file:
    for line in file:
        line=line[0].upper()
        if(line not in my_dict):
            my_dict[line]=0
        
        my_dict[line]+=1
        
            
with open("initials4redis.txt", "w") as f:
    for key,value in my_dict.items():   
        f.write(" SET "+key+" "+str(value)+"\n") 
