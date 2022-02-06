from data_manager import data_manager
from feed import feed


class snake:
    def __init__(self) -> None:
        self.head = data_manager().load('data_general\\snake.json')['pieces'][0]
        self.feed = data_manager().load('data_general\\data_general.json')['feed']['coordinate']
        self.leng = data_manager().load('data_general\\snake.json')['len']
    
    def eat_control(self):
        
        if  self.head == self.feed:
            data_manager().update_s('data_general\\data_general.json',True,'feed','permision')
            data_manager().update('data_general\\snake.json',self.leng+1,'len')
            feed().main()

    
    def len_control(self):
        pieces = data_manager().load('data_general\\snake.json')['coordinates']
        calculating = -self.leng
        pieces = pieces[calculating:]
        data_manager().update('data_general\\snake.json',pieces,'pieces')

    def del_cordinate(self):
        coordinates = data_manager().load('data_general\\snake.json')['coordinates']
        calculating = -self.leng-4
        coordinates = coordinates[calculating:]
        data_manager().update('data_general\\snake.json',coordinates,'coordinates')
    

        





            