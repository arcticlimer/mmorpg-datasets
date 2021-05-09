#!/usr/bin/env python3

import utils

from client import Client
from secrets import HYPIXEL_API_KEY

DATA_DIRECTORY = 'data/hypixel_skyblock'
BASE_API = 'https://api.hypixel.net'

async def run(session):
    client = Client(BASE_API, session)

    current_players = await client.get('/counts', parse=True, params={"key": HYPIXEL_API_KEY})
    bazaar_data     = await client.get('/skyblock/bazaar')
    auctions_data   = await client.get('/skyblock/auctions')
    skills          = await client.get('/resources/skyblock/skills')
    collections     = await client.get('/resources/skyblock/collections')

    current_skyblock_players = client.json_to_string(current_players["games"]["SKYBLOCK"])

    timestamp = utils.timestamp()
    path = f'{DATA_DIRECTORY}/{timestamp}'

    await utils.write_json(path, 'bazaar',      bazaar_data)
    await utils.write_json(path, 'auctions',    auctions_data)
    await utils.write_json(path, 'players',     current_skyblock_players)
    await utils.write_json(path, 'skills',      skills)
    await utils.write_json(path, 'collections', collections)
