from allennlp_models.pretrained import load_predictor
import csv


def predict_sents(challengeset, model, pred_num, word_num):

    srl_predictor = load_predictor(model)

    full_preds = []
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

    return full_preds, predictions, gold_labels