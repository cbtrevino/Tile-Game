import tiles, prompts

def yee():

    sequence = tiles.Tiles.shuffled_tiles()
    user_input_list = []

    for i in sequence:
        user_input_list.append(input(f"Type the colors in order one by one: {sequence}?: "))
        print(" ")
        print("Current Submission: " + str(user_input_list))

    return user_input_list

yee()
