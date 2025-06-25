import os
import time
import discord

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

token = os.getenv('TOKEN')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_update_time = 0

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author != self.user:
            current_time = time.time()
            if current_time - self.last_update_time < 180: 
                return

            if len(message.content) > 32:
                parts = message.content.split()
                new_name = ''
                for part in parts:
                    if len(new_name) + len(part) + 1 <= 32:
                        new_name += f"{part} "
                new_name = new_name.strip()
            else:
                new_name = message.content
            
            await self.user.edit(global_name=new_name)
            self.last_update_time = current_time

client = MyClient()
client.run(token)