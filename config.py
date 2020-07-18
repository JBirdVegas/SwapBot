import json

def ascii_encode_dict(data):
        ascii_encode = lambda x: x.encode('ascii') if isinstance(x, unicode) else x
        return dict(map(ascii_encode, pair) for pair in data.items())

def get_json_data(fname):
        with open(fname) as json_data:
                data = json.load(json_data, object_hook=ascii_encode_dict)
        return data

class Config():

	def __init__(self, sub_name):
		f = open("config/" + sub_name.lower() + "-config.txt", "r")
		info = f.read().splitlines()
		f.close()
		self.subreddit_name = info[0].split(":")[1]
		if self.subreddit_name in ['digitalcodesell', 'uvtrade']:
			self.database_name = 'digitalcodeexchange'
		else:
			self.database_name = self.subreddit_name
		self.client_id = info[1].split(":")[1]
		self.client_secret = info[2].split(":")[1]
		self.bot_username = info[3].split(":")[1]
		self.bot_password = info[4].split(":")[1]
		if info[5].split(":")[1]:
			self.flair_word = " " + info[5].split(":")[1]
		else:
			self.flair_word = " Swaps"
		if info[6].split(":")[1]:
			self.mod_flair_word = info[6].split(":")[1] + " "
		else:
			self.mod_flair_word = ""
		if info[7].split(":")[1]:
			self.flair_templates = get_json_data('templates/'+self.subreddit_name+'.json')
		else:
			self.flair_templates = False
		if info[8].split(":")[1]:
			self.confirmation_text = info[8].split(":")[1]
		else:
			self.confirmation_text = "Added"
		if info[9].split(":")[1]:
			self.flair_threshold = int(info[9].split(":")[1])
		else:
			self.flair_threshold = 0
		if info[10].split(":")[1]:
			self.mod_flair_template = info[10].split(":")[1]
		else:
			self.mod_flair_template = ""
		if info[11].split(":")[1]:
			self.titles = get_json_data('titles/'+self.subreddit_name+'.json')
		else:
			self.titles = False