import discord

client = discord.Client()

@client.event
async def on_ready():
	print("Logged on.")
	print(client.user.name + "#" + client.user.discriminator)
	print(client.user.id)
	print("-------")

@client.event
async def on_message(message):
	if (message.content.startswith("||checkroles") and message.channel.id == 211715067329249280):
		await message.channel.send("Checking for users without Learner role...")
		for member in message.guild.members:
			if (discord.utils.find(lambda r: r.name == "Learners", message.guild.roles) not in member.roles):
				try:
					await member.add_roles(discord.utils.find(lambda r: r.name == "Learners", message.guild.roles))
				except discord.Forbidden:
					await message.channel.send(":x: I need the **Manage Roles** permission to work correctly.")
					return
		await message.channel.send(":white_check_mark: All users now have the Learner role!")

client.run("Lol no token for you")