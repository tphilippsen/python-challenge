# import CSV file
import os
import csv

csvpath = os.path.join('Resources', "election_data.csv")

candidate_names = {}

# variables
most_vote_count = 0
most_vote_name = ""
total_vote_count = 0

 
# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    print("Election Results")
    print("------------------------------")

    for row in csvreader:

        candidates = row[2]

        total_vote_count = total_vote_count + 1

        if candidates in candidate_names:
            candidate_names[candidates] = candidate_names[candidates] + 1

        else:
            candidate_names [candidates] = 1
file_to_save = os.path.join("analysis", "election_results.txt")
with open(file_to_save, "w") as txt_file:

    output = 'Electron Results\n-----------------------------'

    txt_file.write(output + '\n')
       
    for key, value in candidate_names.items():
            
        if value > most_vote_count:
            most_vote_name = key
            most_vote_count = value


    print(f"Total Votes : {total_vote_count}")
    print("------------------------------")
    txt_file.write('Total Votes :' + str(total_vote_count) +'\n')
    txt_file.write('------------------------------' + '\n')


    for key, value in candidate_names.items():
        print (f"{key}: {round((value / total_vote_count)*100,3)}% ({value})")
        txt_file.write(f"{key}: {round((value / total_vote_count)*100,3)}% ({value})" "\n")


    print("------------------------------")
    print(most_vote_name)
    print("------------------------------")
    output = '------------------------------' '\n' + most_vote_name +'\n------------------------------'
    txt_file.write(output)
# print("Charles Casper Stockhom : {  }")
# print("Diana DeGette : {candidate_2}")
# print("Raymon Anthony Doane : {candiadte_3}")
