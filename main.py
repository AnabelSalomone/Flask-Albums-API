from flask import Flask
from flask_restful import Api, Resource, reqparse
import uuid
import csv

app = Flask(__name__)
api = Api(app)

# Req Parser
album_args = reqparse.RequestParser()
album_args.add_argument("name", type=str, required=True, help="Name needed")
album_args.add_argument("band", type=str, required=True, help="Band name needed")
album_args.add_argument("year", type=int)

class Album(Resource):
  def put(self):
    album_id = str(uuid.uuid4())
    args = album_args.parse_args()

    with open("albums.csv", "a") as f:
      writer = csv.writer(f)
      writer.writerow([album_id, args.name, args.band, args.year])

    return "Album created", 201

api.add_resource(Album, "/album")

if __name__ == "__main__":
  app.run(debug=True)