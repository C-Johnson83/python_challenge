#import modules to allow path to files
import os
import csv

# this is the file path to the CSV file and is in the same directory as the main.py
load_file = os.path.join('resources','budget_data.csv')
write_path = os.path.join('analysis','budget_analysis.txt')
# opens the file and skips the header and allows the file to be read
with open(load_file) as data:
    csvreader=csv.reader(data,delimiter=',') 
    header=next(csvreader)

#sets the list to track total months, total revenue, and revenue change
    ttl_months = []
    ttl_rev = []
    rev_change = []
 
# Lopps through each row and adds to the total months and total revenue in the created lists   
    for row in csvreader:
        ttl_months.append(row[0])
        ttl_rev.append(int(row[1]))

# Loops through and gets the monthly revenue change and puts each change into the revenue change list
    for i in range (len(ttl_rev)-1):    
        rev_change.append(ttl_rev[i+1] - ttl_rev[i])      
        
# finds the minimum and maximum monthly changes in the revenue change list and defines them
    p_increase = max(rev_change)
    p_decrease = min(rev_change)

# finds the indexed entry in the revenue change list for the minimum and maximum monthly changes and defines them
    m_increase = rev_change.index(max(rev_change)) +1
    m_decrease = rev_change.index(min(rev_change)) +1

# Sets the output summary for the print and write statements 
output = ( 
        "Financial Analysis\n"
        f"-----------------------\n"
        f"Total Months: {len(ttl_months)}\n"
        f"Total: ${sum(ttl_rev)}\n"
        f"Average Change: ${round(sum(rev_change)/(len(rev_change)),2)}\n"
        f"Greatest Increaase in total_revenues: {ttl_months[m_increase]} (${(str(p_increase))})\n"
        f"Greatest Decrease in total_revenues: {ttl_months[m_decrease]} (${(str(p_decrease))})\n"
        )

# prints the output summary        
print(output)

# writes the text file in the same directory as the main.py and the CSV file
with open(write_path,'w') as file:
   file.write(output)
