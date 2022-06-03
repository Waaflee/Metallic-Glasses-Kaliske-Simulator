# Metallic-Glasses-Kaliske-Simulator
Backend and example client application for Metallic Glass simulations using Kaliske and Robert (1997) propposed numerical method

## Requirements

 - [Pipenv](https://pypi.org/project/pipenv/)

## Setup

Setup env and dependencies
`pipenv shell`
`pipenv install`

## Run

inside pipenv shell run:

init server:
`python app.py`

run plotter client:

`python plotter.py`

## Troubleshooting

if the following error arises:

`Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.`

make sure you have [tkinter](https://docs.python.org/3/library/tkinter.html) installed
