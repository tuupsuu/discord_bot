from multiprocessing import context
from pydoc import cli
from urllib import response
from discord.ext import commands
import discord # pip install discord.py # jos uudella koneella + asenna python
import random
import re

tiedosto = open("./token.dat")
TOKEN = tiedosto.read() # discord botin tokeni

# TODO lisää ohjeet ja lista niistä, niin helpompi tulostaa
help_ohjeet = '?!help = saadaksesi ohjeet tämän botin käyttöön'
help_ohjeet_en = '?!enghelp = to get manual in english'
random_ohjeet = '?!random = saadaksesi random numero, kirjoita "!random" ja jos haluat rajata ylärajaa, niin anna "!random" jälkeen : merkki ja numero ilman välilyöntejä'
ohje_lista = [help_ohjeet, random_ohjeet]

client = commands.Bot(command_prefix = "?!")

@client.event
async def on_ready():
    print('Kirjautunut sisään käyttäjänä {0.user}', format(client)) # kerrotaan kuka on kirjautunut sisään, ei näytä nimeä vielä oikein, TODO pitää korjata


@client.event
async def on_member_join(member):
    channel = client.get_channel(276421999247491072)
    await channel.send(f'Tervetuloa kanavalle {member}')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Tämä komento toimii vain äänikanavilla')

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Poistuttu äänikanavalta')
    else:
        await ctx.send('En ole äänikanavalla')

@client.command()
async def hello(ctx):
    username = str(ctx.message.author).split('#')[0]
    await ctx.send(f'Terve {username}!')

@client.command()
async def bye(ctx):
    username = str(ctx.message.author).split('#')[0]
    await ctx.send(f'Hei hei {username}!')

@client.command()
async def apua(ctx):
    await ctx.send('ei toimi vielä')

@client.command()
async def randomnum(ctx):
    teksti = str(ctx.message.content).split(' ')
    if len(teksti) == 1:
        numero = 1000000
        await ctx.send(f'Tässä sinun random numerosi: {random.randrange(numero)}')
    else:
        try:
            numero = int(teksti[1])
            await ctx.send(f'Tässä sinun random numerosi: {random.randrange(numero)}')
        except:
            numero = teksti[1]
            await ctx.send(f'"{numero}" ei ole positiivinen kokonaisluku')


'''@client.event
async def on_message(message):
    username = str(message.author).split('#')[0] # tallennetaan viestin laittajan nimi myöhempää käyttöä varten
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'botti':
        if re.match(r'\?!help.*', user_message.lower()): # ohjeet botin käyttöön
            await message.channel.send("ei toimi vielä")
            return
        elif re.match(r'\?!enghelp.*', user_message.lower()): # ohjeet botin käyttöön englanniksi
            await message.channel.send("no english support yet")
            return
        elif user_message.lower() == 'hello':
            await message.channel.send(f'Terve {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Hei hei {username}!')
            return
        elif re.match(r'\?!random.*', user_message.lower()):
            if re.match(r'\?!random([:]\d*)?$', user_message.lower()): # annetaan random numero ja jos eroteltu oma numero ":"-merkillä, niin annetaan random numero alle halutun numeron
                str_lista = user_message.split(':')
                if len(str_lista) > 1:
                    numero = int(str_lista[1])
                else:
                    numero = 1000000
                response = f'Tässä sinun random numerosi: {random.randrange(numero)}'
                await message.channel.send(response)
                return
            else:
                await message.channel.send('Virhe, anna komentu muodossa "!random" tai jos haluat rajata ylärajaa niin "!random:x", missä x on haluamasi numero')
                return
    
    if user_message.lower() == '!anywhere':
        await message.channel.send('Tätä voi käyttää missävain')
        return'''


client.run(TOKEN)