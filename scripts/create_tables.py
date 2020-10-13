import os
from pathlib import Path

def main():
    for directory_name in os.scandir(train_directory):
        print(directory_name.path)
        
        
        
if __name__ == "__main__":
    train_directory = str(Path('Train-Corpus/'))
    main()
