# AirBnB Clone - The Console
This is an enhancement over the [command-line implementation](https://github.com/MartyOfMCA/AirBnB_clone_v2) of the AirBnB project. This project focuses on an implementation of a REST API to help data transfer. This project ws created as part of our course requirement at ALX.

## Features
This project adds the following features:
* REST API

## Concepts
This project is based on the following:
* MySQL
* Python Flask Framework
* ORM
* SQLAlchemy
* Environment variables in Python
* REST API

## Prerequisites
All tooling version mentioned should be noted as the minimum version requirement. Additional tool needed alongside [previous tools](https://github.com/MartyOfMCA/AirBnB_clone_v2#prerequisites) include:
* Pip version 20 [Download](https://pypi.org/project/pip/)
* Flask version 3.0.0 [Download](https://pypi.org/project/Flask/)

## How To's
### Starting the command-line interpreter
The command-line tool can be started from any terminal on any of the supported OS. Use the following snippet to start the program in the interactive mode:

`./console.py`

This will start the command-line interface showing a prompt. This signals that the tool is ready to process the commands the user provides infinitely until the user chooses to end the session.

The tool can also be started in the non-interactive mode using the following snippet:

`echo "help" | ./console.py`

### Using the command-line interpreter
After starting the tools you can perform diverse operations directly from the command-line interface.
You can type `help` to see a list of all the available commands. You can also obtains information on how to use any of the listed commands using the following snippet:

`help command_name`

### Examples
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
create  help	add  change  quit

Undocumented commands:
======================
(hbnb) help create
```
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```
