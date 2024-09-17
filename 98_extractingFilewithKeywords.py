""" Created on Wed Sep 11 15:26:33 2024 @ author: Doris Santiago """
#This code helps to isolate data files depending on the keywords generated. It is useful to seperate files based on names.
# change keyword as needed
# I isolated all the files with another code and used that non-sorted text file to be processed by this code.

import os

#Add the path of file generated with code 99 and the set of words that you are targeting, the target keywords and the location of the folder where you would want all your files to be saved.
input_file = r'C:\Users\Doris Santiago\Documents\Experiments\Ex-vivo\EphysAnalysis\DataForAnalysis\all_abf_file_path.txt'
keyword_sets = [('enter your first keyword', 'enter your second keyword')]
output_folder = r'C:\Users\Doris Santiago\Documents\Experiments\Ex-vivo\EphysAnalysis\DataForAnalysis'


def filter_paths_by_keywords(input_file, keyword_sets, output_folder):
    if not os.path.isdir(output_folder):
        print(f"The output folder path '{output_folder}' is not valid.")
        return
    
    
    with open(input_file, 'r') as file:                   # Read paths from the input file
        paths = file.readlines()
        
    keyword_paths = {tuple(keywords): [] for keywords in keyword_sets}

    # Filter paths based on keyword sets
    for path in paths:
        path = path.strip()
        for keywords in keyword_sets:
            if all(keyword.lower() in path.lower() for keyword in keywords):
                keyword_paths[tuple(keywords)].append(path)

    for keywords, filtered_paths in keyword_paths.items():
        if filtered_paths:
            output_file = os.path.join(output_folder, f"paths_with_{'_'.join(keywords)}.txt")
            with open(output_file, 'w') as file:
                file.write('\n'.join(filtered_paths))
            print(f"Paths with keywords {keywords} have been written to '{output_file}'")


filter_paths_by_keywords(input_file, keyword_sets, output_folder)