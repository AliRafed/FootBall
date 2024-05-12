import random

class FootballTeam:  # Defining the FootballTeam class
    def __init__(self, name, players):  # Constructor method to initialize team attributes and create player objects
        self.name = name  # Assigning the team's name
        self.players = players  # Assigning the team's players
        self.experience = self.update_experience()  # Updating the team's experience
        self.cohesion = None  # Initializing cohesion as None

    def match_preparation(self):  # Method to randomly generate cohesion for the team
        self.cohesion = round(random.uniform(1, 10), 2)  # Generating a random cohesion value between 1 and 10

    def after_match(self):  # Method to update the experience of all players after a match
        for player in self.players:  # Iterating over each player in the team
            player.played_game()  # Increasing the player's experience
        self.experience = self.get_experience()

    def update_experience(self):  # Getter method for team's experience
        return self.get_experience()  # Returning the team's experience

    def get_name(self):  # Getter method for team's name
        return self.name  # Returning the team's name

    def get_experience(self):  # Method to calculate and update the team's experience based on player experience
        total_experience = sum(player.get_experience() for player in self.players)  # Calculating the total experience of all players
        return round((total_experience / len(self.players)), 2)  # Returning the average experience of all players

    def get_cohesion(self):  # Getter method for team's cohesion
        return self.cohesion  # Returning the team's cohesion

    def __str__(self):  # Method to return a string representation of the team object
        return f"Team: {self.name}, Experience: {self.experience}, Cohesion: {self.cohesion}"  # Returning a formatted string representation
