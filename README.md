# plico_motor
client of a motor controlled under the plico environment 


 ![Python package](https://github.com/ArcetriAdaptiveOptics/plico_motor/workflows/Python%20package/badge.svg)
 [![codecov](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor/branch/main/graph/badge.svg?token=ApWOrs49uw)](https://codecov.io/gh/ArcetriAdaptiveOptics/plico_motor)
 [![Documentation Status](https://readthedocs.org/projects/plico_motor/badge/?version=latest)](https://plico_motor.readthedocs.io/en/latest/?badge=latest)
 [![PyPI version](https://badge.fury.io/py/plico-motor.svg)](https://badge.fury.io/py/plico-motor)


plico_motor is an application to control motors under the [plico][plico] environment.

[plico]: https://github.com/ArcetriAdaptiveOptics/plico


## Installation ##
Note: it is recommended, before installing packages, to create a conda environment to work.

```
conda create --name myenv
```

To create an environment with a specific python version

```
conda create --name myenv python=3.7
```

To activate you environment

```
conda activate myenv
```

### On server
On the server machine you install plico_motor_server with the following command

```
pip install plico_motor_server
```

This command also installs a server configuration file that needs to be modified. The file is located at 'yourLocalPath/plico_motor_server/plico_motor_server/conf/plico_motor_server.conf' and contains ip address 
and port number of your motor. There are three types of motor indicated with motor1, motor2 and motor3: this number is 
to be used to start the corresponding server.

The plico_motor_server package installs also the client package.

## On client
On the client machine

```
pip install plico_motor
```

## Usage

### Starting Servers
```
plico_motor_server_n
```
where n indicates the number of the server you want to start in according to what is declared in the configuration file.

### Using the client module 

In a python terminal on the client computer:

```
from plico_motor import motor
....to be continued!
```
