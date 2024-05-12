import random
import FootballPlayer
import FootballTeam
import League


class RealLife:

    # Create teams and players
    def __init__(self):
        self.counteries = ["Saudi Arabian", "Iraqi", "Emirati", "Qatari", "Omani", "Egyptian", "Bahraini", "Jordanian"]
        self.Teams = ["KSA", "IRQ", "UAE", "QAT", "OMA", "EGY", "BHR", "JOR"]
        self.teams = []


    def CreateTeams(self):

        for i in range(1, 9):  # Looping to create 8 teams
            players = [FootballPlayer.FootballPlayer(j, f"Player {j}___{self.Teams[i-1]}", self.Teams[i-1], self.counteries[i-1], random.randint(150, 220),  # Generating players for each team
                        random.choice(["Striker", "Defender", "Midfielder"]), random.uniform(0, 10))
                        for j in range(1, 12)]  # Creating 11 players for each team
            team = FootballTeam.FootballTeam(self.Teams[i-1], players)  # Creating a team object
            self.teams.append(team)  # Adding the team to the list

    def MatchSimulation(self):          # Simulate matches

        winners_round_1 = []  # Initializing an empty list to store winners from round 1
        winners_round_2 = []  # Initializing an empty list to store winners from round 2
        final_winner = []  # Initializing an empty list to store the final winner

        print(f"\nThe First Round")
        m = 1
        for i in range(0, len(self.teams), 2):  # Looping through teams in pairs
            team1 = self.teams[i]  # Getting the first team
            team2 = self.teams[i + 1]  # Getting the second team
            winner1 = League.League.match(team1, team2)  # Simulating a match between the two teams
            winners_round_1.append(winner1)  # Adding the winner to the list

            print(f"\nMatch {m} {team1.get_name()} VS. {team2.get_name()}")  # Printing match summary
            print(team1)    #To Show The summary of team 1
            print(team2)    #To Show The summary of team 2
            print("Winner: ************", winner1.get_name() if winner1 else "Draw", "************") # Printing the winner or "Draw" if it's a draw
            m += 1

        print(f"\nThe Second Round")
        m = 1
        for w in range(0, len(winners_round_1), 2):
            team1 = winners_round_1[w]  # Getting the first team
            team2 = winners_round_1[w + 1]  # Getting the second team
            winner2 = League.League.match(team1, team2)  # Simulating a match between the two teams
            winners_round_2.append(winner2)  # Adding the winner to the list
            print(f"\nMatch : {m} {team1.get_name()} VS. {team2.get_name()}")  # Printing match summary
            print(team1)  #To Show The summary of team 1
            print(team2)  #To Show The summary of team 2
            print("Winner: ************", winner2.get_name() if winner2 else "Draw","************")
            m += 1

        print(f"\nThe Final Round")
        for w in range(0, len(winners_round_2), 2):
            team1 = winners_round_2[w]  # Getting the first team
            team2 = winners_round_2[w + 1]  # Getting the second team
            winner3 = League.League.match(team1, team2)  # Simulating a match between the two teams
            final_winner.append(winner3)
            print(f"\nMatch : {m} {team1.get_name()} VS. {team2.get_name()}")  # Printing match summary
            print(team1)    #To Show The summary of team 1
            print(team2)    #To Show The summary of team 2
            print("Winner: ************", winner3.get_name() if winner3 else "Draw","************")



if __name__ == "__main__":  # Running the script if it's the main module
    simulation = RealLife()
    simulation.CreateTeams()
    simulation.MatchSimulation()




