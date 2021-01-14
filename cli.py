#Trying to create a nice cli to use in order to use our tracker
from pyfiglet import Figlet
import inquirer
from pprint import pprint

class CLI:

    def interface(self):
        #Intro text
        f = Figlet(font='slant')
        print(f.renderText('CryptoTracker'))

        print("***************************************************")
        print("***   To confirm selection press Enter/Return   ***")
        print("***************************************************\n")

        #CLI Questions
        questions = [
            inquirer.Checkbox('coin',
                              message="Please select a cryptocurrency (use up/down arrow keys to select)",
                              choices=[
                                  ('Bitcoin', 'BTC'),
                                  ('Litecoin', 'LTC'),
                                  ('Etherium', 'ETH')],
                              default=['BTC']),

            inquirer.List('timeframe',
                          message="What timeframe would you like your data in",
                          choices=['1m', '5m', '15m', '1h', '6h', '1d'],
                          default='1d'),

            inquirer.List('graph',
                          message='Would you like to see the graph(s) as well?',
                          choices=['Yes', 'No'],
                          default='Yes'),
        ]

        #Returning the answers
        self.answers = inquirer.prompt(questions)
        #pprint(self.answers) #Incase you want to see the output of the cli

    def set_values(self):
        #Putting the answers into varibales to access later
        self.selected_coin = self.answers.get('coin')
        self.time_interval = self.answers.get('timeframe')
        self.need_graph = self.answers.get('graph')
