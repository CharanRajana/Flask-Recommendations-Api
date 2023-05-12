from flask import Flask, request, jsonify
from algo import hybrid
from functions import get_watchlist, add_watchlist

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'hello':'world'})

@app.route('/recommendations', methods=['POST'])
def recommendations():
    body = request.get_json()
    user_id = body.get('user_id')
    movie_name = body.get('movie_name')

    ans = hybrid(userId=user_id,titles=movie_name)
    print(ans)
    return jsonify(ans)

@app.route('/watchlist', methods=['POST'])
def watchlist():
    body = request.get_json()
    user_id = body.get('user_id')

    ans = get_watchlist(user_id)
    print(ans)
    return jsonify(ans)

@app.route('/watchlist/add', methods=['POST'])
def update_watchlist():
    body = request.get_json()
    user_id = body.get('user_id')
    movie_id = body.get('movie_id')

    ans = add_watchlist(user_id=user_id,movie_id=movie_id)
    print(ans)
    return jsonify(ans)


if __name__ == '__main__':
    app.run()