import discord
from ask import ask
from scrape import scrape

# Define bot's intents/permissions
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.reactions = True
intents.members = True

# Initialize the bot client with intents
client = discord.Client(intents=intents)

context = ""  # The context of the conversation (all the websites read)
messages = []  # The messages sent by the user and model
thinking = False  # Whether the bot is thinking or not to prevent multiple requests

# Triggered when bot is ready
@client.event
async def on_ready():
    print(f'Bot logged in as: {client.user}')

# Triggered when anyone sends a message
@client.event
async def on_message(message):
    global context, messages, thinking
    # If sender is bot, ignore it
    if message.author == client.user:
        return

    if thinking:  # stop multiple requests from messing it up
        return
    thinking = True

    # Handle commands
    await handle_commands(message)

    thinking = False  # allow the bot to listen to new messages

async def handle_commands(message):
    global context, messages
    if message.content == '!help':
        await message.channel.send("""Hello! I'm Sebastian, a Discord bot here to help you out.
        
Commands:
!help - Shows this message.
!read [URLs] - Reads websites, separated by spaces.
!clear - Clears the conversation and website context.""")
    elif message.content.startswith('!read'):
        urls = message.content.split()[1:]  # Extract URLs from the command
        if not urls:
            await message.channel.send('No links provided!')
            return
        await message.channel.send('**Reading link(s)...** Please wait.')
        for url in urls:
            text = scrape(url)
            context += '\n\n' + text
        await message.channel.send('**Done reading!**')
    elif message.content == '!clear':
        context = ""
        messages = []
        await message.channel.send('Conversation and context cleared!')
    else:
        messages.append(message.content)
        response = ask(["You are a helpful chatbot designed to answer questions given the context of the websites. Respond in markdown. Say \"Okay!\" if you understand.\nContext:\n" + context, "Okay!"] + messages[-15:])
        messages.append(response)
        await message.channel.send(response)

# Run the bot with your Discord bot token
client.run('#Enter discord api token')
