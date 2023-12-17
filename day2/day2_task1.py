import re 

# Game 1: 10 green, 5 blue; 1 red, 9 green, 10 blue; 5 blue, 6 green, 2 red; 7 green, 9 blue, 1 red; 2 red, 10 blue, 10 green; 7 blue, 1 red
# 12 red cubes, 13 green cubes, and 14 blue
red_cube = 12 
green_cube = 13 
blue_cube = 14

def get_number_behind_word(): 
    pass

def main(): 
    
    file = open("day2/input.txt", "r") 
    
    sum_of_games = 0
    
    pattern = re.compile(r'Game (\d+):(?: (\d+) red,)?(?: (\d+) green,)?(?: (\d+) blue,)?')
    
    for line in file:
        amount_of_cubes_per_round = []
        matches = pattern.findall(line)
        print(matches) 
        break
        

if __name__ == "__main__": 
    main() 
    
def re_test_with_fix_pattern(): 
    data = "Game 1: 4 red, 10 green, 5 blue; Game 2: 3 red, 5 green, 6 blue"

    # Definiere das Muster für die Extraktion
    pattern = re.compile(r'Game (\d+): (\d+) red, (\d+) green, (\d+) blue')

    # Suche nach Übereinstimmungen im Text
    matches = pattern.findall(data)
    print(matches)

    # Extrahiere die gewünschten Daten
    for match in matches:
        game_number, red_count, green_count, blue_count = map(int, match)
        print(f"Game {game_number}: {red_count} red, {green_count} green, {blue_count} blue")

def re_test_without_fix_pattern(): 
    import re

    data = "Game 1: 4 red, 10 green, 5 blue; Game 2: 3 red, 5 green, 6 blue, 2 red"

    # Definiere das Muster für die Extraktion
    pattern = re.compile(r'Game (\d+):(?: (\d+) red,)?(?: (\d+) green,)?(?: (\d+) blue,)?')

    # Suche nach Übereinstimmungen im Text
    matches = pattern.findall(data)

    # Extrahiere die gewünschten Daten
    for match in matches:
        game_number, red_count, green_count, blue_count = map(lambda x: int(x) if x else 0, match)
        print(f"Game {game_number}: {red_count} red, {green_count} green, {blue_count} blue")