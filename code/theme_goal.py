from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor

def create_theme_goal():
    editor = Editor()
    givings = ['phone','book','bottle','fork','spoon','sunglasses','charger','drink','gift', 'pen']
    verb = ['gave', 'handed', 'threw', 'slid']
    #### Prep passive capability templates
    ## BASE ARG
    template_passive_base0 = '{first_name1} {verb} {first_name2} the {givings}.'
    full_pass_base0 = editor.template(template_passive_base0, givings=givings, verb=verb, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/theme_goal/theme_goal_unmark1.csv', full_pass_base0.data, 'ARG2')


    template_passive_base0 = '{first_name1} {verb} the {givings} to {first_name2}.'
    full_pass_base0 = editor.template(template_passive_base0, givings=givings, verb=verb, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/theme_goal/theme_goal_mark1.csv', full_pass_base0.data, 'ARG2')

    


#### Predict sentences with AllenNLP with BiLSTM and BERT ####
def predict_theme_goal():
    files = ['theme_goal_mark1.csv', 'theme_goal_unmark1.csv']
    models = ['structured-prediction-srl','structured-prediction-srl-bert']
    for model in models:
        for file_ in files:
            if 'un' in file_:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/theme_goal/'+file_, model, 0, 2 )
                j_dumps('predictions/theme_goal/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/theme_goal/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/theme_goal/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
            else:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/theme_goal/'+file_, model, 0, 5 )
                j_dumps('predictions/theme_goal/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/theme_goal/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/theme_goal/'+file_+model[-4:]+'_results.txt', gold_labels, predictions) 



