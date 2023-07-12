import turtle
import pandas

screen=turtle.Screen()
screen.title("India States Game")
image='India-locator-map-blank.gif'
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("name_of_states.csv")
all_states=data.state.to_list()

guessed_states=[]

while len(guessed_states)<30:
    answer_state=screen.textinput(title=f'{len(guessed_states)}/29 Correct State and territory',prompt="What's another state's name?" ).title()

    if answer_state=='Exit':
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        states=pandas.DataFrame(missing_states)
        states.to_csv("Missed_states")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.x))
        t.write(answer_state)

