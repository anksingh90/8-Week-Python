# copy content of 1 txt file into other using with statement

with open('log.txt', 'r') as infile:
    with open('log_write.txt', 'a') as outfile:
        for line in infile:
            #print(line)
            outfile.write(line.upper())

