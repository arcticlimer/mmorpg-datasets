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

    first_recipe = await client.get('/json/recipes/*all*', parse=True)
    last_page = first_recipe['last_page']
    coroutines = (client.get(f'/json/recipes/*all*/{i}', parse=True)
                  for i in range(2, last_page + 1))

    recipes = await asyncio.gather(*coroutines)
    recipes_str = client.json_to_string(recipes)

    timestamp = utils.timestamp()
    path = f'{DATA_DIRECTORY}/{timestamp}'

    await utils.write_json(path, 'gem_price',    gem_price)
    await utils.write_json(path, 'items_market', items)
    await utils.write_json(path, 'recipes',      recipes_str)
