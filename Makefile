clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip3 install -e .[dev] --upgrade --no-cache

format:
	black -l 88 **/*.py

install:
	pip3 install git+https://github.com/WesleySteve/ve.io-generate-database-sqlite.git
	pip3 install -r requirements.txt
	pip3 install .

install_dev:
	pip3 install git+https://github.com/WesleySteve/ve.io-generate-database-sqlite.git
	pip3 install -r requirements.txt
	pip3 install -e .["dev"]

uninstall:
	pip3 uninstall ve.io-upload_data

uninstall-deps:
	pip3 uninstall ve.io-generate-database-sqlite


up:
	docker-compose up -d

down:
	docker-compose down
