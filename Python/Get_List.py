netflix = ""
try:
    # open the file and read the data
    with open('List.txt', 'r', encoding="utf-8") as f:
        data = str(f.read())

        # find the start and the final of the list
        start = data.find("class=\"galleryLockups\"") + 16
        final = data.find("role=\"contentinfo\"", start) + 18

        # find the start of the title
        startTitle = data.find("aria-label", start) + 12
        while startTitle:
            # find the end of the title
            endTitle = data.find("\"", startTitle)

            # add the title to the list
            netflix = netflix + data[startTitle:endTitle] + "\n"

            # find the start of the next title
            startTitle = data.find("aria-label", endTitle) + 12
            if startTitle > final:
                startTitle = 0

    print(netflix)
    # write the list to a file
    with open('ListCompleted.txt', 'w', encoding="utf-8") as f:
        f.write(netflix)
    input("press enter to exit")
except:
    print("Error make sure you have a file named List.txt in the same folder as this script")
