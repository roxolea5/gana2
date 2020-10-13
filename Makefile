run: 
	python3 webserver.py

build:
	cd ./web && npm install && cd ..
	
start:
	cd ./web && npm start && cd ..
