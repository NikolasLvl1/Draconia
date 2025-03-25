import discord
import os
from dotenv import load_dotenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
const keep_alive = require(`./keep_alive.js`);

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Configurar intents del bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Inicializar el scheduler
scheduler = AsyncIOScheduler()


@client.event
async def on_ready():
    print(f'✅ Bot conectado como {client.user}')
    scheduler.start()


# Función para enviar mensaje diario con un contenido diferente dependiendo de la hora
async def send_daily_message(message):
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message)


# Agregar tarea recurrente a las 01:00 UTC con un mensaje específico
scheduler.add_job(send_daily_message,
                  "cron",
                  hour=1,
                  minute=0,
                  timezone="UTC",
                  args=["@here<@&1352065515798925410> ¡BOSS WORLD 🚨."])

# Agregar tarea recurrente a las 06:00 UTC con un mensaje etiquetando un rol
scheduler.add_job(send_daily_message,
                  "cron",
                  hour=23,
                  minute=28,
                  timezone="UTC",
                  args=["@here<@&1352065515798925410> ¡Fiesta de Brigada 🚨."])

# Agregar tarea recurrente a las 12:00 UTC con un mensaje específico
scheduler.add_job(send_daily_message,
                  "cron",
                  hour=15,
                  minute=42,
                  timezone="UTC",
                  args=["@here<@&1352065515798925410> ¡BOSS WORLD 🚨."])
# Agregar tarea recurrente a las 12:00 UTC con un mensaje específico
scheduler.add_job(send_daily_message,
                  "cron",
                  hour=9,
                  minute=0,
                  timezone="UTC",
                  args=["@here<@&1352065515798925410> ¡RESET LISTO 🚨."])
# Ejecutar el bot
client.run(TOKEN)
