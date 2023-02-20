Netflix = ""
try:
    # open the file and read it
    with open('List.txt', 'r', encoding="utf-8") as f:
        data = str(f.read())
        
        # find the start of the list
        # 18 is the length of the string + >
        startList = data.find("class=\"col title\"") + 18
        while startList:
            # find the start and end of the title
            startTitle = data.find(">", startList) + 1  # +1 to remove the >
            endTitle = data.find("<", startTitle)
            
            print(data[startTitle:endTitle])
            # add the title to the list
            Netflix = Netflix + data[startTitle:endTitle] + "\n"
            
            # find the start of the next title
            startList = data.find("class=\"col title\"", endTitle) + 18
            if startList < startTitle:
                startList = 0
    print(Netflix)
except:
    print("Error make sure you have a file named List.txt in the same folder as this script")


# write the list to a file
with open('ListLikeCompleted.txt', 'w', encoding="utf-8") as f:
    f.write(Netflix)
input("press enter to exit")
