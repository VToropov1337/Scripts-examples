import base64

with open('path_to_file', 'r') as f:
	decoded_file = f.read()

decoded_file = decoded_file.encode("UTF-8")
decoded_file = base64.b64decode(decoded_file)
decoded_file = decoded_file.decode("UTF-8")

with open('path_to_file', 'w') as f:
	f.write(decoded_file)
