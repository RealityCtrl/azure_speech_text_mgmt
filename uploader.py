import os, requests, time

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
			'Content-Type': 'multipart/form-data',
			'Accept': 'text/plain',
			'Authorization':'Bearer ' + self.access_token
		}
		payload = {
			'name':'TestLMData1',
			'description':'Testing%20creating%20a%20custom%20langauge%20data',
			'locale':'en-US',
			'dataImportKind':'Language'
		}
		files={'languagedata':('TestLMData1.txt',open(self.filepath,'r'),'text/plain')}
		r = requests.post(url=upload_url, data=payload, files=files)
		print(r.status_code)
		print(r.json)
		
if __name__ == "__main__":
	subscription_key = sys.argv[1]
	file_path = sys.argv[2]
	app = TextToSpeech(subscription_key, file_path)
	app.get_token()
	app.upload_adaptation_data()