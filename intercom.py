import discord
import threading

botID = -1
client = discord.Client()
targetChannel = '-1'
channelID = '-1'
speaker = 'SENDER'
nameColor = ''
speakerID = 0


def timeout():
    global speakerID
    global targetChannel
    global speaker
    global nameColor
    global channelID

    speakerID = 0
    targetChannel = '-1'
    speaker = '[SENDER]'
    nameColor = ''
    channelID = '-1'
    intercomTimer.cancel()


intercomTimer = threading.Timer(1800.0, timeout)


@client.event
async def on_message(message):
    global intercomTimer
    global speakerID
    global channelID
    global targetChannel
    global nameColor
    global speaker

    if message.guild is None and message.author != client.user:
        if message.content.startswith('#init'):
            if speakerID == 0:
                speakerID = message.author.id
                await message.channel.send('You are now using the Intercom. Your session will expire 30 minutes after your most recent activity.')
            else:
                await message.channel.send('The Intercom is in use!')

            intercomTimer = threading.Timer(1800.0, timeout)
            intercomTimer.start()
        if message.author.id == speakerID:
            if message.content.startswith('#room'):
                roomConfig = message.content.split('|', 1)
                channelID = roomConfig[1]
                targetChannel = await client.fetch_channel(channelID)
                await message.channel.send('Target channel has been set to ' + roomConfig[1] + '.')

                intercomTimer.cancel()
                intercomTimer = threading.Timer(1800.0, timeout)
                intercomTimer.start()

            if message.content.startswith('#name'):

                nameConfig = message.content.split('|', 1)
                speaker = '[' + nameConfig[1] + ']'
                await message.channel.send('Name has been set to ' + nameConfig[1] + '.')

                intercomTimer.cancel()
                intercomTimer = threading.Timer(1800.0, timeout)
                intercomTimer.start()

            if message.content.startswith('#color'):

                colorConfig = message.content.split('|', 1)

                if colorConfig[1] == 'white':
                    nameColor = ''
                    await message.channel.send('Name is now white.')
                elif colorConfig[1] == 'green':
                    nameColor = 'css'
                    await message.channel.send('Name is now green.')
                elif colorConfig[1] == 'cyan':
                    nameColor = 'yaml'
                    await message.channel.send('Name is now cyan.')
                elif colorConfig[1] == 'yellow':
                    nameColor = 'fix'
                    await message.channel.send('Name is now yellow.')

                intercomTimer.cancel()
                intercomTimer = threading.Timer(1800.0, timeout)
                intercomTimer.start()

            if message.content == '#leave':
                await message.channel.send('Ending session.')

                speakerID = 0
                channelID = '-1'
                targetChannel = '-1'
                speaker = '[SENDER]'
                nameColor = ''

            if message.content.startswith('#') is False:
                if (channelID == '-1') is False:
                    await targetChannel.send('```' + nameColor + '\n' + speaker + ':``` ' + message.content)
                    intercomTimer.cancel()
                    intercomTimer = threading.Timer(1800.0, timeout)
                    intercomTimer.start()
                else:
                    await message.channel.send('No room has been set!')

                    intercomTimer.cancel()
                    intercomTimer = threading.Timer(1800.0, timeout)
                    intercomTimer.start()
        else:
            await message.channel.send('You are not currently using the Intercom!')

botID = input('Please enter the bot ID that will be used for the Intercom. ')

client.run(botID)
