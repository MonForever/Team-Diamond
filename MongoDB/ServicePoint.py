
import pymongo

# connect to mongodb from python using pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
# open the database
dbname = client['CarRental']
#print (dbname)
# get the collection
collection_name = dbname["ServicePoint1"]
#print(collection_name)
dbname.c
# get the data from the collection
item_details = collection_name.find()
#print(item_details)
#for row in item_details:
   #print(row” }})
#collection_name.find( [  { "CITY": 1, "Availcar": { "$subtract": [ "$TotalNumberOfCars", "$NumberOfActiveBookings" ]  } }  ] )

#print the Service point with full bookings

xy=collection_name.find( {
"CarsAvailable" : { "$eq" : 0}
                },{"CITY":1})
print(xy)
for k in xy:
    print(k)














