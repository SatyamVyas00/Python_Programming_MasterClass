available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                  }

current_choice = None
computer_parts = {}     # empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_parts = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_parts}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_parts}")
            computer_parts[current_choice] = chosen_parts
        print(f"You dictionary now contains: {computer_parts}")
    else:
        for key in available_parts:
            print("{}: {}".format(key,available_parts[key]))
    current_choice = input("> ")


