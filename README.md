# discord-intercom
A simple bot for Discord that relays messages to a public channel. It requires a bot ID to be given on start-up, as hard-coding the ID is a generally unsafe practice, and then takes the following commands:

<b>#init</b> Begins an intercom session, preventing anyone else from using the bot for the duration of the session (either 30 minutes or until manual termination).


<b>#room|(channel ID)</b>
Sets the channel in which messages will be sent.

  
<b>#name|(sending name)</b> *Sets the name which will be added to the start of any message relayed through the bot.

  
<b>#color|(color)</b>
*Sets the color which will be used for the messenger name. Due to Discord's limitations, the options available are as follows: 'white', 'cyan', 'green', 'yellow'


<b>#leave</b> Ends the intercom session, setting all values back to default and allowing others to make use of the intercom.

Any message that does not start with a # character will be relayed as set up by these previous commands.

As this is a demonstration bot, it does not come with limitations on who is allowed to send messages through it. In a practical situation, it would check sender ID against a list of "approved" IDs before allowing a session to be opened.
