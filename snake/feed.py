from data_manager import data_manager
import random


class feed :
    def __init__(self) -> None:
        
        self.permision = data_manager().load('data_general\\data_general.json')['feed']['permision']

        x_range = data_manager().load('data_general\\data_general.json')['x_range']
        y_range = data_manager().load('data_general\\data_general.json')['y_range']
        
        self.x = random.randint(1,x_range-2)
        self.y = random.randint(1,y_range-2)
        
    def main(self):
        
        if self.permision:
            
            data_manager().update_s('data_general\\data_general.json',[self.x,self.y],'feed','coordinate')
            data_manager().update_s('data_general\\data_general.json',False,'feed','permision')
