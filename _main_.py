from tkinter import *
game = Tk()
game.configure(bg="dark blue")
game.title("TIC TAC TOE by Charity Rymbai")

##Functions

#Function to decide to print X or O after button click
def button_click(button):
    global Player_turn
    if Player_turn % 2 == 0:
        player(button, "X")
        turn("O")
    elif Player_turn % 2 != 0:
        player(button, "O")
        turn("X")
    check()
    Player_turn += 1

#Function to print X or O on fresh space
def player(button,XO_determiner):
    global Player_turn
    if button['text']=="   ":
        button['text'] = XO_determiner
    else:
        Player_turn-=1

#Function to print which player's turn in label2
def turn(player):
    # printing which player's turn in label2
    changing_text_in_label2("Player "+player+"'s turn!!")

#Function to check the neccesary criteria to win is fulfilled or not
def check():
    #check in horizontal line 1
    if button_1['text']==button_2['text']==button_3['text']:
        wingame(button_1)
    #check in horizontal line 2
    elif button_4['text']==button_5['text']==button_6['text']:
        wingame(button_4)
    #check in horizontal line 3
    elif button_7['text']==button_8['text']==button_9['text']:
        wingame(button_7)
    #check in vertical line 1
    elif button_1['text'] == button_4['text'] == button_7['text']:
        wingame(button_4)
    #check in vertical line 2
    elif button_2['text']==button_5['text']==button_8['text']:
        wingame(button_2)
    #check in vertical line 3
    elif button_3['text']==button_6['text']==button_9['text']:
        wingame(button_6)
    # check in diagonal from 1st to last button
    elif button_1['text'] == button_5['text'] == button_9['text']:
        wingame(button_1)
    #check in diagonal from 3rd to 7th button
    elif button_3['text']==button_5['text']==button_7['text']:
        wingame(button_3)
    # check for DRAW(all conditions to win not met but the space is filled)
    elif button_1['text']!="   "and button_2['text']!="   "and button_3['text']!="   "and button_4['text']!="   "and button_5['text']!="   "and button_6['text']!="   "and button_7['text']!="   "and button_8['text']!="   "and button_9['text']!="   ":
        printwinner("draw")

#Function to determine which player won
def wingame(button):
    if button['text']=="X":
        printwinner("X")
    elif button['text']=="O":
        printwinner("O")

#Function to print the winner of the game
def printwinner(Winner):
    if Winner=="X" or Winner== "O":
        First_part="Player "
        Last_part=" wins!!!"
        text_to_show=First_part+Winner+Last_part
    elif Winner=="draw":
        text_to_show="It's a Draw!!!!"
    changing_text_in_label2(text_to_show)
    #disabling all buttons after printing the winner
    disableButton()
    #enabling the restart button
    button_to_restart["state"] = "normal"

def changing_text_in_label2(text_to_show):
    global label_2
    label_2.config(text=text_to_show)

# disabling all buttons in the space
def disableButton():
    button_1["state"]="disabled"
    button_2["state"]="disabled"
    button_3["state"]="disabled"
    button_4["state"]="disabled"
    button_5["state"]="disabled"
    button_6["state"]="disabled"
    button_7["state"]="disabled"
    button_8["state"]="disabled"
    button_9["state"]="disabled"

# enabling all buttons in the space
def enableButton():
    button_1["state"]="normal"
    button_2["state"]="normal"
    button_3["state"]="normal"
    button_4["state"]="normal"
    button_5["state"]="normal"
    button_6["state"]="normal"
    button_7["state"]="normal"
    button_8["state"]="normal"
    button_9["state"]="normal"

#Function to restart the game
def restart_game():
    for button in (button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9):
        button['text']="   "
    #enabling all buttons
    enableButton()
    #clearing the text on label printing winner
    global label_2
    label_2.config(text="Player X's turn!!")
    #disabling the restart button
    button_to_restart["state"] = "disabled"
    global Player_turn
    Player_turn=0

##_main_

#Declaring Buttons
button_1= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_1))
button_2= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_2))
button_3= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_3))
button_4= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_4))
button_5= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_5))
button_6= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_6))
button_7= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_7))
button_8= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_8))
button_9= Button(game, text="   ",font=("Comic Sans MS",20),bg="light blue", width=10, height=4, command=lambda:button_click(button_9))
button_to_restart= Button(game, text="Restart",font=("Comic Sans MS",20),bg="light blue", width=10, height=1, command=restart_game)

#declaring labels
label_1=Label(game,text="Tic tac toe game",font=("Comic Sans MS",20),bg="dark blue",fg="white",height=1)
label_2=Label(game,text="Player X's turn!!",font=("Comic Sans MS",20),bg="dark blue",fg="white", height=1)

#Placing buttons in the game
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_to_restart.grid(row=4, column=2)
#keeping restart button disabled
button_to_restart["state"] = "disabled"

#placing labels in the game
label_1.grid(row=0,columnspan=3)
label_2.grid(row=4,columnspan=2)

#declaring global variable to determine the players turn
Player_turn=0
game.mainloop()
