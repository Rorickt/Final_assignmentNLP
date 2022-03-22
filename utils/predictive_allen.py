from allennlp_models.pretrained import load_predictor
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import csv, numpy as np


def predict_sents(challengeset, model, pred_num, word_num):
    """Use an AllenNLP model to predict the semantic roles of each sentence in the challenge set

    Args:
        challengeset (list): List of strings containing sentences
        model (_type_): string representing the AllenNLP SRL model to use for the predictions
        pred_num (_type_): which predicate to use as base
        word_num (_type_): the index of the word to test its validation of

    Returns:
        list: list containing predicted labels, gold labels, full prediciton from model and erred predictions
    """
    srl_predictor = load_predictor(model)

    full_preds = []
    faulty_preds = []
    predictions = []
    gold_labels = []

    with open(challengeset, 'r', encoding='utf-8') as file:
        file = csv.reader(file, delimiter='\t')
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
    cm = confusion_matrix(gold_args, pred_args)
    cm = np.array([cm[0]])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
                        # display_labels=set(pred_args)) doesn't work right somehow
    disp.plot()
    plt.savefig(filepath, dpi=600)

    