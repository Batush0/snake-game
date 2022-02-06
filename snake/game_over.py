from data_manager import data_manager


class game_over:
    
    def __init__(self) -> None:
        
        self.x = data_manager().load('data_general\\snake.json')['pieces'][0][0]
        self.y = data_manager().load('data_general\\snake.json')['pieces'][0][1]

        self.x_range = data_manager().load('data_general\\data_general.json')['x_range']-1
        self.y_range = data_manager().load('data_general\\data_general.json')['y_range']-1

        self.highest_score = data_manager().load('data_general\\highest_score.json')['highest_score']
    
    
    def paste(self):
        
        self.score()
        exit()

    def control(self):

        if self.x <= 0 or self.y <=0 or self.x >= self.x_range or self.y >= self.y_range:
            self.paste()

    def score(self):
        
        score = data_manager().load('data_general\\snake.json')['len'] * 58

        print(f'highest score ever {self.highest_score}')
        print(f"your score : {score}")

        if score > self.highest_score:
            print('u just broke the record')
            print('yeeeyy !')
            print('well done')
            print(f'new record : {score}')
            data_manager().update('data_general\\highest_score.json',score,'highest_score')
        