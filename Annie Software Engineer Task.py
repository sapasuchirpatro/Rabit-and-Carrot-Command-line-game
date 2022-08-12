import random
import os

def generateMap():
    """Generate the Path"""
    path = ['r', 'O', '-', '-', 'c', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    random.shuffle(path)
    return path

def help():
    """Guide how to play the game"""
    print("Press 'a' to move left")
    print("Press 'd' to move right.")
    print("Press 'j' to jump over the hole from left to right and vice versa.")
    print("Press 'p' to pickup the carrot and put the carrot into the hole")

def indexOfR(path):
    """Find the index of the rabit"""
    if 'r' in path:
        return path.index('r')
    elif 'R' in path:
        return path.index('R')

def moveRight(path, index):
    """Move the rabbit towards right"""
    path[index], path[index+1] = path[index+1], path[index]
    return path

def moveLeft(path, index):
    """Move the rabbit towards left"""
    path[index], path[index-1] = path[index-1], path[index]
    return path

def jumpLeft(path, index):
    """Jump over the hole from right to left"""
    path[index], path[index-2] = path[index-2], path[index]
    return path

def jumpRight(path, index):
    """Jump over the hole from left to right"""
    path[index], path[index+2] = path[index+2], path[index]
    return path

def pickupCarrotFromLeft(path,index):
    """Pickup the carrot from left side"""
    path[index-1], path[index] = 'R', '-'
    return path

def pickupCarrotFromRight(path,index):
    """Pickup the carrot from right side"""
    path[index+1], path[index] = 'R', '-'
    return path

def moveRabit(path):
    """Control the rabit and put the carrot into the hole"""
    while True:
        index = indexOfR(path)
        command = input().lower()
        if index == 0 and path[index+1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
            elif path[index] == 'r':
                if command == 'j':
                    path = jumpRight(path, index)
        elif index == len(path)-1 and path[index-1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
            elif path[index] == 'r':
                if command == 'j':
                    path = jumpLeft(path, index)
        elif index == 0:
            if command == 'd':
                path = moveRight(path, index)
        elif index == len(path)-1:
            if command == 'a':
                path = moveLeft(path,index)
        elif path.index('O') == 0 and path[path.index('O')+1] != '-':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'd':
                    path = moveRight(path, index)
            elif path[index] == 'r':
                if command == 'd':
                    path = moveRight(path, index)
        elif path.index('O') == len(path)-1 and path[path.index('O')-1] != '-':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'a':
                    path = moveLeft(path,index)
            elif path[index] == 'r':
                if command == 'a':
                    path = moveLeft(path,index)
        elif path[index-1] == 'c':
            if command == 'p':
                path = pickupCarrotFromLeft(path, index)
            elif command == 'd':
                path = moveRight(path, index)
        elif path[index+1] == 'c':
            if command == 'p':
                path = pickupCarrotFromRight(path, index)
            elif command == 'a':
                path = moveLeft(path,index)
        elif path[index-1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'd':
                    path = moveRight(path, index)
            elif path[index] == 'r':
                if command == 'j' and path[index-2] == '-':
                    path = jumpLeft(path, index)
                elif command == 'j' and path[index-2] == 'c':
                    path[index-2], path[index] = 'R', '-'
                elif command == 'd':
                    path = moveRight(path, index)
        elif path[index+1] == 'O':
            if path[index] == 'R':
                if command == 'p':
                    return 'over'
                elif command == 'a':
                    path = moveLeft(path,index)
            elif path[index] == 'r':
                if command == 'j' and path[index+2] == '-':
                    path = jumpRight(path, index)
                elif command == 'j' and path[index+2] == 'c':
                    path[index+2], path[index] = 'R', '-'
                elif command == 'a':
                    path = moveLeft(path,index)
        else:
            if command == 'a':
                path = moveLeft(path,index)
            elif command == 'd':
                path = moveRight(path, index)
        os.system('cls')
        print(''.join(path))
        

        
def main():
    "Main Function"
    os.system('cls')
    print('+++++++++++++++++')
    print('+               +')
    print('+    WELCOME    +')
    print('+    TO THE     +')
    print('+     GAME      +')
    print('+               +')
    print('+++++++++++++++++')
    help()
    command = input("Press 's' to start the game\n").lower()
    while True:
        path = generateMap()
        os.system('cls')
        print(''.join(path))
        result = moveRabit(path)
        if result == 'over':
            os.system('cls')
            print('+++++++++++++++++')
            print('+               +')
            print('+   GAME OVER   +')
            print('+               +')
            print('+++++++++++++++++')
            yn = input("Do you want to play again. press 'y' for yes and 'n' for no \n").lower()
            if yn == 'y':
                continue
            elif yn == 'n':
                os.system('cls')
                print('Thanks for playing our game')
                break


if __name__ == '__main__':
    main()