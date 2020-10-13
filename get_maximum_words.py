import operator

def get_maximum_count_words(words_dict):
    sorted_words = dict( sorted(words_dict.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_words

def get_maximum_count_tags(tags_dict):
    sorted_tags = dict( sorted(tags_dict.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_tags
