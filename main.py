from urllib import response
import discord
import random
import re

TOKEN = 'OTc2OTA3MDUxMzUzNjQwOTYw.GpV6MR.Z6CuE2rLdTqSp5O82XN0-4FM04B2Wm_7GozezA' # discord botin tokeni

# TODO lisää ohjeet ja lista niistä, niin helpompi tulostaa
help_ohjeet = '?!help = saadaksesi ohjeet tämän botin käyttöön'
help_ohjeet_en = '?!enghelp = to get manual in english'
random_ohjeet = '?!random = saadaksesi random numero, kirjoita "!random" ja jos haluat rajata ylärajaa, niin anna "!random" jälkeen : merkki ja numero ilman välilyöntejä'
ohje_lista = [help_ohjeet, random_ohjeet]

client = discord.Client()

@client.event
async def on_ready():
    print('Kirjautunut sisään käyttäjänä {0.user}', format(client)) # kerrotaan kuka on kirjautunut sisään, ei näytä nimeä vielä oikein

@client.event
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
        return


client.run(TOKEN)