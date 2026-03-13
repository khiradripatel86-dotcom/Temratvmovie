from pyrogram import Client, filters

API_ID = 35790707
API_HASH = "44753bcac8911c81028f009377368330"
BOT_TOKEN = "8779345278:AAGUeRRmEx0C2MP2q4xDmNQUVlcyh_GRRR4"

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Send file name.")

@app.on_message(filters.text)
async def search(client, message):
    await message.reply("Searching file...")

app.run()
