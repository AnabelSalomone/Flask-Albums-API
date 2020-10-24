from flask import Flask
from flask_restful import Api, Resource, reqparse
import uuid
import csv

csv_file = "albums.csv"

app = Flask(__name__)
api = Api(app)

# Req Parser
album_args = reqparse.RequestParser()
album_args.add_argument("name", type=str, required=True, help="Name needed")
album_args.add_argument("band", type=str, required=True, help="Band name needed")
album_args.add_argument("year", type=int)

class Album(Resource):
  def get(self, album_name):
    with open(csv_file, "r") as f:
      for row in csv.reader(f):
        if row[1] == album_name:
          return row
      return f'{album_name} was not found'
  
  def put(self, album_name):
    # Adds a random id
    album_id = str(uuid.uuid4())
    args = album_args.parse_args()

    with open(csv_file, "a") as f:
      writer = csv.writer(f)
      writer.writerow([album_id, args.name, args.band, args.year])

    return "Album created", 201

api.add_resource(Album, "/album/<string:album_name>")

if __name__ == "__main__":
  app.run(debug=True)