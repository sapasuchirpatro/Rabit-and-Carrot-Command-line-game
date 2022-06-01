# import sys

# def checkPerformance(team_details, no_of_consecutive_losses):
#     print(f'\nFinding list of teams having {no_of_consecutive_losses} consecutive losses: ')
#     filtered_teams = []
#     for e in team_details:
#         if ('l' * no_of_consecutive_losses) in e[2]:
#             print(e[0].upper())
#             filtered_teams.append([e[0],e[1]])
#     if len(filtered_teams) == 0:
#         print(f'No teams found with consecutive {no_of_consecutive_losses} losses')
#         sys.exit()
#     return filtered_teams
    
# def avgPoints(filtered_teams):
#     sum_of_points = 0
#     for e in filtered_teams:
#         sum_of_points += e[1]
#     print('\nAverage Points of the filtered teams =', sum_of_points/len(filtered_teams))

                
# no_of_consecutive_losses = int(input("Enter a number 'n' to print the team name having 'n' consecutive losses: "))
# team_details = [['gt', 20, 'wwllw'], ['lsg', 18, 'wllww'], ['rr', 16, 'wlwll'], ['dc', 14, 'wwlwl'], ['rcb', 14, 'lwwll'], ['kkr', 12, 'lwwlw'], ['pbks', 12, 'lwlwl'], ['srh', 12, 'wllll'], ['csk', 8, 'llwlw'], ['mi', 8, 'lwlww']]
    
# filtered_teams = checkPerformance(team_details, no_of_consecutive_losses)
# avgPoints(filtered_teams)


# =======================================================================================

import sys

class TeamPerformace:
    def __init__(self, no_of_consecutive_wins_or_losses, team_details, loss_or_win, value):
        self.no_of_consecutive_wins_or_losses = no_of_consecutive_wins_or_losses
        self.team_details = team_details
        self.loss_or_win = loss_or_win
        self.value = value

    def checkPerformance(self):
        print(f'\nFinding the list of teams having {self.no_of_consecutive_wins_or_losses} consecutive {self.value}: ')
        self.filtered_teams = []
        for e in self.team_details:
            if (self.loss_or_win * self.no_of_consecutive_wins_or_losses) in e[2]:
                print(e[0].upper())
                self.filtered_teams.append([e[0], e[1]])
        if len(self.filtered_teams) == 0:
            print(f'No teams found with consecutive {self.no_of_consecutive_wins_or_losses} {self.value}')
            sys.exit()
    
    def avgPoints(self):
        sum_of_points = 0
        for e in self.filtered_teams:
            sum_of_points += e[1]
        print('\nAverage Points of the filtered teams =', sum_of_points/len(self.filtered_teams))
    
while(1):   
    loss_or_win = input("What do you want to find win or loss. Enter 'w' for win and 'l' for loss: ")
    if loss_or_win in ['w', 'l']:
        break
    else:
        print('Enter a valid input')

if loss_or_win == 'w':
    value = 'wins'
elif loss_or_win == 'l':
    value = 'losses'

while(1):
    no_of_consecutive_wins_or_losses = int(input(f"Enter a number 'n' to print the team names having 'n' consecutive {value}: "))
    if no_of_consecutive_wins_or_losses in [1,2,3,4,5]:
        break
    else:
        print('Enter a valid input')

team_details = [['gt', 20, 'wwllw'], ['lsg', 18, 'wllww'], ['rr', 16, 'wlwll'], ['dc', 14, 'wwlwl'], ['rcb', 14, 'lwwll'], ['kkr', 12, 'lwwlw'], ['pbks', 12, 'lwlwl'], ['srh', 12, 'wllll'], ['csk', 8, 'llwlw'], ['mi', 6, 'lwlww']]

tp = TeamPerformace(no_of_consecutive_wins_or_losses, team_details, loss_or_win, value)

tp.checkPerformance()
tp.avgPoints()