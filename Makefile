install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# post-install:
# 	python -m textblob.download_corpora

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py

build:
	docker build -t data-eng-api .

# run:
# 	#run docker
	
deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 854733302685.dkr.ecr.us-east-1.amazonaws.com
	docker build -t ids_706_de_api .
	docker tag ids_706_de_api:latest 854733302685.dkr.ecr.us-east-1.amazonaws.com/ids_706_de_api:latest
	docker push 854733302685.dkr.ecr.us-east-1.amazonaws.com/ids_706_de_api:latest

all: install lint test deploy