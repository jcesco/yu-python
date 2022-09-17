import turtle, pandas
from state_tracker import StateTracker


def check_guess(guess):
    if guess in all_states:
        state_data = data[data.state == guess]
        state_tracker.update_map(guess, int(state_data.x), int(state_data.y))
        return True


screen = turtle.Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_tracker = StateTracker()

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()

total_correct = 0
correct_guesses = []

while total_correct < len(data.state):
    answer_state = screen.textinput(title=f"{total_correct}/50 States Correct", prompt="What's another name?").title()
    if check_guess(answer_state):
        correct_guesses.append(answer_state)
        total_correct += 1

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./states_to_learn.csv")
        break



