import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S STATES GAME")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data=pandas.read_csv("50_states.csv")
state_list=data["state"].to_list()
x_coordinates=data["x"].to_list()
y_coordinates=data["y"].to_list()

scoreboard=0
score=turtle.Turtle()
score.hideturtle()
score.penup()
score.speed("fastest")
score.goto(0,280)
score.write(f"score: {scoreboard}",align="center",font=("Arial", 20, "normal"))


guessed_states=[]
game_is_on=True
while len(guessed_states)<50:
    answer_state = screen.textinput(title=f"{scoreboard}/50 states correct", prompt="What's another state's name?")
    if answer_state.title()=="Exit":
        break
    for state in state_list:
        if answer_state.title()==state:
            i=state_list.index(state)
            tim=turtle.Turtle()
            tim.speed("fastest")
            tim.hideturtle()
            tim.penup()
            tim.goto(x_coordinates[i],y_coordinates[i])
            tim.pendown()
            tim.write(state, align="center", font=("Arial",8, "normal"))
            score.clear()
            scoreboard += 1
            score.write(f"score: {scoreboard}", align="center", font=("Arial", 20, "normal"))
            guessed_states.append(state)

states_to_learn=[]
for item in state_list:
    if item not in guessed_states:
        states_to_learn.append(item)
data_dict={"states to learn":states_to_learn}
data=pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")


