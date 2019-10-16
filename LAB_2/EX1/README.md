# Bases de Dados de Documentos

  

## 2.1 MongoDB – Instalação e exploração por linha de comandos

### Advantages of MongoDB over RDBMS
-   **Schema less** − MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.
    
-   Structure of a single object is clear.
    
-   No complex joins.
    
-   Deep query-ability. MongoDB supports dynamic queries on documents using a document-based query language that's nearly as powerful as SQL.
    
-   Tuning.
    
-   **Ease of scale-out** − MongoDB is easy to scale.
    
-   Conversion/mapping of application objects to database objects not needed.
    
-   Uses internal memory for storing the (windowed) working set, enabling faster access of data.

### Why Use MongoDB?
-   **Document Oriented Storage** − Data is stored in the form of JSON style documents.
    
-   Index on any attribute
    
-   Replication and high availability
    
-   Auto-sharding
    
-   Rich queries
    
-   Fast in-place updates
    
-   Professional support by MongoDB

### Where to Use MongoDB?
-   Big Data
-   Content Management and Delivery
-   Mobile and Social Infrastructure
-   User Data Management
-   Data Hub


### Tutorial

Create a database:

    use DATABASE_NAME
To check your currently selected database:

    db
To check your databases list:
```
>show dbs
local     0.78125GB
test      0.23012GB
```
To display our database we need to insert at least one document first:

```
>db.movie.insert({"name":"tutorials point"})  >show dbs local  0.78125GB mydb 0.23012GB test 0.23012GB
```

To drop a database you first need to switch to it with:

    use mydb
Then use the command:

    db.dropDatabase()

Collections are created automatically when you insert a new document but if you want to create one this are the commands:
```
db.createCollection(name,options)
```

To insert a document:
```
use mydb
db.post.insert([  { title:  'MongoDB Overview', description:  'MongoDB is no sql database',  by:  'tutorials point', url:  'http://www.tutorialspoint.com', tags:  ['mongodb',  'database',  'NoSQL'], likes:  100  },  { title:  'NoSQL Database', description:  "NoSQL database doesn't have tables",  by:  'tutorials point', url:  'http://www.tutorialspoint.com', tags:  ['mongodb',  'database',  'NoSQL'], likes:  20, comments:  [  { user:'user1', message:  'My first comment', dateCreated:  new  Date(2013,11,10,2,35), like:  0  }  ]  }  ])
```
To find a document use:
```
db.getCollection('movies').find({}).pretty()
```

 1. Query Document:

Equality operator:
```
db.getCollection('movies').find({"by":"tutorials point"}).pretty()
```

Lesser than and lesser than equals:

 ```
 db.getCollection('movies').find({"likes":{$lt:50}}).pretty()

db.getCollection('movies').find({"likes":{$lte:50}}).pretty()
```

Greater than and Greater than equals:

 ```
 db.getCollection('movies').find({"likes":{$gt:50}}).pretty()

db.getCollection('movies').find({"likes":{$gte:50}}).pretty()
```

Not equals:

 ```
db.getCollection('movies').find({"likes":{$ne:50}}).pretty()
```

And operator:

 ```
db.getCollection('movies').find({$and:[{"likes":{$ne:50}},{"title": "MongoDB Overview"}]}).pretty()
```

Or operator:
 ```
db.getCollection('movies').find({"likes":  {$gt:10},$or:[{"likes":{$ne:50}},{"title": "MongoDB Overview"}]}).pretty()
```

1. Update Document:

Equality operator:
```
db.getCollection('movies').find({"by":"tutorials point"}).pretty()
```

Lesser than and lesser than equals:

 ```
 db.getCollection('movies').find({"likes":{$lt:50}}).pretty()

db.getCollection('movies').find({"likes":{$lte:50}}).pretty()
```

Greater than and Greater than equals:

 ```
 db.getCollection('movies').find({"likes":{$gt:50}}).pretty()

db.getCollection('movies').find({"likes":{$gte:50}}).pretty()
```

Not equals:

 ```
db.getCollection('movies').find({"likes":{$ne:50}}).pretty()
```

And operator:

 ```
db.getCollection('movies').find({$and:[{"likes":{$ne:50}},{"title": "MongoDB Overview"}]}).pretty()
```

Or operator:
 ```
db.getCollection('movies').find({"likes":  {$gt:10},$or:[{"likes":{$ne:50}},{"title": "MongoDB Overview"}]}).pretty()
```

 2. Update Documents

```
db.movies.update({'title':'MongoDB Overview'},{$set:{'title':'New MongoDB Overview'}})
```

 3. Aggregation
This query agregates all the data and groups by the field "by" displaying how many entries are associated with the "by" id
```
db.movies.aggregate([{$group : {_id : "$by", num_tutorial : {$sum : 1}}}])
```
