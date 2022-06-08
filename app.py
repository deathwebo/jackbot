import os
import random
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


jack_says = """wasson today then
cheers homie
innum
shiiettt
wagwan
nice bro
bastard thing
fair one
Ah shiiettt
nice man
just here existing
How's she goin bud
I'm alright love just here
Nawh bbz
Alreet?
Mike
Lovely stuff
Oh bby
Lads
ya daft racist
:laughing:
aye
ohh aye
fuck a job
True true
cba
Wasson today then bud
Aye
Fair
Yup
innit
Innit Bro
you know it bud
How you doing hun
:pinched_fingers:
dam sun
damn son
bummers
sup miguel
no bueno
oh baby
amazing
some people
decent
same man
bastards"""


# Add functionality here
# @app.event("app_home_opened") etc

@app.message("jack")
def say_hello(message, say):
    jack_msg = random.choice(jack_says.split('\n'))
    say(jack_msg)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
  try:
    # views.publish is the method that your app uses to push a view to the Home tab
    client.views_publish(
      # the user that opened your app's app home
      user_id=event["user"],
      # the view object that appears in the app home
      view={
        "type": "home",
        "callback_id": "home_view",

        # body of the view
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Welcome to your _App's Home_* :tada:"
            }
          },
          {
            "type": "divider"
          },
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
            }
          },
          {
            "type": "actions",
            "elements": [
              {
                "type": "button",
                "text": {
                  "type": "plain_text",
                  "text": "Click me!"
                }
              }
            ]
          }
        ]
      }
    )
  
  except Exception as e:
    logger.error(f"Error publishing home tab: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))
