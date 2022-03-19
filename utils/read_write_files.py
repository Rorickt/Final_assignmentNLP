import csv, json

def write_to_file(filepath, sentences, label):
    """Write checkList sentences and gold label to file

    Args:
        filepath (str): string to the location to save the file
        sentences (list): list of sentences as created by CheckList
        label (str): a string representing the gold label for the targeted SR 
    """
    
    with open(filepath, 'w', encoding='UTF8', newline='') as f:
        output = csv.writer(f, delimiter='\t')
        for sentence in sentences: 
            output.writerow([sentence, label])
    
def j_dumps(filepath, data):
    """dump the AllenNLP predictions to a .json

    Args:
        filepath (str): path to save the file to
        data (_type_): list of dictionaries to store in the json
    """
    with open(filepath, 'w') as mfile:
        json_item = json.dumps(data)
        mfile.write(json_item)