import tiles
import time
import os

class Prompts():

    def tile_sequence(user_input):

        correct_sequence = tiles.Tiles.shuffled_tiles()
        count = 0

        for color1 in user_input:
            if color1 != correct_sequence[count]:
                print(" ")
                print("*************")
                return f"You entered: {user_input}\n. The correct answer was {correct_sequence}\n. You Lose!\n*************\n\n"
            count += 1
        print(" ")
        print("*************")
        return f"You entered: {user_input}\n. The correct answer was {correct_sequence}\n. You Win!\n*************\n\n"

    def users_list():

        sequence = tiles.Tiles.shuffled_tiles()
        user_input_list = []

        for i in sequence:
            user_input_list.append(input(f"Colors: blue, green, pink, purple, red, yellow\n\n What was the order? (Enter one color at a time) :-> "))
            print(" ")
            print(" ")
            print("-------------")
            print("Current Submission: " + str(user_input_list) + "\n")

        return user_input_list
    
    def countdown(sequence):
        print(" ")
        print("-------------")
        print("Memorize:")
        print(sequence)
        time.sleep(3)
        print(" ")
        print("5...")
        print(" ")
        time.sleep(1)
        print("4...")
        print(" ")
        time.sleep(1)
        print("3...")
        print(" ")
        time.sleep(1)
        print("2...")
        print(" ")
        time.sleep(1)
        print("1...")
        print(" ")
        time.sleep(1)
        os.system('cls||clear')
        print(" ")
        print(" ")
