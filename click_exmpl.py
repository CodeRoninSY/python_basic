#!/usr/bin/env python
'''
click_exmpl.py
<2019-04-27> CodeRoninSY

'''

import click


def greeter(**kwargs):
    ''' greeter '''
    output = '{0}, {1}!'.format(kwargs['greeting'], kwargs['name'])
    if kwargs['caps']:
        output = output.upper()
    print(output)


@click.group()
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
