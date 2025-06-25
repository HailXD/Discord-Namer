import os
import discord

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

token = os.getenv('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author != self.user:
            
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

client = MyClient()
client.run(token)