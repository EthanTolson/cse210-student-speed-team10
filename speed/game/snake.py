import random as r
from game import constants
from game.actor import Actor
from game.point import Point

class Snake:
    def __init__(self):
        super().__init__()
        self._words = []
        self._segments = []
        self._inputs = []
        self.length = len(self._inputs)
        self._input_seg = []
        self.i = 0

        self.indexstartword = 0
        
        self._prepare()
    
    def get_all(self):
      
        return self._segments
    
    def get_input_all(self):
        return self._input_seg

    def move_words(self):
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            segment.move_next()
        
    def _add_input_segment(self, text, position, velocity):
   
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._input_seg.append(segment)

    def _add_segment(self, text, position, velocity):
    
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def refresh(self):            
        y = constants.MAX_Y
        v = Point(0,0)
        position = Point(self.i + 11, y)
        if not self.length == len(self._inputs):
            self._add_input_segment(self._inputs[-1], position, v)
            self.length += 1
            self.i += 1
        
    def get_last_input(self):
        if self.length != 0:
            return self._inputs[-1]
        else:
            return ""

    def reset_inputs(self):
        self._inputs.clear()
        self._input_seg.clear()
        self.length = 0
        self.i = 0
    
    def check_length(self):
        if self.length <= constants.MAX_X - 11:
            return False
        else:
            return True

        return False

    def compare_words(self):
        q = 0
        points = 0
        input_string = ""

        for n in range(self.indexstartword, len(self._inputs)):
            input_string = input_string + self._inputs[n]
                    

        for word in self._words:

            if str(word) in input_string:
                self.update_words(q)
                points += 1
                break

            q += 1

        return points

    def update_words(self, index):
        self._words[index] = constants.LIBRARY[r.randint(0,10000)]
        self._segments = []

        for word in self._words:
            x = r.randint(1, constants.MAX_X - 2)
            y = r.randint(1, constants.MAX_Y - 2)
            l = 0
            for letter in word:
                text = letter
                position = Point(x + l, y)
                velocity = Point(1, 0)
                self._add_segment(text, position, velocity)
                l += 1
        

    def _prepare(self):
        for i in range(0,5):
            self._words.append(constants.LIBRARY[r.randint(0,10000)])
        
        for word in self._words:
            x = r.randint(1, constants.MAX_X - 2)
            y = r.randint(1, constants.MAX_Y - 2)
            l = 0
            for letter in word:
                text = letter
                position = Point(x + l, y)
                velocity = Point(1, 0)
                self._add_segment(text, position, velocity)
                l += 1
        
    