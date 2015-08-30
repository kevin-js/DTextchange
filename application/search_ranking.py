from application import mongo_client

# search ranking algorithm by person name
def rank_by_name(parameters):
	name_matches = mongo_client.db.users.find({
		"first_name" : parameters[0]
	})
	return name_matches

# search ranking algorithm by book name
def rank_by_book(parameters):
	book_matches = mongo_client.db.books.find({

		})
	return None

# search ranking algorithm by course name
def rank_by_course(parameters):
	return None

