import os
import json
import shutil

class Files:
    
    def __init__(self):
        
        self.files_extensions = json.load(open('./files_extensions.json'))
    
    def detect_file_type(self, dir):
        
        files = os.listdir(dir)
        file_count = len(files)
        for name in files:
            #check if found name is a file
            if os.path.isdir(os.path.join(dir, name)):
                pass
            else:
                ext = name.split('.')[1]
                image_found = self.files_extensions["image"]
                video_found = self.files_extensions["video"]
                compressed_found = self.files_extensions["compressed"]
                
                #check file type
                if ext in image_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./images")
                elif ext in video_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./videos")
                elif ext in compressed_found:
                    
                    self.move_file(f"{dir}/{name}",  dir + "./compressed")
                    
                #unknown file type action
                elif ext not in image_found or ext not in video_found:
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