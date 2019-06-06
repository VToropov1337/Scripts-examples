import base64

with open('path_to_file', 'r') as f:
	file = f.read()

file = file.encode("UTF-8")
encoded_file = base64.b64.encode(file)
encoded_file = encoded_file.decode("UTF-8")

with open('path_to_file', 'w') as f:
	f.write(encoded_file)
