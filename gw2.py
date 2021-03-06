#!/usr/bin/env python3

import asyncio

import utils
from client import Client


DATA_DIRECTORY = 'data/gw2'
BASE_API = 'https://www.gw2spidy.com/api/v0.9'


async def run(session):
    client = Client(BASE_API, session)

    items = await client.get('/json/all-items/all')
    gem_price = await client.get('/json/gem-price')
    recipes = await client.get('/json/all-recipes/all')

    timestamp = utils.timestamp()
    path = f'{DATA_DIRECTORY}/{timestamp}'

    await utils.write_json(path, 'gem_price',    gem_price)
    await utils.write_json(path, 'items_market', items)
    await utils.write_json(path, 'recipes',      recipes)
