# project-template ![](https://github.com/moskomule/project-template/workflows/test/badge.svg)

Template for my research projects using Python

```
.github/test.yaml       # pytest and yamllint
.gitignore
notebooks               # Jupyter notebooks
script                  # Shell scripts for running experiments
src                     # Root of main codes
tests                   
  - requirements.txt    # Requirements for pytest
README.md               # This file
```

## Requirements

I usually use conda to create virtual environments.

```
conda create -n ${PROJECT_NAME} python=...
conda activate ${PROJECT_NAME}
```

### For unit tests

```
pip install pytest
pytest
```

## Training

```
python train.py ...
```

## Evaluation

...

## Results

...

## Pre-training Models

...
