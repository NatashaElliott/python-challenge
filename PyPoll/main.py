import csv
import os
# Define variables and file paths
election_data=os.path.join(".","Resources","election_data.csv")
output_file = os.path.join(".","Analysis","election_data.txt")
votes = {}
totalvotes = 0
# Lists to store votes, County, and Candidates in order
candidates = []

# Define function to analyse election results
def electionanalysis():
    # Opening the CSV file and creating a dictionary
    with open(election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skipping/storing header rows
        next(csvreader, None)
        for rows in csvreader:
            # Create dictionary of candidates and their total votes
            if rows[2] in votes:
                votes[rows[2]] = votes[rows[2]]+1
            else:
                votes[rows[2]] = 1
    # Print total number of votes
    print("Election Results \n")
    print("----------------------------\n")
    print("Total Votes: " + str(sum(votes.values())) + "\n")
    print("----------------------------\n")
    # Cycle through dictionary and print all candidate names, their share of votes, and their total votes
    for candidate in votes:
        print(candidate + ": " + str(round(votes[candidate]/(sum(votes.values()))*100,3)) + "% (" + str(votes[candidate]) + ") \n" )
    print("----------------------------\n")
    # Print the winner of the election
    winner = max(votes, key=votes.get)
    print("Winner: " + winner + "\n")
    print("----------------------------\n\n")
    # Print results in file
    with open(output_file, "w", newline='') as datafile:
        datafile.write("Election Results \n")
        datafile.write("----------------------------\n")
        datafile.write("Total Votes: " + str(sum(votes.values())) + "\n")
        datafile.write("----------------------------\n")
        for candidate in votes:
            datafile.write(candidate + ": " + str(round(votes[candidate]/(sum(votes.values()))*100,3)) + "% (" + str(votes[candidate]) + ") \n" )
        datafile.write("----------------------------\n")
        datafile.write("Winner: " + winner + "\n")
        datafile.write("----------------------------\n\n")
    
    return
    
electionanalysis()