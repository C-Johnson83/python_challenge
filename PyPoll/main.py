#import modules to allow path to files
import os
import csv

# this is the file path to the CSV file for reading, and the write path for the analysis text document
file_path = os.path.join('resources','election_data.csv')
write_path = os.path.join('analysis','election_results.txt')

# opens the file and allows the file to be read and skips the header
with open(file_path) as data:
    csvreader=csv.reader(data)
    header=next(csvreader)

#sets the counter for total ballots cast and counts total votes by candidate
    ballots = 0
    candidate_vote_count = {}
   
# each row adds to the total ballot count
    for row in csvreader:
        ballots += 1
        

 # if the candidate name is not found in the candidate vote count list then it gets added with a count of 1
 # if the candidiates name is found then it's count gets increased by 1
        if row[2] not in candidate_vote_count:
            candidate_vote_count[row[2]] = 1
        else:
             candidate_vote_count[row[2]] += 1
                
# finds the candidiate with the max vote count in the candidate vote count list and finds their name and count using the dictionary key
winner = max(candidate_vote_count, key=candidate_vote_count.get)

#determines the outputs for the print and write events. I had to separate them. Explained bellow
# sets output 1
output= (     
    "Election Results\n"
   f"-------------------------\n"
   f"Total Votes:   {str(ballots)}\n"
   f"-------------------------"
    )

#sets output 2
output2=(        
f"-------------------------\n" 
f"Winner: {winner}"
)

# prints the first output followed by the summary of candidates in the candidate vote count list
# I could not figure out how to get all of the prints into 1 output like I did on the PyBank challenge
print(output)

# this summarizes the candidates from the list with the percentage of their votes and their vote count
# I cannot figure out how to set this as its own variable to be used in the print statement
# I tried several times and ended up breaking the code. I didn't have a previous save so I had to start over and stuck with it
for candidate, votes in candidate_vote_count.items():
     print(candidate + ": " + "{:.3%}".format(votes/ballots) + "   (" +  str(votes) + ")")

#prints the second output
print(output2)

# now we are going to write the results to a text file into the analysis directiory 
# same as above, I had to write the outputs and candidate summary separate
f =  open(write_path, "w")

# writes the first output 
f.write(output)

# skips a line
f.write('\n')

# writes the candidiate summary and skips a line between candidates. This confused me for a while
# I was printing all the candidates in a row. I didnt have the f.write('\n') indented
for candidate, votes in candidate_vote_count.items():
    f.write(candidate  + ": " + "{:.3%}".format(votes/ballots) + "   (" +  str(votes) + ")")
    f.write('\n') 

# writes the second output      
f.write(output2) 






 





    





