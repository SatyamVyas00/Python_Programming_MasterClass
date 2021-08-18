def banner_text(text=" ",screen_width=80):
    # this docstring using which we can write function for
    """
    Print the given string in a ** string ** format

    The function will raise an error if given string exceed len(screen_width)-4
    :param text: The String to print on Screen
    :param screen_width:limit of Screen width (Screen Size)
    :return:None
    """
    if len(text) > screen_width -4:
    # it will raise an error when condition is met
        raise ValueError("String {0} is larger then specified width {1}".format(text,screen_width))


    if text == "*":
        print("*"*screen_width)
    else:
        centre_text = text.center(screen_width-4)
        output_string = ("**{}**".format(centre_text))
        print(output_string)

#print(banner_text.__doc__)
help(banner_text)
banner_text("*",60)
banner_text("Always look on the left bright side of life...",60)
banner_text("If life seems jolly rotten,",60)
banner_text("There's something you've forgotten!",60)
banner_text("And that's to laugh and smile and dance and sing,",60)
banner_text(screen_width=60) #parameter can be passed using positon or keyword name like in this one
banner_text("When you're feeling in the dumps,",60)
banner_text("Don't be silly Chumps",60)
banner_text("Just purse your lips and whistle - that's the thing!",60)
banner_text("And... always look on the bright side of life",60)
banner_text("*",60)