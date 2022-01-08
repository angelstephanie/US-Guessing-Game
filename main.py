import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

file = pandas.read_csv("50_states.csv")
data = file.to_dict()
guessed_state = []
unguessed_state = pandas.read_csv("50_states.csv")["state"].to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state's name").title()
    for state in data["state"]:
        if answer_state == data["state"][state]:
            guessed_state.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x_cor = data["x"][state]
            y_cor = data["y"][state]
            t.goto(x_cor, y_cor)
            t.write(answer_state)
            unguessed_state.remove(answer_state)
    if answer_state == "Exit":
        break

missing_state = pandas.DataFrame(unguessed_state)
missing_state.to_csv("missing_state.csv")
screen.exitonclick()
