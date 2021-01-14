#Scipt to take the CLI feed sort it and then utlilize data_pull.py

import cli
import data_pull

class Operate:
    def __init__(self,cli):
        self.selected_coin = cli.selected_coin
        self.time_interval = cli.time_interval
        self.need_graph = cli.need_graph

    #Function to handle coin selection and then feed main program
    def feed(self, data_pull):
        if len(self.selected_coin) == 1:
            feed_coin = self.selected_coin[0]
            data_pull.setup(feed_coin, self.time_interval)
            data_pull.get_data()
            data_pull.expand_df()
            data_pull.report()
            if self.need_graph == 'Yes':
                data_pull.create_plot()
            else:
                pass

        elif len(self.selected_coin) == 2:
            for coin in self.selected_coin:
                data_pull.setup(coin, self.time_interval)
                data_pull.get_data()
                data_pull.expand_df()
                data_pull.report()
                if self.need_graph == 'Yes':
                    data_pull.create_plot()
                else:
                    pass
                print("\n------------------------------------------\n\n")

        elif len(self.selected_coin) == 3:
            for coin in self.selected_coin:
                data_pull.setup(coin, self.time_interval)
                data_pull.get_data()
                data_pull.expand_df()
                data_pull.report()
                if self.need_graph == 'Yes':
                    data_pull.create_plot()
                else:
                    pass
                print("\n------------------------------------------\n\n")
        else:
            print("You're an idiot you have to select a coin... run it again because im not doing it for you")
