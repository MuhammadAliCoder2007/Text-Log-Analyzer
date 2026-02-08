
#Log Analyzer Project
#Goals
# Read a log file line by line
#Count total lines
#Count the most common words
#Output a detailed summary

f = open("log.txt")
empty_dict = dict()

total =0
string = 'error'
errors = 0
for line in f:
    # print(line) #print each line
    total+=1 #keeping the count of total
    if string in line.lower():  #checking if error is in the line
        errors+=1   #increasing the count of error by 1
    sentecne = line.split()
    for word in sentecne:
        if word in empty_dict:
            empty_dict[word]+=1
        else:
            empty_dict[word] =1

print(total)    #printing total logs
print(errors)   #printing total errors
print(empty_dict)



sorted_words_top5 = sorted(empty_dict.items(), key=lambda item: item[1], reverse=True)[:5]
for word,count in sorted_words_top5:
    print(word,count)

