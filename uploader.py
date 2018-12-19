import requests
from requests_toolbelt import MultipartEncoder
import sys
import base64

class TextToSpeech(object):
	def __init__(self, subscription_key,filepath):
		self.subscription_key = subscription_key
		self.access_token = None
		self.filepath = filepath

	def get_token(self):
		fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
		headers = {
			'Ocp-Apim-Subscription-Key': self.subscription_key
		}
		response = requests.post(fetch_token_url, headers=headers)
		self.access_token = str(response.text)
		
	def upload_adaptation_data(self):
		upload_url =  'https://westus.cris.ai/api/speechtotext/v2.0/datasets/upload'
		headers = {
			"Ocp-Apim-Subscription-Key":self.subscription_key
		}
		payload = {
			"name":"TestLMData3",
			"description":"from_python",
			"locale":"en-US", 
			"dataImportKind":"Language"
		}
		uploadfile={'languagedata':("TestLMData1.txt",open(self.filepath,'rb'),'text/plain')}
		r = requests.post(url=upload_url, headers=headers, data=payload, files=uploadfile)
		print("\n",r.status_code)
		print("\n",r.headers)

		
if __name__ == "__main__":
	subscription_key = sys.argv[1]
	file_path = sys.argv[2]
	app = TextToSpeech(subscription_key, file_path)
	#app.get_token()
	app.upload_adaptation_data()