from dotenv import load_dotenv
from time import sleep
import os

from slack_bolt import App

load_dotenv()
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

emojis = [
  "cool",
  "comet"
  "cookie",
  "computer"
  "collision",
  "cactus",
  "wolf",
  "cold_face"
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
  "o"
  "red_circle",
  "large_blue_circle",
  "large_orange_diamond",
  "large_blue_diamond",
  "large_orange_circle",
  "large_blue_square",
  "large_red_square",
  "large_red_triangle_down",
  "large_red_triangle",
]

# infinite times
for i in range(40):
  # trycatch
  try:
    emoji = emojis[i % len(emojis)]
    app.client.users_profile_set(profile={"status_emoji": ":" + emoji + ":"})
  except Exception as e:
    print(e)
  sleep(10)

