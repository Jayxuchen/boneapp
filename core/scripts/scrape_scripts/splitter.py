
fp = open("words_alpha.txt")
filenum = 0
newfp = open("words_"+str(filenum)+".txt","w")
count = 0
for line in fp:
    print(line.strip())
    print count
    if count >= 10000:
        count = 0
        filenum+=1
        newfp = open("words_"+str(filenum)+".txt","w")
    newfp.write(line)
    count+=1
