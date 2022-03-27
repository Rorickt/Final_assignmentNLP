from allennlp_models.pretrained import load_predictor
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import csv, numpy as np
import logging


def predict_sents(challengeset, model, pred_num, word_num, variance=False):
    """Use an AllenNLP model to predict the semantic roles of each sentence in the challenge set

    Args:
        challengeset (list): List of strings containing sentences
        model (_type_): string representing the AllenNLP SRL model to use for the predictions
        pred_num (_type_): which predicate to use as base
        word_num (_type_): the index of the word to test its validation of

    Returns:
        list: list containing predicted labels, gold labels, full prediciton from model and erred predictions
    """

    ## remove output messages:
    logging.getLogger('allennlp.common.params').disabled = True 
    logging.getLogger('allennlp.nn.initializers').disabled = True 
    logging.getLogger('allennlp.modules.token_embedders.embedding').disabled = True 
    logging.getLogger('urllib3.connectionpool').disabled = True 
    logging.getLogger('allennlp.common.plugins').disabled = True 
    logging.getLogger('allennlp.common.model_card').disabled = True 
    logging.getLogger('allennlp.models.archival').disabled = True 
    logging.getLogger('allennlp.data.vocabulary').disabled = True 
    logging.getLogger('cached_path').disabled = True



    srl_predictor = load_predictor(model)

    full_preds = []
    faulty_preds = []
    predictions = []
    gold_labels = []

    with open(challengeset, 'r', encoding='utf-8') as file:
        file = csv.reader(file, delimiter='\t')
        if variance:
            
            for row in file:
                predicted_arg = ''
                prediction = srl_predictor.predict(row[0])
                full_preds.append(prediction)
                
                # get all tags
                pred_args = prediction['verbs'][pred_num]['tags']
                for tag in pred_args:
                    predicted_arg += tag.strip('B-').strip('I-')
                
                predictions.append(predicted_arg)
                gold_labels.append(row[1])
                if predicted_arg != row[1]:
                    faulty_preds.append(prediction['verbs'][pred_num]['description'])


        else:
            for row in file:
                prediction = srl_predictor.predict(row[0])
                full_preds.append(prediction)
                predicted_arg = prediction['verbs'][pred_num]['tags'][word_num].strip('B-').strip('I-')
                predictions.append(predicted_arg)
                gold_labels.append(row[1])
                if predicted_arg != row[1]:
                    faulty_preds.append(prediction['verbs'][pred_num]['description'])

    return predictions, gold_labels, full_preds, faulty_preds

def output_conf_matr(filepath, gold_args, pred_args):
    """_summary_

    Args:
        filepath (_type_): _description_
        gold_args (_type_): _description_
        pred_args (_type_): _description_
    """

    accuracy = str(accuracy_score(gold_args, pred_args))
    labels = sorted(set(pred_args))
    confusion = str(confusion_matrix(gold_args, pred_args, labels=labels)[0])

    with open(filepath, 'w', encoding='utf8') as f:
        f.write(accuracy)
        f.write('\n')
        f.write(str(labels))
        f.write(confusion)

    