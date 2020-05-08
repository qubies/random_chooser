import json
import random
from time import sleep
from tabulate import tabulate
from PyInquirer import prompt, print_json
from os import system
import cowsay

{
    "type": "input",
    "name": "first_name",
    "message": "What's your first name",
}

menu_choices = [
    "Choose Without Replacement",
    "Choose with Replacement",
    "List Available Victims",
    "Add a Victim",
    "Remove a Victim",
    "Reset",
    "Quit",
]

colors = [
    "\u001b[31;1m",
    "\u001b[32;1m",
    "\u001b[33;1m",
    "\u001b[34;1m",
    "\u001b[35;1m",
    "\u001b[36;1m",
    "\u001b[37;1m",
]
reset_color = "\u001b[0m"


def select_from_list(l, message="Choose:"):
    vic_menu = [{"type": "rawlist", "name": "vic", "message": message, "choices": l,}]
    return prompt(vic_menu)["vic"]


def list_victims():
    print("--------------- Current Choices -----------------")
    print(tabulate(enumerate(current_list)))
    print("---------------   All Choices   -----------------")
    print(tabulate(enumerate(choices)))


def reset():
    global current_list
    current_list = list(choices)


def sample():
    if len(current_list) <= 0:
        reset()
    if len(current_list) <= 0:
        print("Sorry, you'll have to add some choices first")
        return None
    return random.choice(current_list)


def save():
    with open("choices.json", "w") as json_file:
        json.dump(choices, json_file)


def add_victim(name):
    choices.append(name)
    current_list.append(name)
    save()


def remove_victim(name, permanatly):
    current_list.remove(name)
    if permanatly:
        choices.remove(name)
        save()


def temp_remove_victim(name):
    current_list.remove(name)


with open("choices.json") as json_file:
    choices = json.load(json_file)

reset()


def announce_victim(victim, build_suspense=3, update_interval=0.2):
    build_suspense = int(build_suspense / update_interval)
    for x in range(1, build_suspense + 1):
        print("\r" + ("." * (x % 6) + "         "), end="")
        sleep(update_interval)
    print()
    cowsay.tux(f"{random.choice(colors)}{victim}{reset_color} was Chosen!!")
    print()
    print()


while True:
    answer = select_from_list(menu_choices, message="Main")

    if answer == "Choose Without Replacement":
        victim = sample()
        if victim != None:
            current_list.remove(victim)
            announce_victim(victim)

    elif answer == "Choose with Replacement":
        victim = sample()
        if victim != None:
            announce_victim(victim)

    elif answer == "List Available Victims":
        list_victims()

    elif answer == "Add a Victim":
        new_vic = input("Please enter the victim: ")
        add_victim(new_vic)

    elif answer == "Remove a Victim":
        dead_vic = select_from_list(
            choices, message="Choose the Victim that has to go...."
        )
        perm = select_from_list(["Yes", "No"], message="Permanently??")
        remove_victim(dead_vic, perm == "Yes")

    elif answer == "Reset":
        reset()

    elif answer == "Quit":
        break
    input("Press enter to continue.....")
    system("clear")

