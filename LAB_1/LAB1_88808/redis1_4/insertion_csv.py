import redis
import csv
r = redis.Redis()


with open('nomes-registados-2018.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        r.zadd("N_names",{row[0].strip("\n"):row[2]})

            

