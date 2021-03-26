from flask import Flask
import database
import models

app = Flask(__name__)

# Create a database with the correct models.


@app.route('/')
def hello_world():
  database.Base.metadata.create_all(database.postgres_engine)
  return 'Hello World'


if __name__ == '__main__':
  app.run()
