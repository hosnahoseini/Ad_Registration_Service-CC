DOMAIN = "sandboxa9f677b9be0e4f48b9b79050b7a96698.mailgun.org"
API_KEY = "b73a19ece11142a760aa952c45bd3c9e-d117dd33-52fc7b48"
EMAIL_ADDRESS = "hosna.hoseini@gmail.com"
TEXT = "Your ad has been accepted!"
SUBJECT = "Cloud Computing HW1"

def send_simple_message(email, subject, text):
	return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY),
		data={"from": f"{DOMAIN}>",
			"to": [email],
			"subject": subject,
			"text": text})

response = send_simple_message(EMAIL_ADDRESS, SUBJECT, TEXT)
print(response.json())