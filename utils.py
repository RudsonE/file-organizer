import os
import json
import shutil

class Files:
    
    def __init__(self):
        
        self.files_extensions = json.load(open('./files_extensions.json'))
        self.image_found = self.files_extensions["image"]
        self.video_found = self.files_extensions["video"]
        self.compressed_found = self.files_extensions["compressed"]
    
    def detect_file_type(self, dir):
        
        files = os.listdir(dir)
        file_count = len(files)
        for name in files:
            #check if found name is a file
            if os.path.isdir(os.path.join(dir, name)):
                pass
            else:
                ext = name.split('.')[1]
                
                #check file type
                if ext in self.image_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./images")
                elif ext in self.video_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./videos")
                elif ext in self.compressed_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./compressed")
                    
                #unknown file type action
                elif ext not in self.image_found or ext not in self.video_found:
                    print(f"Unknown file type: {name} | Type: {ext}")
                else:
                    print("Not files found")
                    
        print(f"Done, {file_count} files found")
        
    #move files to destination directory
    def move_file(self, file, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
            shutil.move(file, dir)
        elif os.path.exists(dir):
            shutil.move(file, dir)