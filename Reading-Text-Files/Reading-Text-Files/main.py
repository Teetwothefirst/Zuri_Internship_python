# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open ('story.txt', 'r') as filename:
        lines = filename.read()
        print(lines)
        filename.close()
    return lines

read_file_content('story.txt')


def count_words():
    text = read_file_content("story.txt")
    print(text)
    print(len(text))
    
    # [assignment] Add your code here

    each_word_in_paragraph = text.split()
    count = {}
    for the_words in each_word_in_paragraph:
        if the_words in count:
            count[the_words]+=1
        else:
            count[the_words] = 1
    return count_words
print(count_words)  
    #print(f'word {count} : {each_word_in_paragraph} ')
    # return {"as": 10, "would": 20}

count_words()