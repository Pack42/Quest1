import csv
# Create dictionary to store output info
departments = {}
# Open the csv in read mode and label as file
with open('city-of-seattle-2012-expenditures-dollars.csv', mode ='r') as file:    
       # Use dict reader to convert csv to dict
       csvDict = csv.DictReader(file)
       # Loop through the dictionary
       for line in csvDict:
            # Only include departments that have data for 2012
            if line['2012 Actual'] != '':
                  # Add department to output dictionary if it is not already in the dictionary
                  if line['Department'] not in departments:
                        # Initialize value as the 2012 actual spending
                        departments[line['Department']] = int(line['2012 Actual'])
                  else:
                        # Add expenses together if multiple exist
                        departments[line['Department']] += int(line['2012 Actual'])
# Loop through output dictionary and print out results
for department in departments:
      print(department + " " + format(departments[department], ","))