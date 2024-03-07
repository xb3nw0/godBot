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
        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            user_input = await client.wait_for('message', timeout=60.0, check=check)
            response = openai.Completion.create(
                engine="davinci", 
                prompt=user_input.content,
                max_tokens=100
            )
            if response.choices:
                bible_quote = response.choices[0].text.strip()
                await message.channel.send(bible_quote)
            else:
                await message.channel.send("You ask god something he can't answer? Repent or burn in hell!")
        except asyncio.TimeoutError:
            await message.channel.send("One does not play with the Lord's time. Repent or burn in hell!")

# Replace 'YOUR_DISCORD_TOKEN' with your actual Discord bot token
client.run('MTIxNTEzNDE1NzczNTIwNzAxMg.GG3Bri.LPhXWSV6Huc8rl9pSSWJaC8YVVRQR16KFFkT9s')
