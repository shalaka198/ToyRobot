# Toy Robot App

## Pre-requisites
1. python 3.8.2 installed


## Running the App
By default, config is setup to pickup development environment settings.

### Option 1: Console
(To run in production settings, setup envionment variable PY_ENV=production)
1. In terminal, navigate to directory containing Dockerfile. In this project navigate to ToyRobotSolution directory
2. Run python command in the terminal
`python .\start.py`

### Option 2: Container
(To build production container, update Dockerfile variable pyenv_value=production)
1. Navigate to directory containing Dockerfile. In this project navigate to ToyRobotSolution directory

2. Build image
`docker build -t toyrobot .`

3. Run the container in interactive mode
`docker run --name robot -p 5000:80 -it toyrobot`

4. After exiting the app, if you want to start the container again, use
`docker start -i robot`


## Running Tests
1. In terminal, navigate to directory containing Dockerfile. In this project navigate to ToyRobotSolution directory
2. Run python command in the terminal
`python .\start_tests.py`


## Assumptions
- User input is not constrained to be uppercase
- User input can include whitespace; my app removes whitespace and capitalises instruction before proceeding to next steps
- Wherever user provides invalid instruction, my app ignores it
- Board is considered to be square and dimension is set to 5 but this is configurable in config file


## Improvements
- Could separate static validate methods in command handler to CommandValidator class. In this case, it is small simple method, hence manageable
- Environment variables could be setup in deployment scripts, depending on deployment environment test/uat/prod, we can add config files.
- Fuzzy matching commands - we could provide user with suggestion if they are "close" to correct command eg. someone enters "MOEV", we could suggest "Did you mean MOVE?"