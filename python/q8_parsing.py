#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.



import csv
def read_data(data):
    f = open(data,"rb")
    fball = csv.DictReader(f)
    for row in fball:
       print row


#want to find the lowest goals scores - highest goals scored against
def get_min_score_difference(data):
    f = open(data,"rb")
    fball = csv.DictReader(f)
    minDiff = float("inf")
    for row in fball:
        goals = int(row["Goals"])
        allowed = int(row["Goals Allowed"])
        diff = abs(goals-allowed)
        if diff < minDiff:
            minDiff = diff
            averagest_team = row["Team"]
    print minDiff



def get_team(data):
    f = open(data,"rb")
    fball = csv.DictReader(f)
    minDiff = float("inf")
    averagest_team = None
    for row in fball:
        goals = int(row["Goals"])
        allowed = int(row["Goals Allowed"])
        diff = abs(goals-allowed)
        if diff < minDiff:
            minDiff = diff
            averagest_team = row["Team"]
    print averagest_team

print read_data("football.csv")
print get_min_score_difference("football.csv")
print get_team("football.csv")
