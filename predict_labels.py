from allennlp_models.pretrained import load_predictor
import csv
srl_predictor = load_predictor('structured-prediction-srl')

f_all_preds = []
f_pred_args = []
f_gold_args = []

with open('challenge_sets/female_aggressor.csv', 'r', encoding='utf-8') as file:
    file = csv.reader(file, delimiter='\t')
    for row in file:
        prediction = srl_predictor.predict(row[0])
        f_all_preds.append(prediction)
        predicted_arg = prediction['verbs'][0]['tags'][0].strip('B-').strip('I-')
        f_pred_args.append(predicted_arg)
        f_gold_args.append(row[1])


