import requests
from dotenv import dotenv_values

env_variables = dotenv_values()

def send_message(email, message):
  mail_api_key= env_variables["MAILGUN_API_KEY"]
  mail_domain = env_variables["MAILGUN_API_DOMAIN"]

  return requests.post(
    "https://api.mailgun.net/v3/{}/messages".format(mail_domain),
      auth=("api", mail_api_key),
      data={"from": "Excited User <mailgun@{}>".format(mail_domain),
        "to": [email],
        "subject": "Greetings!",
        "text": message})
