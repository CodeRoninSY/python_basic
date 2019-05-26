#!/usr/bin/env python
'''
click_exmpl.py
<2019-04-27> CodeRoninSY

'''

import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def greeter(**kwargs):
    ''' greeter '''
    output = '{0}, {1}!'.format(kwargs['greeting'], kwargs['name'])
    if kwargs['caps']:
        output = output.upper()
    print(output)


@click.group()
def cli():
    """ cli group """
    pass


@cli.command()
def colordemo():
    """ Demonstrates ANSI color support. """
    for color in 'red', 'green', 'blue':
        click.echo(click.style('colored %s' % color, fg=color))
        click.echo(click.style('background color %s' % color, bg=color))


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
def greet():
    ''' Greet '''
    pass


@greet.command()
@click.argument('name')
@click.option('--greeting', default='Hello', help='word to use for the greeting')
@click.option('--caps', is_flag=True, help='uppercase the output')
def hello(**kwargs):
    ''' hello '''
    greeter(**kwargs)


@greet.command()
@click.argument('name')
@click.option('--greeting', default='Goodbye', help='word to use for the greeting')
@click.option('--caps', is_flag=True, help='uppercase the output')
def goodbye(**kwargs):
    ''' goodbye '''
    greeter(**kwargs)


if __name__ == "__main__":
    greet()
