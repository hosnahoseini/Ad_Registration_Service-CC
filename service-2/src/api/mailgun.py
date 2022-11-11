import requests

DOMAIN = "sandbox723af48ac00c438e9cbf52899e888fba.mailgun.org"
API_KEY = "749ac0bafdc729e1e67bbee1efa9dc56-48c092ba-fb629447"
TEXT = TEXT = f"""
        <h1>BOOO </h1>
        
        """
SUBJECT = "Cloud Computing HW1"
EMAIL_ADDRESS = "hosna.hoseini@gmail.com"

def send_simple_message(email, subject, text):
	return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY),
		data={"from": f"<mailgun@{DOMAIN}>",
			"to": [email],
			"subject": subject,
			"html": text})

if __name__ == '__main__':
	
	response = send_simple_message(EMAIL_ADDRESS, SUBJECT, TEXT)
	print(response.json())