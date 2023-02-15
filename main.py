
f = open("/home/sameeranati/mail merge project/Input/Names/invited_names.txt", "r")
names=f.readlines()
with open("/home/sameeranati/mail merge project/Input/Letters/starting_letter.txt", mode='r') as file:
    content=file.read()
    # file=open("/home/sameeranati/mail merge project/Output/ReadyToSend/letters.txt", "w")
    for name in names:
        stripped_name=name.strip()
        letter= content.replace("[name]", stripped_name)
        with open(f"/home/sameeranati/mail merge project/Output/ReadyToSend/{stripped_name}_letter.txt", "w") as file:
            file.write(letter)
            file.write('\n\n\n')


