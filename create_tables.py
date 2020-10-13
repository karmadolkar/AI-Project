import os
from pathlib import Path
from bs4 import BeautifulSoup
from get_maximum_words import get_maximum_count_words, get_maximum_count_tags

def main():
    """
    This function runs on all the Train directories and returns the 3 tables(dictionaries)
    words_dict : For storing frequency of words 
    tags_dict: For storing the frequency of tags
    word_tags_dict: For storing word_tag for the dataset.
    """
     
    words_dict = {}
    tags_dict = {}
    word_tags_dict = {}
    
    for directory in os.scandir(train_directory):
        for filename in os.scandir(directory):
            
            with open(filename.path,'r') as _:
                file_content = _.read()
                _.close()
            
            soup = BeautifulSoup(file_content, 'lxml')
            
            for words in soup.findAll("w"):
                word = words.text
                if(word[-1] is ' '):
                    word = word[:-1]
                tag = words["pos"]
                if(tag[-1] is ' '):
                    tag = tag[:-1]
                
                word_tag = word + '_' + tag

                if(word in words_dict):
                    words_dict[word] += 1
                else:
                    words_dict[word] = 0

                if(tag in tags_dict):
                    tags_dict[tag] += 1
                else:
                    tags_dict[tag] = 0
                    
                if(word_tag in word_tags_dict):
                    word_tags_dict[word_tag] += 1
                else:
                    word_tags_dict[word_tag] = 0        
        
    """Prints all the words in the table in descending order of their appearance."""
    words_dict = get_maximum_count_words(words_dict)
    sort_words = dict(list(words_dict.items())[0: 10])
    print(str(sort_words))  
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    """prints all the tags in the table in descending order of their appearance."""
    tags_dict = get_maximum_count_tags(tags_dict)
    sort_tags = dict(list(tags_dict.items())[0: 10])
    print(str(sort_tags))      

        
if __name__ == "__main__":
    
    train_directory = str(Path('Train-corups\\'))
    train_directory = train_directory.replace('\\',os.sep)
    main()
