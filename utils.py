import os
import json
import shutil

class Files:
    
    def __init__(self):
        
        self.files_extensions = json.load(open('./files_extensions.json'))
        self.file_type = list(self.files_extensions.keys())
        self.terminal_columns = os.get_terminal_size().columns
    
    def detect_file_type(self, dir):
        
        files = os.listdir(dir)
        found_files = []
        total_valid_files = 0
        for file in files:
            if os.path.isdir(os.path.join(dir, file)):
                pass
            else:
                found_files.append(file)
            
        for name in files:
            ext = ""
            for type in self.file_type:
                
                if "." in name:
                    #check if found name is a file
                    ext = name.split('.')[1]
                    if ext in self.files_extensions[type]:
                        total_valid_files = total_valid_files + 1
                        print(f"Found: {name} | Extension: {ext} | Type: {type}")
                        self.move_file(f"{dir}/{name}", f"{dir}/{type}")
                    
                else:
                    pass
        if len(found_files) - (len(found_files) - total_valid_files) == 0:
                print("No files moved")
                    
        print("\n")
        print("=" * self.terminal_columns)      
        print(f"Done, {len(found_files)} files found, {len(found_files) - total_valid_files} is unknown type.")
        print("=" * self.terminal_columns)    
        
    #move files to destination directory
    def move_file(self, file, dir):
        if not os.path.exists(dir):
            os.mkdir(dir)
            shutil.move(file, dir)
        elif os.path.exists(dir):
            shutil.move(file, dir)
