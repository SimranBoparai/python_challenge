import os
import csv

## Define the CSV path
CSV_PATH = os.path.join('Resources', 'election_data.csv')

## Define indiciese for CSV columns
BALLOT_ID_INDEX = 0
COUONTY_INDEX = 1
CANDIDATE_INDEX = 2

## Change directory to find specific location of file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(__file__)


## Define the constants of the csv file
def read_csv_count_votes(csvpath):
    total_votes = 0
    candidate_votes = {}
    percentage_votes = {}
    highest_votes = -9999999
    election_winner = None

    ## Read the csv file
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)


        ## Read each row in the csv file and calculate the values
        for row in csvreader:
            total_votes += 1
            print(total_votes)

        ## Write a if statement to determine a list of candidates who received votes
            candidate = row[CANDIDATE_INDEX]
            if candidate not in candidate_votes:
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1

        ## Calculate to find the percentage of votes per candidate
        for candidate, vote in candidate_votes.items(): ## this code was debugged by the help of the learning assistant on slack
            percentage = (vote / total_votes) * 100
            percentage_votes[candidate] = percentage

        ## Write a if statement to determine the winner
        for candidate, votes in candidate_votes.items():
            if votes > highest_votes:
                highest_votes = votes
                election_winner = candidate
                

    ## Print each calculation 
    print(total_votes)
    print(candidate_votes)
    print(percentage_votes)
    print(election_winner)


    ## Call the functions to return the values 
    return total_votes, candidate_votes, percentage_votes, election_winner
            
total_votes, candidate_votes, percentage_votes, election_winner = read_csv_count_votes(CSV_PATH)


## Write a text file for the results
write_file= "Election_Results.txt"
with open(write_file, 'w') as file:
    file.write(f"Election Results\n") 
    file.write(f"------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n")
    file.write(f"------------------------\n")
    file.write(f"Winner: {election_winner}\n")
    file.write(f"------------------------\n")
    