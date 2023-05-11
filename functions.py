from mongodb import get_database

db =get_database() 
def get_watchlist(user_id):
    print(user_id)
    ss=db.get_collection('users_data').find_one({"id":user_id})
    watchlist=ss['watchlist']
    return watchlist

def add_watchlist(user_id, movie_id):
    ss=db.get_collection('users_data').find_one({"id":user_id})
    print(ss)
    watchlist=ss['watchlist']
    watchlist.append(movie_id)
    ss['watchlist']=watchlist
    print(ss)
    db.get_collection('users_data').replace_one({"id":user_id},ss)
    return {"msg":"data being ingested"}

    