import re
import urllib
import urllib.parse

class PyParsing(object):
	@classmethod
	def parseMessageFromClient(cls, data_as_string):
		filter = 'GET \/\?([^ ]+)'
		m = re.search(filter,data_as_string)
		if m:
			found = m.group(1)
			content = urllib.parse.parse_qs(found)
			callback = content['callback'][0]
			token = content['_'][0]
			data = dict()
			for key, value in content.items():
				layers = key.replace("]", "").split("[")
				if layers[0] != "callback" and layers[0] != "_":
					current = data
					j = 0
					while j < len(layers):
						layer = layers[j]
						if j < len(layers) - 1 and layers[j + 1] == "":
							current[layer] = list()
							j += 1
						else:
							if not layer in current.keys():
								current[layer] = dict()
						current = current[layer]
						j += 1
					current = data
					i = 0
					while i < len(layers) - 1:
						current = current[layers[i]]
						i += 1
					#print(str(layers) + "\t" + str(i))
					#print(layers[i] + "\t" + str(key) + "\t" + str(value))
					if layers[i] == "":
						i = 0
						current = data
						while i < len(layers) - 2:
							current = current[layers[i]]
							i += 1
						current[layers[i]].append(value)
					else:
						current[layers[i]] = value
			return callback, token, data
		return None, None, dict()