word = input("Enter a string: ")

if word == "":
    print("Compressed string:")
else:
    result = ""
    count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count = count + 1
        else:
            result = result + word[i - 1] + str(count)
            count = 1

    result = result + word[-1] + str(count)
    print("Compressed string:", result)
