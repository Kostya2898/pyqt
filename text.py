with open("text.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
    for i in range (0,len(text),2):
        print(text[i])



