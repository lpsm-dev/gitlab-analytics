.PHONY: clean python-packages install run all

# =============================================================================
# PYTHON
# =============================================================================

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . -type d -name __pycache__ -delete

python-packages:
	pip3 install -r requirements.txt

install: python-packages

run:
	python3 code/main.py

all: clean install run
