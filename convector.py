# -*- coding: utf-8 -*-

import click

from convectors import ConvectorINI


@click.command()
@click.argument('path_to_file')
@click.option('--indent', default=2, help='number of indent json')
def main(path_to_file: str, indent: int = 2):
    """
    Convert ini file to json.

    :param path_to_file: path to .ini file
    :param indent: number of indent
    :return: json
    """
    convector = ConvectorINI(path_to_file)
    click.echo(convector.dumps(indent))


if __name__ == '__main__':
    main()
