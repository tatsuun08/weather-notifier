from get_weather import get_city_weather
import discord
from config import Config


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

japan_regions = {
    "北海道": ["道北", "道東", "道央", "道南"],
    "東北": ["青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県"],
    "関東": ["茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県"],
    "中部": ["新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県"],
    "近畿": ["三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県"],
    "中国": ["鳥取県", "島根県", "岡山県", "広島県", "山口県"],
    "四国": ["徳島県", "香川県", "愛媛県", "高知県"],
    "九州": ["福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]
}

class Select(discord.ui.Select):
    def __init__(self):
        options=[]

        for region in japan_regions.keys():
            options.append(
                discord.SelectOption(label=region)
            )
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Your choice is {self.values[0]}!",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!Weather':
        await message.channel.send(view=SelectView())

print("client run")
client.run(Config.DISCORD_TORKEN)

