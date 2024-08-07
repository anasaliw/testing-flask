from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
account=os.getenv("ACCOUNT_SID")


app = Flask(__name__)

@app.route('/')
def hello_world():
	return f'Hello World! {account}'

if __name__ == "__main__":
	app.run(host='0.0.0.0')
