import click


@click.group()
def cli():
    """This is the main CLI group."""
    pass


@cli.command()
@click.argument("name")
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--uppercase", is_flag=True, help="Convert greeting to uppercase.")
def greet(name, count, uppercase):
    """Greet a person a specified number of times."""
    for _ in range(count):
        greeting = f"Hello, {name}!"
        if uppercase:
            greeting = greeting.upper()
        click.echo(greeting)


@cli.command()
@click.argument("input", type=click.File("r"))
@click.argument("output", type=click.File("w"))
@click.option("--uppercase", is_flag=True, help="Convert file content to uppercase.")
def process_file(input, output, uppercase):
    """Read from INPUT file and write to OUTPUT file."""
    content = input.read()
    if uppercase:
        content = content.upper()
    output.write(content)
    click.echo(f"Processed {input.name} and wrote to {output.name}.")


@cli.command()
@click.option("--verbose", is_flag=True, help="Enables verbose mode.")
def status(verbose):
    """Check the status of the system."""
    if verbose:
        click.echo("Verbose mode enabled.")
    click.echo("System status is OK.")


@cli.group()
def config():
    """Configuration related commands."""
    pass


@config.command()
@click.option("--key", prompt="Config key", help="Configuration key to set.")
@click.option("--value", prompt="Config value", help="Configuration value to set.")
def set(key, value):
    """Set a configuration value."""
    click.echo(f"Setting {key} to {value}")
    # Logic to set the configuration


@config.command()
@click.argument("key")
def get(key):
    """Get a configuration value."""
    # Logic to get the configuration
    value = "some_value"  # Placeholder for the actual logic
    click.echo(f"{key} is set to {value}")


@cli.command()
@click.option("--interactive", is_flag=True, help="Enable interactive mode.")
def shell(interactive):
    """Run a shell interface."""
    if interactive:
        click.echo("Entering interactive mode...")
        while True:
            cmd = input("> ")
            if cmd == "exit":
                break
            click.echo(f"You entered: {cmd}")
    else:
        click.echo("Running in non-interactive mode.")


if __name__ == "__main__":
    cli()
