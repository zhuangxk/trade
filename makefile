dev:
	export FLASK_APP=app.py
	export FLASK_ENV=development
	flask run

deploy:
	cd ./vue && npm i && npm run build
	# gunicorn -w 4 -b 0.0.0.0:5000 app:app >> app.log

docker_build:
	docker build -t flask_vue:1.0 .
docker_run:
	docker run -it --name=flask_app -p 5000:5000 flask_vue:1.0