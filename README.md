# BigData Technical Interview Question

## Overview

This repository contains the solution for the BigData Technical Interview Question.

Using Spark via PySpark, the following tasks are implemented:

- Task 1: Exploratory Data Analysis
- Task 2: Recommender System Design
- Task 3: Text Analysis as NLP Task

## Datasets

- Source Datasets must be under Datasets folder

  - Movielens-small.db (for Task 1-2)
  - Large Movie Review Dataset_v1 as aclImdb_v1.tar.gz | Download link: [Large Movie Review Dataset v1.0](http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz) (for Task 3)

  - All the extraction and implementation has been done with pipelines. No additional action needed.

## Requirements

create a virtual environment

```bash
python3 -m venv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

deactivate virtual environment

```bash
deactivate
```

make sure to give execution permission to the script

```bash
sudo chmod +x install_spark.py
```

run the install_spark.py script first

```bash
sudo ./install_spark.py
```

Then run the juptyer notebook for the task
