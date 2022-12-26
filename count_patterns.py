#2 variables one for pattern one for the text 
#user input = string if inside the string there is this pattern then count +1
def pattern_count(text, pattern) :
    count = 0 
    for i in range (len(text)-len(pattern)+1) :
        if text[i:i+len(pattern)] == pattern :
            count = count + 1
    return count 