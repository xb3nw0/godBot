import discord
import os
import openai
import asyncio

# Set your OpenAI API key
openai.api_key = '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'

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

 # Check if the bot is mentioned
    if client.user.mentioned_in(message):
        response = openai.Completion.create(
            engine="davinci", 
            prompt=message.content,
            max_tokens=100
        )
        if response.choices:
            bible_quote = response.choices[0].text.strip()
            await message.channel.send(bible_quote)
        else:
            await message.channel.send("You ask god something he can't answer? Repent or burn in hell!")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
client.run('MTIxNTEzNDE1NzczNTIwNzAxMg.GG3Bri.LPhXWSV6Huc8rl9pSSWJaC8YVVRQR16KFFkT9s')
