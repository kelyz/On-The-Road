from app import app

if __name__ == "__main__":
	app.secret_key = os.environ['app.secret_key']
	app.run(debug = True)