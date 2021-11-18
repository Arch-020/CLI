import click
import requests


# @click.group()
# def openlib():
#    '''
#    Command to manage subset of commands
#   '''
#    pass


@click.command()
@click.option('--name', prompt='Book name',
              help='Book name to get the title.')
def get_book_title(name):
    '''
    Gets the book title
    '''
    name = name.replace(" ", "+")
    result = requests.get(
        f"http://openlibrary.org/search.json?q={name}")

    result_dict = result.json()
    click.echo(f"Title: {result_dict['docs'][0]['title']}")


# openlib.add_command(get_book_title())


if __name__ == "__main__":
    get_book_title()
