# importing the csv module
import csv



    
#   Defining function to write data to csv file  
def write_csv(output_filename, rows):
    
    # writing to csv file
    with open(output_filename, 'w', newline='') as csvfile:
        
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        
        # writing the data rows
        csvwriter.writerows(rows)
        
    
    print(f'Data successfully stored in {output_filename}')
    
    
