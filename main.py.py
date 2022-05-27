def read_file_content(filename):
    # [assignment] Add your code here 
    with open (filename,'r') as f:
        file= f.read()
        return file
        
    #   return read_file_content('./story.txt')

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words=text.split()
    counts= dict()

    for word in words:
       if word in counts:
           counts[word]+=1
       else:
          counts[word]= 1
    return counts

print(count_words())

    