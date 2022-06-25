from internetSpeedTwitterBot import InternetSpeedTwitterBot


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(bot.up, bot.down)

bot.tweet_at_provider()
