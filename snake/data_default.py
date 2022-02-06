import json
import random

from data_manager import data_manager


class data_default:

    def main(self):
        self.general()
        self.snake()
        self.score()
        self.map()

    def general(self):
        data = {
                    "fps":99999,
                    "feed":{
                        "permision":True,
                        "coordinate":None
                    }
                    
                }
        file = open('data_general\\data_general.json','w')
        json.dump(data,file)
    
    
    def map(self):
        x_range = 20
        y_range = 35

        whole = []
        borders = []
        grasses = []
        
        for ana in range(x_range):
            for ic in range(y_range):
                whole.append([ana,ic])
        
        for i in whole:
            if i[0] == 0 or i[0] == x_range-1 or i[1] == 0 or i[1] == y_range-1:
                borders.append(i)
            else:
                grasses.append(i)
            
        data_manager().update('data_map\\map_whole.json',whole,'whole')
        data_manager().update('data_map\\map_border.json',borders,'borders')
        data_manager().update('data_map\\map_grasses.json',grasses,'grasses')
        data_manager().update('data_general\\data_general.json',x_range,'x_range')
        data_manager().update('data_general\\data_general.json',y_range,'y_range')

    
    def snake(self):
        data = {
            "coordinates":[[]],
            "pieces":[[]],
            "len":1,
        }
        file = open('data_general\\snake.json','w')
        json.dump(data,file)

    def score(self):
        data = {
            "score":0
        }
        file = open('data_general\\score.json','w')
        json.dump(data,file)

