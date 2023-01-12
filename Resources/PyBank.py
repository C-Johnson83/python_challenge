
import os
import csv

load_file = os.path.join('budget_data.csv')
write_file = os.path.join('budget_analysis.txt')

with open(load_file) as data:
    csvreader=csv.reader(data,delimiter=',') 
    header=next(csvreader)

    ttl_months = []
    ttl_rev = []
    rev_change = []
    m_change = []
    
    for row in csvreader:
        ttl_months.append(row[0])
        ttl_rev.append(int(row[1]))
    for i in range (len(ttl_rev)-1):    
        rev_change.append(ttl_rev[i+1] - ttl_rev[i])
       


        previous_rev = int(row[1])
        rev_change = rev_change + []
        

    p_increase = max(rev_change)
    p_decrease = min(rev_change)

    m_increase = rev_change.index(max(rev_change)) +1
    m_decrease = rev_change.index(min(rev_change)) +1  
    Average = {sum(rev_change)/(len(rev_change)),2}

output = ( 
"Financial Analysis\n"
f"-----------------------\n"
f"Total Months: {len(ttl_months)}\n"
f"Total: ${sum(ttl_rev)}\n"
f"Average Change: ${round(sum(rev_change)/(len(rev_change)),2)}\n"
f"Greatest Increaase in total_revenues: {ttl_months[m_increase]} (${(str(p_increase))})\n"
f"Greatest Decrease in total_revenues: {ttl_months[m_decrease]} (${(str(p_decrease))})\n"
)
print(output)

with open(write_file,'w') as analysis:
    analysis.write(output)
