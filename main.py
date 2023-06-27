#this game would need to have sanitization of inputs and solutions for incorrect inputs


# Set up an instance of GameObject with name, appearance, feel, and smell
class GameObject:
    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell
    
    # returns the string describing object appearance
    def look(self):
        return f"\nYou look at the {self.name}. {self.appearance}\n"
    
    # Return string describing object feel
    def touch(self):
        return f"\nYou touch the {self.name}. {self.feel}\n"
    
    # Returns string describing object smell
    def sniff(self):
        return f"\nYou smell the {self.name}. {self.smell}\n"
    
# Set up an instance of Room with escape_code and [GameObject]game_objects    
class Room:
    def __init__(self, escape_code, game_objects):
        self.escape_code = escape_code
        self.game_objects = game_objects

    # returns whether the entered code is true or false 
    def check_code(self, code):
        return self.escape_code == code

    # returns the list of game objects present in the room
    def get_game_object_names(self):
        names = []
        for item in self.game_objects:
            names.append(item.name)
        return names
    
# Set up an instance of the escape room game
class Game:
    def __init__(self):
        self.attempts = 0
        objects = self.create_objects()
        self.room = Room(731, objects)

    # returns the 5 objects that are in the one room
    def create_objects(self):
        return[
            GameObject('Sweater',
                       "It's a blue sweater that had the number 12 stitched on it.",
                        'Someone has unstitched the second number, leaving only the 1.',
                        'The sweater smells of laundry detergent.'),
            GameObject('Chair',
                       "It's a wooden chair with only 3 legs.",
                       'Someone had deliberately snapped off one of the legs.',
                       'It smells like old wood.'),
            GameObject('Journal',
                        'The final entry states that time should be hours then minutes then seconds (H-M-S).',
                        'The cover is worn and several pages are missing.',
                        'It smells like musty leather.'),
            GameObject('Clock',
                       'The hour hand is pointing towards the soup, the minute hand towards the chair, and the second hand towards the sweater.',
                       'The battery compartment is open and empty.',
                       'It smells of plastic.'),
            GameObject('Bowl of Soup',
                       'It appears to be tomato soup.',
                       'It has cooled down to room temperature.',
                       'You detect 7 different herbs and spices.')
        ]
    
    # this defines the actual operation of the game
    def take_turn(self):
        if self.attempts < 3:
            prompt = self.get_room_prompt()
            selection = int(input(prompt))
            if selection >= 1 and selection <= 5:
                self.select_object(selection - 1)
                self.take_turn()
            else:
                if not self.guess_code(selection):
                    print(f"\nIncorrect code. {3 - self.attempts} attempts remaining.\n")
                    self.take_turn()
                else:
                    print(f"You have escaped the room.")
        else:
            print(f"Reload the game to try again\n")
    
    # this returns the information about the room to the user
    def get_room_prompt(self):
        prompt = "Enter the 3 digit lock code or type the number of an item to interact with:\n"
        names = self.room.get_game_object_names()
        index = 1
        for name in names:
            prompt += f"{index}. {name}\n"
            index += 1
        return prompt
    
    # this allows the user to select the objects
    def select_object(self, index):
        selected_object = self.room.game_objects[index]
        prompt = self.get_object_interaction_string(selected_object.name)
        interaction = input(prompt)
        clue = self.interact_with_object(selected_object, interaction)
        print(clue)

    # this allows the user to pick a method of interacting with an object
    def get_object_interaction_string(self, name):
        return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

    # this returns the string associated with the action the player took with the object in the room
    def interact_with_object(self, object, interaction):
        if interaction == "1":
            return object.look()
        elif interaction == "2":
            return object.touch()
        else:
            return object.sniff()
        
    # checks if the entered escape_code is True
    def guess_code(self, code):
        if self.room.check_code(code):
            return True
        else:
            self.attempts += 1
            return False




# game = Game()
# game.take_turn()



    
# unit testing should not require inputs/outputs from the user / server
# this is a sample of unit testing for this escape_room game
class RoomTests:
    def __init__(self):
        self.room_1 = Room(111, [
                        GameObject('Sweater',
                                "It's a blue sweater that had the number 12 stitched on it.",
                                    'Someone has unstitched the second number, leaving only the 1.',
                                    'The sweater smells of laundry detergent.'),
                        GameObject('Chair',
                                "It's a wooden chair with only 3 legs.",
                                'Someone had deliberately snapped off one of the legs.',
                                'It smells like old wood.')
        ])
        self.room_2 = Room(222, [])

    def test_check_code(self):
        print(self.room_1.check_code(111) == True)
        print(self.room_1.check_code(222) == False)
    
    def test_get_game_object_names(self):
        print(self.room_1.get_game_object_names() == ["Sweater","Chair"])
        print(self.room_2.get_game_object_names() == [])
        

# tests = RoomTests()
# tests.test_check_code()
# tests.test_get_game_object_names()
