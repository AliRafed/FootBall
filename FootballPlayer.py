class FootballPlayer:  # Defining the FootballPlayer class
    def __init__(self, player_id, name, team, nationality, height, position, experience):  # Constructor method to initialize player attributes
        self.id = player_id  # Assigning the player's ID
        self.name = name  # Assigning the player's name
        self.team = team  # Assigning the player's team
        self.nationality = nationality  # Assigning the player's nationality
        self.height = height  # Assigning the player's height
        self.position = position  # Assigning the player's position
        self.experience = experience  # Assigning the player's experience level

    def played_game(self):  # Method to increase the player's experience
        self.experience += 0.5  #Incrementing the player's experience by 0.5

    def get_id(self):  # Getter method for player's ID
        return self.id  # Returning the player's ID

    def get_name(self):  # Getter method for player's name
        return self.name  # Returning the player's name

    def get_team(self):  # Getter method for player's team
        return self.team  # Returning the player's team

    def get_nationality(self):  # Getter method for player's nationality
        return self.nationality  # Returning the player's nationality

    def get_height(self):  # Getter method for player's height
        return self.height  # Returning the player's height

    def get_position(self):  # Getter method for player's position
        return self.position  # Returning the player's position

    def get_experience(self):  # Getter method for player's experience
        return self.experience  # Returning the player's experience

    def __str__(self):  # Method to return a string representation of the player object
        return f"Player {self.name} (ID: {self.id})"  # Returning a formatted string representation
