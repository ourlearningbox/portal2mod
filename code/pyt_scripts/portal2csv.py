"""
    Script to convert portal2 logs to more practical csv files
    
    using from outside
    import portal2csv
    portal2csv.convert(input_filename, output_filename)
"""
import csv
from pathlib import Path

import re

def file_exists(absolute_path):
    input_file = Path(absolute_path)
    try:
        input_file.resolve(strict=True)
    except FileNotFoundError:
        return False
    else:
        return True

def convert(input_filename, output_filename=None, must_override=False):
    def in_between(lookforward, lookbehind):
        """
        https://docs.python.org/3/library/re.html#regular-expression-syntax
        """
        return re.search('(?<='+lookforward+')(.*)(?='+lookbehind+')', line)[0]

    def column_index_from_header(header):
        """
        If the header already exists return its index, else return -1
        """
        try:
            return events_matrix[0].index(header)
        except ValueError:
            return -1

    def na_fill(line, column_index):
        """
        Fill empty spaces in event_matrix[current_line] with "NA".
        Starts from the last position of that matrix line until the index of the header corresponding to that value
        """
        for _ in range(len(events_matrix[line]), column_index):
            events_matrix[line] += ['NA']

    if output_filename == None:
        filename, fileext = os.path.splitext(input_filename)
        output_filename = filename+'.csv' 
     
    if file_exists(output_filename):
        if not must_override:
            print('Output file exists, cannot proceed:' + output_filename)
            return

    if file_exists(input_filename):
        # matrix to store game events from the log file
        events_matrix = [['Event', 'Time']]
        # opening the log file
        with open(input_filename) as input_file:
            line = input_file.readline()
            current_line = 0
            while line:
                if line.startswith('Game event'): # creates a new line in the matrix for each Game Event
                    event = in_between('Game event "', '", Tick')
                    tick = in_between('", Tick ', ':')
                    current_line += 1
                    events_matrix += [[event, tick]];
                    line = input_file.readline()
                    while line.startswith('-'): # values of a Game Event starts with '-' in the log file
                        current_header = in_between('- "', '" = "')
                        current_value = in_between('" = "','"')
                        column_index = column_index_from_header(current_header)
                        if column_index >= 0: # if the current header already exists
                            na_fill(current_line, column_index)
                            events_matrix[current_line] += [current_value] # add the current_value in the events_matrix
                        else:                 # if the current header  doesn't exists 
                            events_matrix[0] += [current_header]
                            na_fill(current_line, column_index)
                            events_matrix[current_line] += [current_value] # add the current_value in the events_matrix
                        line = input_file.readline()
                line = input_file.readline()
            input_file.close()

        current_line = 1
        number_of_columns = len(events_matrix[0])
        for line in range(1,len(events_matrix)):
            na_fill(line, number_of_columns) # fill in remaining empty spaces with "NA"

        with open(output_filename, 'w', newline='') as csvFile: # write the event_matrix in a csv file
            writer = csv.writer(csvFile)
            for row in events_matrix:
                writer.writerow(row)
            csvFile.close()

        print('Create' +' '+ output_filename)
    else:
        print(input_filename +' '+ 'not found.')

if __name__ == '__main__':
    import os
    from glob import glob

    def get_files(src_directory):
        target_filters = ['*.txt']
        glob_lists = [glob(os.path.join(src_directory, tf)) for tf in target_filters]
        return [sorted(glob_list) for glob_list in glob_lists][0]

    basepath = os.path.dirname(os.path.abspath(__file__))
    input_filepath = os.path.join(basepath, 'data')
    data_files = get_files(input_filepath)

    for file in data_files:
        convert(file, None, True)
