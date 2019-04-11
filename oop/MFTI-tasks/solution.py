class Filereader(object):
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        
    def read(self):
        try:
            with open(self.path_to_file, 'r') as f:
                file = f.read()
                return file
        except IOError:
            return ""
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    reader = Filereader("example2.txt")
    print(reader.read())