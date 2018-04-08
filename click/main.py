import click

from commands import network

@click.group()
def main():
    pass


if __name__ == '__main__':
    main.add_command(network.network)
    main()
