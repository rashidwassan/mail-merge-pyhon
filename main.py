with open('./Input/Names/invited_names.txt') as invited_people:
    invited_people_list = invited_people.readlines()

for person in invited_people_list:
    with open('Input/Letters/starting_letter.txt') as letter:
        letter_content = letter.read().replace('[name]', person)

    with open(f'Output/ReadyToSend/letter_to_{person}.txt', 'w') as ready_letter:
        ready_letter.write(letter_content)
