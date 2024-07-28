# Click CLI Application Template

This is a Python CLI application built using the Click library. The application demonstrates various features of Click, including commands, options, arguments, file handling, nested commands, and interactive mode.

[//]: # (Author Links)
[![Author](https://img.shields.io/badge/Author-Jonathan%20Hoffman-blue.svg)](https://www.linkedin.com/in/jonathan-hoffman-b5839195/)

## Installation

To use this CLI application, you need to have Python installed. You can install the Click library using pip:

```bash
pip install click
```

## Usage

```shell
❯ python main.py --help       
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  This is the main CLI group.

Options:
  --help  Show this message and exit.

Commands:
  config        Configuration related commands.
  greet         Greet a person a specified number of times.
  process-file  Read from INPUT file and write to OUTPUT file.
  shell         Run a shell interface.
  status        Check the status of the system.

```

```shell
❯ python main.py config --help
Usage: main.py config [OPTIONS] COMMAND [ARGS]...

  Configuration related commands.

Options:
  --help  Show this message and exit.

Commands:
  get  Get a configuration value.
  set  Set a configuration value.
```

```shell
❯ python main.py greet --help 
Usage: main.py greet [OPTIONS] NAME

  Greet a person a specified number of times.

Options:
  --count INTEGER  Number of greetings.
  --uppercase      Convert greeting to uppercase.
  --help           Show this message and exit.
```

```shell
❯ python main.py process-file --help
Usage: main.py process-file [OPTIONS] INPUT OUTPUT

  Read from INPUT file and write to OUTPUT file.

Options:
  --uppercase  Convert file content to uppercase.
  --help       Show this message and exit.
```

```shell
❯ python main.py shell --help       
Usage: main.py shell [OPTIONS]

  Run a shell interface.

Options:
  --interactive  Enable interactive mode.
  --help         Show this message and exit.
```

```shell
❯ python main.py status --help
Usage: main.py status [OPTIONS]

  Check the status of the system.

Options:
  --verbose  Enables verbose mode.
  --help     Show this message and exit.
```
