import argparse
import logging
import sys
import os


# setup the logger parameters
dirpath = os.path.dirname(sys.argv[0])
log_path = dirpath + "./compare.log"
logging.basicConfig(filename=log_path,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')


def get_args():
    """Parse the passed arguments. If arguments are passed assign them to the file
       name variables. If not prompt the user to enter the file names."""
    # Define the description
    parser = argparse.ArgumentParser(
        description='Script compares two given file names')
    # Define the first argument
    parser.add_argument(
        '-f1', '--file1', type=str, help='First file to compare', required=False)
    # Define the second argument
    parser.add_argument(
        '-f2', '--file2', type=str, help='Second file to compare', required=False)
    args = parser.parse_args()
    if args.file1:
        fname1 = args.file1
        fname2 = args.file2
    else:
        fname1 = input("Enter the first filename: ")
        fname2 = input("Enter the second filename: ")
    # Return the file name variables
    return fname1, fname2


# Call the get_args() function to assign the filename variables
fname1,fname2 = get_args()

# Open file for reading in text mode (default mode)
try:
    f1 = open(fname1)
except IOError:
    print ('File1 error: There is no file named', fname1)
    sys.exit(1)
try:
    f2 = open(fname2)
except IOError:
    print ('File2 error: There is no file named', fname2)
    sys.exit(1)

# Print confirmation
print("-----------------------------------")
print("Comparing files ", " > " + fname1, " < " +fname2, sep='\n')
print("-----------------------------------")


# Read the first line from the files
f1_line = f1.readline()
f2_line = f2.readline()

# Initialize counter for line number
line_no = 1

# Loop if either file1 or file2 has not reached EOF
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    # Compare the lines from both file
    if f1_line != f2_line:
        
        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            print(">+", "Line-%d" % line_no, f1_line)
            logging.info(">+ Line-%d %s", line_no, f1_line)
        # otherwise output the line on file1 and mark it with > sign
        elif f1_line != '':
            print(">", "Line-%d" % line_no, f1_line)
            logging.info("> Line-%d %s", line_no, f1_line)
            
        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("<+", "Line-%i" % line_no, f2_line)
            logging.info("<+ Line-%d %s", line_no, f2_line)
        # otherwise output the line on file2 and mark it with < sign
        elif f2_line != '':
            print("<", "Line-%d" %  line_no, f2_line)
            logging.info("< Line-%d %s", line_no, f2_line)

        # Print a blank line
        print()

    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()


    #Increment line counter
    line_no += 1

# Close the files
f1.close()
f2.close()