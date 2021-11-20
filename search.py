import click
import requests


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
    for current in result_dict['docs']:
        print("Title: ", current['title'])


if __name__ == "__main__":
    get_book_title()
