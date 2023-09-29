from enum import Enum

class COMPONENT(Enum):
    new_2_2 = 'new/component_2_2.txt'
    new_2_3 = 'new/component_2_3.txt'
    new_3_2 = 'new/component_3_2.txt'
    new_3_3 = 'new/component_3_3.txt'
    old_2_2 = 'old/component_2_2.txt'
    old_2_3 = 'old/component_2_3.txt'
    old_3_2 = 'old/component_3_2.txt'
    old_3_3 = 'old/component_3_3.txt'
    
class ACTION(Enum):
    new_2_2 = 'new/action_2_2.txt'
    new_2_3 = 'new/action_2_3.txt'
    new_3_2 = 'new/action_3_2.txt'
    new_3_3 = 'new/action_3_3.txt'
    old_2_2 = 'old/action_2_2.txt'
    old_2_3 = 'old/action_2_3.txt'
    old_3_2 = 'old/action_3_2.txt'
    old_3_3 = 'old/action_3_3.txt'
    
class TEST(Enum):
    test_1 = 'test/test1.txt'
    test_2 = 'test/test2.txt'
    test_3 = 'test/test3.txt'
    
TaskActionType = {
    "Earn Cash" : 1,
    "Buy Component": 2,
    "Upgrade Component":4,
    "Reach Upgrade Level": 8,
    "Resolve Fire Emergency": 16,
}

COMPONENT_TYPE = {'Firetruck': '1', 
                  'Bench': '1', 
                  'Firefighter Crew': '2', 
                  'Anything': '1', 
                  'Table': '1',
                  'Phone': '1', 
                  'Seats': '1', 
                  'Decoration': '1', 
                  'Toilet': '1', 
                  'Fill Station': '1', 
                  'Locker': '1', 
                  'Ambulance': '1', 
                  'Parademic Crew': '2', 
                  'Sink': '1', 'Storage': '1', 
                  'Water Pump': '1',
                  'Screen': '1', 
                  'Counter': '1', '': '3',
                  'Television': '1', 
                  'Darth Board': '1',
                  'Fridge': '1'}

VISUALIZATION_TYPE = {('Reach Upgrade Level', 'Firetruck'): '0', 
                      ('Buy Component', 'Bench'): '0', 
                      ('Buy Component', 'Firefighter Crew'): '2', 
                      ('Upgrade Component', 'Anything'): '3', 
                      ('Reach Upgrade Level', 'Table'): '0', 
                      ('Reach Upgrade Level', 'Phone'): '0', 
                      ('Buy Component', 'Seats'): '0', 
                      ('Buy Component', 'Decoration'): '0', 
                      ('Reach Upgrade Level', 'Toilet'): '0', 
                      ('Buy Component', 'Firetruck'): '0', 
                      ('Reach Upgrade Level', 'Locker'): '0', 
                      ('Reach Upgrade Level', 'Sink'): '0', 
                      ('Buy Component', 'Locker'): '0', 
                      ('Reach Upgrade Level', 'Bench'): '0', 
                      ('Buy Component', 'Storage'): '0', 
                      ('Reach Upgrade Level', 'Screen'): '0', 
                      ('Buy Component', 'Toilet'): '0', 
                      ('Buy Component', 'Table'): '0', 
                      ('Reach Upgrade Level', 'Counter'): '0', 
                      ('Reach Upgrade Level', 'Seats'): '0', 
                      ('Resolve Fire Emergency', ''): '4', 
                      ('Earn Cash', ''): '1', 
                      ('Reach Upgrade Level', 'Television'): '0', 
                      ('Reach Upgrade Level', 'Darth Board'): '0', 
                      ('Reach Upgrade Level', 'Storage'): '0', 
                      ('Upgrade Component', 'Firetruck'): '0', 
                      ('Reach Upgrade Level', 'Decoration'): '0', 
                      ('Reach Upgrade Level', 'Fridge'): '0', 
                      ('Buy Component', 'Ambulance'): '0', 
                      ('Buy Component', 'Parademic Crew'): '5', 
                      ('Reach Upgrade Level', 'Ambulance'): '0'}