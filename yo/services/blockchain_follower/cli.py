#! /usr/bin/env python
# -*- coding: utf-8 -*-


import click
import yo.yolog

@click.command(name='follower')
@click.option('--database_url', envvar='DATABASE_URL')
@click.option('--dpayd_url', envvar='DPAYD_URL',
              default='https://api.dpays.io')
@click.option('--start_block', envvar='START_BLOCK',default=None)
def yo_blockchain_follower_service(database_url, dpayd_url, start_block):
    from yo.services.blockchain_follower.service import main_task
    main_task(database_url=database_url,
              dpayd_url=dpayd_url,
              start_block=start_block)


if __name__ == "__main__":
    yo_blockchain_follower_service()
