import os
import csv

# set file names (relative location does not work, so I use absolue path)

election_data_csv = "/Users/eneas/desktop/bootcamp/repository/my-repository/python-challenge/pypoll/Resources/election_data.csv"
output_file = "/Users/eneas/desktop/bootcamp/repository/my-repository/python-challenge/pypoll/Output/election_Analysis.csv"

# Variables and lists to store data

total_votes = 0    # This will hold the Month/Year information
candidate = ""
saved_candidate = ""
votes_candidate = 0
results =  []

print("")
print("---------------------------------")
print("Election Results")
print("---------------------------------")
# opening the file and processing each line, first is the header, so it will be ignored.
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # read header, and skip, as it is not needed in this code
    csv_header = next(csvreader)
    # now, read and deal with each row
    for row in csvreader:
        # count total votes
        total_votes = total_votes + 1
        # retrieve candidate name
        candidate = row[2]
        # Check for candidate sequence break
        if candidate != saved_candidate:
            # deal with the first time
            if saved_candidate == "":
                votes_candidate=1
                saved_candidate=candidate
            else:
                results.append([saved_candidate,votes_candidate,0])
                votes_candidate = 1
                saved_candidate = candidate
        else:
            votes_candidate=votes_candidate + 1
    results.append([saved_candidate,votes_candidate,0])

# Show total votes

print("Total Votes : " + str(total_votes))
print("---------------------------------")

# calculate percentages

for l in results:
    candidate_r = l[0]
    vote_r = l[1]
    vote_perc = vote_r / total_votes * 100
    l[2] = vote_perc
    print(l[0]+": ", str.format('{:.3f}',l[2]) + "%" , "(" + str(l[1]) + ")")

# Check for the winner

winner_count = 0
winner_name = ""
for l in results:
    if l[1] > winner_count:
        winner_count = l[1]
        winner_name = l[0]
print("---------------------------------")
print ("winner : " + winner_name)
print("---------------------------------")

# Now, store the results in a file

with open(output_file, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # writing the output
    csvwriter.writerow([""])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Total Votes : " + str(total_votes)])
    csvwriter.writerow(["---------------------------------"])
    for l in results:
        csvwriter.writerow([l[0]+": " + str.format('{:.3f}',l[2]) + "% (" + str(l[1]) + ")"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["winner : " + winner_name])
    csvwriter.writerow(["---------------------------------"])

# And that's all for the day!




