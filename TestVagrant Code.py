import sys

class TeamPerformace:
    def __init__(self, no_of_consecutive_wins_or_losses, team_details, loss_or_win):
        self.no_of_consecutive_wins_or_losses = no_of_consecutive_wins_or_losses
        self.team_details = team_details
        self.loss_or_win = loss_or_win

    def checkPerformance(self):
        """
        This will filter the teams having 'n' consecutive wins/losses and the team names will be 
        stored in an array(filtered_teams).
        """
        print(f'\nFinding the list of teams having {self.no_of_consecutive_wins_or_losses} consecutive {self.loss_or_win}: ')
        self.filtered_teams = []
        for e in self.team_details:
            if (self.loss_or_win[0] * self.no_of_consecutive_wins_or_losses) in e[2]:
                print(e[0].upper())
                self.filtered_teams.append([e[0], e[1]])
        if len(self.filtered_teams) == 0:
            print(f'No teams found with consecutive {self.no_of_consecutive_wins_or_losses} {self.loss_or_win}')
            sys.exit()
    
    def avgPoints(self):
        """
        This method will find the average points of all the filtered teams.
        """
        sum_of_points = 0
        for e in self.filtered_teams:
            sum_of_points += e[1]
        print('\nAverage Points of the filtered teams =', sum_of_points/len(self.filtered_teams))

# This loop will run until it gets a valid input i.e win or loss
while(1):
    # Asks input(win or loss) to find list of team having 'n' consecutive wins/losses
    loss_or_win = input("\nWhat do you want to find win or loss. Enter 'wins' for consecutive wins and 'losses' for consecutive losses: ").strip()
    if loss_or_win in ['wins', 'losses']:
        break
    else:
        print('Enter a valid input')


# This loop will run until it gets a valid input for 'n'
while(1):
    # Asks input to find how many consecutive wins/losses you want to find
    no_of_consecutive_wins_or_losses = int(input(f"\nEnter a number 'n' to print the team names having 'n' consecutive {loss_or_win}: ").strip())
    if no_of_consecutive_wins_or_losses in [1,2,3,4,5]:
        break
    else:
        print('Enter a valid input')

# Details of past 5 matches of the ipl teams
team_details = [['gt', 20, 'wwllw'], ['lsg', 18, 'wllww'], ['rr', 16, 'wlwll'], ['dc', 14, 'wwlwl'], ['rcb', 14, 'lwwll'], ['kkr', 12, 'lwwlw'], ['pbks', 12, 'lwlwl'], ['srh', 12, 'wllll'], ['csk', 8, 'llwlw'], ['mi', 6, 'lwlww']]

# Create an object
tp = TeamPerformace(no_of_consecutive_wins_or_losses, team_details, loss_or_win)

tp.checkPerformance()
tp.avgPoints()