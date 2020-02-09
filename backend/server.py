from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/addface', methods=['POST'])
def post_addFace():
  return "Nice man"

@api.route('/getface', methods=['POST'])
def post_getFace():
  return "Nice face"

if __name__ == '__main__':
    api.run()