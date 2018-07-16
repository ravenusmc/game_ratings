#This file will fix all of the issues with the user input to get it ready to scrape a site 

class Fix_Input():

    def transform_user_input_to_lowercase(self, gameTitle):
        gameTitle_lower = gameTitle.lower()
        return gameTitle_lower

    def add_dash_in_gameTitle(self, gameTitle):
        gameTitle_replaced = gameTitle.replace(" ", "_")
        return gameTitle_replaced