setup:
	pip install -r requirements_dev.txt

test:
	python -m unittest

build-dist:
	python setup.py sdist

upload-pypi: build-dist
	twine upload dist/*

upload-pypitest: build-dist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
