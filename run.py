from dotenv import load_dotenv
from time import sleep
import os

from slack_bolt import App

load_dotenv()
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

emojis = [
  "cool",
  "comet",
  "cookie",
  "computer"
  "collision",
  "cactus",
  "wolf",
  "cold_face",
  "100",
  "brain",
  "koala",
  "grapes",
  "earth_africa",
  "scooter",
  "airplane",
  "cyclone",
  "fire",
  "safety_vest",
  "musical_note",
  "musical_keyboard",
  "fax",
  "mute",
  "no_bell",
  "no_mobile_phones",
  "mag",
  "briefcase",
  "warning",
  "o",
  "red_circle",
  "fuelpump",
  "scissors",
  "sparkles",
  "sparkling_heart",
  "star",
  "star2",
  "dizzy",
  "boom",
  "zzz",
  "alien",
  "satellite",
  "satellite_orbital",
  "scorpius",
  "ophiuchus",
  "aries",
  "taurus",
  "gemini",
  "cancer",
  "leo",
  "virgo",
  "libra",
  "scorpius",
  "sagittarius",
  "capricorn",
  "aquarius",
  "pisces",
  "ophiuchus",
  "six_pointed_star",
  "negative_squared_cross_mark",
  "white_check_mark",
  "eight_pointed_black_star",
  "eight_spoked_asterisk",
  "sparkle",
  "question",
  "grey_question",
  "grey_exclamation",
  "exclamation",
  "heavy_exclamation_mark",
  "heavy_heart_exclamation_mark_ornament",
  "heart",
  "heavy_plus_sign",
  "heavy_minus_sign",
  "heavy_division_sign",
  "heavy_multiplication_x",
  "heavy_dollar_sign",
  "currency_exchange",
]

for i in range(999 * 999 * 99 * 99):
  emoji = emojis[i % len(emojis)]
  try:
    app.client.users_profile_set(profile={"status_emoji": ":" + emoji + ":"})
  except Exception as e:
    print(emoji)
    print(e)
  sleep(7)

