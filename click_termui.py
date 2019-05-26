#!/usr/bin/env python
'''
click_termui.py
<2019-04-28> CodeRoninSY

'''

import math
import time
import random
import click


try:
    range_type = xrange
except NameError:
    range_type = range


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


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


@cli.command()
def pager():
    """ Demonstrates using the pager. """
    lines = []
    for x in range_type(200):
        lines.append('%s. Hello World!' % click.style(str(x), fg='green'))
    click.echo_via_pager('\n'.join(lines))


@cli.command()
@click.option('--count', default=8000, type=click.IntRange(1, 100000),
              help='The number of items to process.')
def progress(count):
    """Demonstrates the progress bar."""
    items = range_type(count)

    def process_slowly(item):
        time.sleep(0.002 * random.random())

    def filter(items):
        for item in items:
            if random.random() > 0.3:
                yield item

    with click.progressbar(items, label='Processing accounts',
                           fill_char=click.style('#', fg='green')) as pbar:
        for item in pbar:
            process_slowly(item)

    def show_item(item):
        if item is not None:
            return 'Item #%d' % item

    with click.progressbar(filter(items), label='Committing transaction',
                           fill_char=click.style('#', fg='yellow'),
                           item_show_func=show_item) as pbar:
        for item in pbar:
            process_slowly(item)

    with click.progressbar(length=count, label='Counting',
                           bar_template='%(label)s %(bar)s | %(info)s',
                           fill_char=click.style('#', fg='cyan'),
                           empty_char=' ') as pbar:
        for item in pbar:
            process_slowly(item)

    with click.progressbar(length=count, width=0, show_percent=False,
                           show_eta=False,
                           fill_char=click.style('#', fg='magenta')) as pbar:
        for item in pbar:
            process_slowly(item)

    # nonlinear progress bar
    steps = [math.exp(x * 1. / 20) - 1 for x in range(20)]
    count = int(sum(steps))
    with click.progressbar(length=count, show_percent=False,
                           label='Slowing progress bar',
                           fill_char=click.style(u'█', fg='green')) as pbar:
        for item in steps:
            time.sleep(item)
            pbar.update(item)


@cli.command()
def menu():
    """Shows a simple menu."""
    menu = 'main'
    while 1:
        if menu == 'main':
            click.echo('Main menu:')
            click.echo('    d: debug menu')
            click.echo('    q: quit')
            char = click.getchar()
            if char == 'd':
                menu = 'debug'
            elif char == 'q':
                menu = 'quit'
            else:
                click.echo('Invalid input')
        elif menu == 'debug':
            click.echo('Debug menu')
            click.echo('*****Do something here*****')
            click.echo('    b: back')
            char = click.getchar()
            if char == 'b':
                menu = 'main'
            else:
                click.echo('Invalid input')
        elif menu == 'quit':
            return


if __name__ == "__main__":
    cli()
