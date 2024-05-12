

class League:  # Defining the League class
    @staticmethod
    def match(team1, team2):  # Static method to simulate a match between two teams
        team1.match_preparation()  # Calling match_preparation() method for team1
        team2.match_preparation()  # Calling match_preparation() method for team2
        team2.after_match()
        team1.after_match()

        total_performance_team1 = team1.update_experience() + team1.get_cohesion()  # Calculating total performance of team1
        total_performance_team2 = team2.update_experience() + team2.get_cohesion()  # Calculating total performance of team2

        if total_performance_team1 > total_performance_team2:  # Comparing total performances

            return team1  # Returning team1 as winner
        elif total_performance_team2 > total_performance_team1:  # Comparing total performances

            return team2  # Returning team2 as winner
        else:  # If total performances are equal
            return None  # Returning None for draw
