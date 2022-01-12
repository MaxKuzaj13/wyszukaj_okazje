from discordwebhook import Discord
from decouple import config


discord = Discord(url=config('webhook'))
