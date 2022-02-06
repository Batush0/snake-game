import time
from data_default import data_default

from data_manager import data_manager
from feed import feed
from snake import snake
from map_update import update_map
from game_over import game_over
import keyboard


class the_loop:
    def __init__(self) -> None:
        
        data_default().main()
        
        self.sleep_for_fps = 1 / data_manager().load('data_general\\data_general.json')['fps']
        
        self.x = 2
        self.y = 3
        
        self.to_right = False
        self.to_up = False
        self.to_left = False
        self.to_down = False
        self.direction = 'right'

        self.leng = 1


    def loop(self):
        
        
        feed().main()

        while True:
            data_manager().update_s('data_general\\snake.json',[self.x,self.y],"pieces", 0 )
            
            data_manager().append_tuple('data_general\\snake.json',[[self.x,self.y]],'coordinates')
            
            snake().eat_control()
            
            snake().len_control()
            
            snake().del_cordinate()

            update_map().main()
          
            self.controls()
            
            game_over().control()
            
            time.sleep(self.sleep_for_fps)

    def controls(self):
        
        if keyboard.is_pressed('right') or keyboard.is_pressed('d') or keyboard.is_pressed('D') or self.to_right:
                if self.direction != 'left':
                    self.direction = 'right'
                    self.to_down , self.to_up = False,False
                    self.to_right = True
                    self.y +=1
                    
        if keyboard.is_pressed('left') or keyboard.is_pressed('a') or keyboard.is_pressed('A') or self.to_left:
            if self.direction != 'right':
                self.direction = 'left'
                self.to_down , self.to_up = False,False
                self.to_left = True
                self.y-=1

        if keyboard.is_pressed('up') or keyboard.is_pressed('w') or keyboard.is_pressed('W') or self.to_up:
            if self.direction != 'down':
                self.direction = 'up'
                self.to_left , self.to_right = False , False
                self.to_up = True
                self.x-=1

        if keyboard.is_pressed('down') or keyboard.is_pressed('s') or keyboard.is_pressed('S') or self.to_down:
            if self.direction != 'up':
                self.direction = 'down'
                self.to_left , self.to_right = False , False
                self.to_down = True
                self.x+=1
