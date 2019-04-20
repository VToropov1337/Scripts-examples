def imper_to_json(json_file):
	for k,v in json_file.items():
		if type(v) == dict:
			imper_to_json(v)
		if type(v) == list and len(v) > 0:
			for i in range(len(v)):
				imper_to_json(v[i])
		if k in hh.keys():
			json_file[k] = hh[k]

	return json_file