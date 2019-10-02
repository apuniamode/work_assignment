	from pymongo import MongoClient

	#Insert is User_details
	def insert_User(age,gender,weight,BMI):
					try:
							database = MongoClient('127.0.0.1:27017')
							db = database.assignment
							result=db.user_details.insert({"age": age,"gender":gender,"weight":weight,"BMI":BMI})
							print('Record succsfully insert',result)
					except pymongo.errors.ConnectionFailure as e::
							print (e)

	#Insert in Airtical Datasat
	def insert_airtical(artical_title,artical_conatct,age_group,category="all"):
					try:
							database = MongoClient('127.0.0.1:27017')
							db = database.assignment
							result=db.airtical_details.insert({ "artical" :{ "title" : artical_title, "content" :artical_conatct }, "age_group" : age_group, "category" : category })
							print('Record succsfully insert',result)
					except pymongo.errors.ConnectionFailure as e:
							print (e)



