import tiles, prompts

def main():
    # current color sequence
    sequence = tiles.Tiles.shuffled_tiles()

    # displays sequence, counts down, then clears terminal
    prompts.Prompts.countdown(sequence)

    # list of colors user entered
    user_colors = prompts.Prompts.users_list()

    # compares users input with sequence to determine win/loss
    print(prompts.Prompts.tile_sequence(user_colors))

if __name__ == "__main__":
    main()