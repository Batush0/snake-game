import re
from data_manager import data_manager
class update_map:
    def __init__(self) -> None:
        self.borders = data_manager().load('data_map\\map_border.json')['borders']
        self.grasses = data_manager().load('data_map\\map_grasses.json')['grasses']
        self.whole = data_manager().load("data_map\\map_whole.json")['whole']
        self.feed = data_manager().load('data_general\\data_general.json')['feed']['coordinate']
        self.snake = data_manager().load('data_general\\snake.json')['pieces']
        self.len = data_manager().load('data_general\\snake.json')['len']
    
    def main(self):

        front_end = ''
        for single_data in self.whole:
            
            if single_data in self.borders:
                piece = '/'
                front_end+=piece
                continue
            
            
            elif self.snake_control(single_data):
                piece =  'O'
                front_end+= piece
                continue
                
            
            elif single_data == self.feed:
                piece = '#'
                front_end+=piece
                continue
            
            
            elif single_data in self.grasses:
                piece = '.'
                front_end+=piece
                continue
            

        print(front_end)

    def snake_control(self,data):
        
        for turn in range(self.len):
            if data_manager().load('data_general\\snake.json')['pieces'][turn] == data:
                return True

