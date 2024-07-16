install-deps: deps
	pip-sync requirements.txt

deps:
	python -m pip install --upgrade pip pip-tools
	pip-compile --output-file requirements.txt --resolver=backtracking pyproject.toml