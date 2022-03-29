from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor

def create_roleset():
    editor = Editor()
    building= ['store','house','hotel','shop', 'pharmacy', 'room', 'station',
    'airport','boat','harbor','school','cafe', 'restaurant', 'university']
    item= ['phone','pen','knife','fork', 'spoon', 'charger', 'headphones',
    'bottle','keys','wallet','bag','beanie', 'backpack', 'book']
    
    ###### Manner addition [variance test] ######
    roleset_template1 = '{first_name} left the {building}.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    roleset_leave1 = editor.template(roleset_template1, building=building, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/roleset/roleset_leave1.csv', roleset_leave1.data, 'ARG1')
    
    ###### Manner addition [variance test] ######
    roleset_template2 = '{first_name} left the {building} to {first_name1}.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    roleset_leave2 = editor.template(roleset_template2, building=building, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/roleset/roleset_leave2.csv', roleset_leave2.data, 'ARG1')
    write_to_file('challenge_sets/roleset/roleset_leave3.csv', roleset_leave2.data, 'ARG2')

    ###### Manner addition [variance test] ######
    roleset_template2 = '{first_name} left the {item} to {first_name1}.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    roleset_leave2 = editor.template(roleset_template2, item=item, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/roleset/roleset_leave4.csv', roleset_leave2.data, 'ARG1')
    write_to_file('challenge_sets/roleset/roleset_leave5.csv', roleset_leave2.data, 'ARG2')

#### Predict sentences with AllenNLP with BiLSTM and BERT ####
def predict_roleset():
    files = ['roleset_leave1.csv', 'roleset_leave2.csv', 'roleset_leave3.csv', 'roleset_leave4.csv', 'roleset_leave5.csv']
    models = ['structured-prediction-srl', 'structured-prediction-srl-bert']
    for model in models:
        for file_ in files:
            if '3' in file_ or '5' in file_:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/roleset/'+file_, model, 0, 5)
                j_dumps('predictions/roleset/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/roleset/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/roleset/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
            else:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/roleset/'+file_, model, 0, 3)
                j_dumps('predictions/roleset/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/roleset/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/roleset/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)

