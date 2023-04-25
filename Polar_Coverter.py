import csv
import math
import os

# make it so that the current directoy is the one where the script is
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# open the csv file
with open('train.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # open a new csv file to write to
    with open('train_polar.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(["r","theta","Category"])
        # loop through the rows in the csv file
        for line in csv_reader:
            # skip the first line (header)
            if line[0] == 'x1':
                continue
    
            # get the x and y coordinates
            x = float(line[0])
            y = float(line[1])

            # calculate the radius and angle
            r = math.sqrt(x**2 + y**2)
            theta = math.atan2(y, x)

            # write the new row to the new csv file
            csv_writer.writerow([r, theta, line[2]])

# make the same process for test data where the first column is id, the second is x1, the third is x2
with open('test_x.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('test_polar.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',', lineterminator='\n')
        csv_writer.writerow(["Id","r","theta"])
        for line in csv_reader:
            print
            if line[0] == 'Id':
                continue

            x = float(line[1])
            y = float(line[2])

            r = math.sqrt(x**2 + y**2)
            theta = math.atan2(y, x)

            csv_writer.writerow([line[0], r, theta])