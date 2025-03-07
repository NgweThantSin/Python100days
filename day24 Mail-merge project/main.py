PLACEHOLDER = "[name]"


with open("./input/Name/Invited_names.txt","r") as name_file:
    names = name_file.readlines()
    # print(names)

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    for name in names:
        striped_name = name.strip()
        new_letter =letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/Letter_for_{striped_name}.txt", mode ="w") as completed_letter:
            completed_letter.write(new_letter)
