"""
BULLS & COWS

projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author: Petr Vodák
email: vodak.petr10@seznam.cz
discord: Pitrix#0619


Poznámka:   Vím, že bych zde už mohl uplatnit rozdelení do určitých funkcí,
            ale stále je to pro obtížnější na vytvoření, proto jsem se uchýlil
            k tomuto jednotnému zápisu. Nicméně na tom pracuji a určitě
            do budoucna plánuji projekt přepracovat na "vyšší úrověň". Každopádně
            doufám, že nyní je ke splnění tohoto projektu dostatečná i tato verze.
"""

import random

# úvodní text
print("""Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")

separator = '-'*47

# vygenerování čtyřciferného čísla s unikátními ciframi
generating = True
generated_number = list()
while generating:
    number = random.randrange(1,10)
    if number in generated_number:
        continue
    else:
        generated_number.append(number)

    if len(generated_number) == 4:
        generating = False
    else:
        continue


# přiřazení indexů k vygenerovanému číslu
modified_number = dict()
for index, number in enumerate(generated_number,1):
    modified_number[index] = number

key_number = list(modified_number.keys())
val_number = list(modified_number.values())


# hádání čísla
game_running = True
attemps = 0
while game_running:
    guess_number = input(">>> ")
    attemps += 1

    # ošetření, zda se jedná o 4 ciferné číslo
    if guess_number.isnumeric():
        if int(guess_number) in range(1000,10000):
            pass
        else:
            print("Wrong format! Enter 4 digit number..", separator, sep='\n')
            continue
    else:
        print("Not a valid number!", separator, sep='\n')
        continue
    
    # ošetření vstupu, aby byla každá číslice unikátní
    guess_number_list = list()

    for number in guess_number:
        if number not in guess_number_list:
            guess_number_list.append(number)
    if len(guess_number_list) != 4:
        print("Enter 4 (unique) digit number!", separator, sep='\n')
        continue

    # přiřazení indexu tipovanému číslu
    modified_guess = dict()
    for number in guess_number:
        guess_number_list.append(int(number))

    for index, number in enumerate(guess_number_list,1):
        modified_guess[index] = int(number)

    # zjisteni, zda je cislice stejna jako v libovolna v hadanem cisle
    key_guess = list(modified_guess.keys())
    val_guess = list(modified_guess.values())

    cows = 0
    bulls = 0
    
    # pokud ANO, pricte 1 k hodnote bulls nebo cows (podle typu uhodnuti)
    for number in guess_number_list:
        if number in generated_number:
            if key_guess[val_guess.index(number)] == key_number[val_number.index(number)]:
                bulls += 1
            else:
                cows += 1
        else:
            continue
    
    # ukonceni v pripade uhodnuti -> 4x bull + pocet pokusu
    if bulls == 4:
        print("Correct, you've guessed the right number",
        f"in {attemps} guesses!", separator, sep='\n')
        
        # podle poctu pokusu ohodnoceni hry
        if attemps <=5:
            print("That's amazing!")
        elif attemps >5 and attemps <=15:
            print("That's average.")
        else:
            print("That's not so good..")
        exit()
    
    
    # gramaticky správný výpis bull/s a cow/s
    if bulls == 1 and cows == 1:
        print(f"{bulls} bull, {cows} cow", separator, sep='\n')
    elif bulls == 1:
        print(f"{bulls} bull, {cows} cows", separator, sep='\n')
    elif cows == 1:
        print(f"{bulls} bulls, {cows} cow", separator, sep='\n')
    else:
         print(f"{bulls} bulls, {cows} cows", separator, sep='\n')