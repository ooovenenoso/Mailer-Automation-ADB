import os
import discord
import requests
import time
import datetime
import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://spreadsheets.google.com/feeds']
SERVICE_ACCOUNT_FILE = 'credentials.json'

# use creds to create a client to interact with the Google Drive API
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, SCOPES)
gspread_client = gspread.authorize(creds)

intents = discord.Intents.all()
intents.guilds = False
intents.members = False
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('/sendout'):
        await message.channel.send("Ingrese el mensaje a enviar:")
        user_message = ""
        while len(user_message) == 0:
            message_input = await client.wait_for('message', check=lambda message: message.author == message.author, timeout=120)
            user_message = message_input.content.strip()
        message_to_send = user_message

        url = "https://docs.google.com/spreadsheets/d/SHEET-URL-HERE"
        sh = gspread_client.open_by_url(url)
        worksheet = sh.get_worksheet(0)
        list_of_hashes = worksheet.get_all_values()

        for row in list_of_hashes[1:]:
            phone = row[0]
            adb_command = f"adb shell am startservice --user 0 -n com.android.shellms/.sendSMS -e contact {phone} -e msg \"{message_to_send}\""
            os.system(adb_command)
            print(f"Mensaje enviado a {phone}")
        await message.channel.send('Mensajes enviados exitosamente')

client.run('DISCORD-BOT-API')
