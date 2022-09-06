# [project-template](https://moskomule.github.io/project-template) ![](https://github.com/moskomule/project-template/workflows/test/badge.svg)

Template for my research projects using PyTorch

```
.github/test.yaml       # pytest and yamllint
.gitignore
notebooks               # Jupyter notebooks
script                  # Shell scripts for running experiments
src                     # Root of main codes
tests
README.md               # This file
```

## Requirements

I usually use conda to create virtual environments for PyTorch.

```
conda create -n ${PROJECT_NAME} python=3.10
conda activate ${PROJECT_NAME}
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

### For unit tests

```
pip install -U hatch
hatch run tests:pytest
```

### For building documents

```
pip install -U hatch
hatch run docs:build
```

## Training

...

## Evaluation

...

## Results

...

## Pre-training Models

...
