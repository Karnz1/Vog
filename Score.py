def add_score(difficulty):
    with open('scores.txt', 'r+') as file:
        content = file.read().strip()
        score = int(content)
        points_of_winning = (difficulty * 3) + 5
        score = score + points_of_winning
        # Print the list of lines
        print(score)

        file.seek(0)
        file.truncate()
        file.write(str(score))
