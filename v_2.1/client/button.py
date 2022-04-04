def changeSign(data, buttons, sign):
    if data == "1":
        buttons[0].configure(text=sign)
    elif data == "2":
        buttons[1].configure(text=sign)
    elif data == "3":
        buttons[2].configure(text=sign)
    elif data == "4":
        buttons[3].configure(text=sign)
    elif data == "5":
        buttons[4].configure(text=sign)
    elif data == "6":
        buttons[5].configure(text=sign)
    elif data == "7":
        buttons[6].configure(text=sign)
    elif data == "8":
        buttons[7].configure(text=sign)
    elif data == "9":
        buttons[8].configure(text=sign)