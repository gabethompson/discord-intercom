# discord-intercom
A simple bot for Discord that relays messages to a public channel. It requires a bot ID to be given on start-up, as hard-coding the ID is a generally unsafe practice, and then takes the following commands:


<b>#room|(channel ID)</b>
Sets the channel in which messages will be sent.

  
<b>#name|(sending name)</b> *Sets the name which will be added to the start of any message relayed through the bot.

  
<b>#color|(color)</b>
*Sets the color which will be used for the messenger name. The options available are as follows:

placeholder

Any message that does not start with a # character will be relayed as set up by these previous three commands.
