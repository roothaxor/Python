import stripe, sys, json
from sys import platform as _platform
from termcolor import colored
if _platform == 'win32':
    import colorama
    colorama.init()
def green(text):
    return colored(text, 'green', attrs=['bold'])
def red(text):
    return colored(text, 'red', attrs=['bold'])

stripe.api_key = "secret_KEY"

info = []
name = raw_input("\nName: ")
try:
	info = raw_input('\nEnter Card: ').split()
except KeyboardInterrupt:
	print "[+] :( Exiting "
	sys.exit(1)

if len(info[0]) != 16:
	print red("\nInvalid Card Number :(")
	sys.exit(0)
#Create a Token for card.
tokreq = stripe.Token.create(
  card={
  	"name": name,
    "number": info[0],
    "exp_month": info[1],
    "exp_year": info[2],
    "cvc": info[3]
  },
)

tokk = json.dumps(tokreq)
token = json.loads(tokk)
token = token['id']

#Charge Card.
try:
	status = stripe.Charge.create(
	  amount=50,
	  currency="usd",
	  source=token, # obtained with Stripe.js
	  description="Automated Charge"
	)
except stripe.error.CardError as e:
	print red("\n[!] Card Declined :( ") + str(e)
	sys.exit(0)
output = json.dumps(status)
outpt = json.loads(output)
output = outpt['status']
if output == 'succeeded':
	print green("\n[+] Card is Alive :)")