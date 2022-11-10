# import CSV file
import os
import csv

csvpath = os.path.join('Resources', "election_data.csv")

# create dictionary for candidates
candidate_names = {}

# name variables
most_vote_count = 0
most_vote_name = ""
total_vote_count = 0

 
# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    print("Election Results")
    print("------------------------------")
 
 # loop through rows to get candidates, vote counts, and total vote count
    for row in csvreader:

        candidates = row[2]

        total_vote_count = total_vote_count + 1

        if candidates in candidate_names:
            candidate_names[candidates] = candidate_names[candidates] + 1

        else:
            candidate_names [candidates] = 1

# create folder to save txt file and txt file
file_to_save = os.path.join("analysis", "election_results.txt")
with open(file_to_save, "w") as txt_file:

# Print out title to terminal and to txt file
    output = 'Electron Results\n----------------------------- \n'

    txt_file.write(output)

   # loop through dictionary to determine most votes name and value  
    for key, value in candidate_names.items():
            
        if value > most_vote_count:
            most_vote_name = key
            most_vote_count = value


   #print output of total votes to terminal and txt file

    print(f"Total Votes : {total_vote_count}")
    print("------------------------------")
    txt_file.write('Total Votes :' + str(total_vote_count) +'\n')
    txt_file.write('------------------------------\n')

# print each candidate, percentage of votes, and total vote count to terminal and txt file
    for key, value in candidate_names.items():
        print (f"{key}: {round((value / total_vote_count)*100,3)}% ({value})")
        txt_file.write(f"{key}: {round((value / total_vote_count)*100,3)}% ({value})" "\n")

# print most vote name to terminal and txt file
    print("------------------------------")
    print(most_vote_name)
    print("------------------------------")
      
    output = (f"------------------------------ \n"
              f'{most_vote_name} \n'
              f"------------------------------")

    txt_file.write(output)

