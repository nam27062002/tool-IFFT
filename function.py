from data import *
import re
def readfile(url):
    ans = []
    with open(url, 'r') as file:
        for line in file:
            ans.append(line.strip())
    return ans

def check_conflict(old_list, new_list):
    if len(old_list) != len(new_list):
        print("Not the same size")
        return
    conflict_count = 0
    for index, (old_value, new_value) in enumerate(zip(old_list, new_list)):
        if old_value != new_value:
            conflict_count += 1
            print(f"Conflict at {index}")
    if conflict_count == 0:
        print("There is no conflict")

def getActionType(url):
    with open(url, 'r') as file:
            for line in file:
                print(TaskActionType[line.strip()])
                


def extract_levels(text):
    matches = re.findall(r'Level (\d+)', text)
    levels = [int(match) for match in matches]
    return levels