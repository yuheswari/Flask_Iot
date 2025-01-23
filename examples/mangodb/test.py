from pymongo import MongoClient                        
client=MongoClient('mongodb://yuheswari:Asuk_2627@mongodb.selfmade.ninja:27017/?authSource=users')
db=client.yuheswari_iotcloud
#db=client['yuheswari_iotcloud'] alternative way to access the database
result=db.test.find_one({"username":"uk"})
print(result)
