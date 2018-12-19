import requests
import sys

class TextToSpeech(object):
	def __init__(self, subscription_key):
		self.subscription_key = subscription_key
		self.access_token = None

	def get_token(self):
		fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
		headers = {
			'Ocp-Apim-Subscription-Key': self.subscription_key
		}
		response = requests.post(fetch_token_url, headers=headers)
		self.access_token = str(response.text)
		
	def list_datasets(self):
		dataset_url =  'https://westus.cris.ai/api/speechtotext/v2.0/datasets'
		headers = {
			#'Authorization':'bearer ' + self.access_token,
			'Ocp-Apim-Subscription-Key':self.subscription_key,
			'Accept': 'application/json'
		}
		r = requests.get(url=dataset_url, headers=headers)

		print(r.status_code)
		print(r.text)


if __name__ == "__main__":
	subscription_key = sys.argv[1]
	app = TextToSpeech(subscription_key)
	app.get_token()
	app.list_datasets()