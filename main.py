import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        new_states = []
        for state in all_states:
            if state not in guessed_states:
                new_states.append(state)
        new_data = pandas.DataFrame(new_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        state_data = data[data.state == answer_state]
        text.goto(int(state_data.x), int(state_data.y))
        text.write(state_data.state.item())





# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


screen.exitonclick()