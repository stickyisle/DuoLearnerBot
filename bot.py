import discord

client = discord.Client()
guild = None
token = None
with open("token.txt") as file:
	token = file.read()

@client.event
async def on_ready():
	print("Logged on.")
	print(client.user.name + "#" + client.user.discriminator)
	print(client.user.id)
	print("-------")
	guild = client.guilds[0]

async def check_for_users():
	i=0
	for member in guild.members:
		if (discord.utils.find(lambda r: r.name == "Learners", guild.roles) not in member.roles):
			try:
				await member.add_roles(discord.utils.find(lambda r: r.name == "Learners", guild.roles))
				i += 1
			except discord.Forbidden:
				await client.get_channel(371388150683271178).send(":x: I need the **Manage Roles** permission to work correctly.")
				return
	await client.get_channel(371388150683271178).send(":white_check_mark: All users now have the Learner role! (%d added.)" % i)

async def hour_loop():
	if (client.is_ready()):
		await check_for_users()
		await asyncio.sleep(60 * 60)
	else:
		await asyncio.sleep(60 * 5)
client.run(token)