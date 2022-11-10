install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

post-install:
# 	python -m textblob.download_corpora

format:
#	black *.py mylib/*.py

lint:
#	pylint --disable=R,C *.py mylib/*.py

test:
#	python -m pytest -vv --cov=mylib --cov=main test_*.py

build:
#	docker build -t deploy-fastapi .

# run:
# 	#run docker
	
deploy:
# 	#pushes container to ECR
# 	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 894437926398.dkr.ecr.us-east-2.amazonaws.com
# 	docker build -t wiki-fastapi .
# 	docker tag wiki-fastapi:latest 894437926398.dkr.ecr.us-east-2.amazonaws.com/wiki-fastapi:latest
# 	docker push 894437926398.dkr.ecr.us-east-2.amazonaws.com/wiki-fastapi:latest

all: install post-install lint test deploy