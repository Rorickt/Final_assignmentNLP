from passive import predict_passive
from manner import predict_manner
from rel_clause import predict_elips
from roleset import predict_roleset
from theme_goal import predict_theme_goal
import sys

def main(argv=None):

    # 'predict_passive', 'predict_manner', 'predict_rel_clause', 'predict_roleset', 'predict_theme_goal'
    if argv is None:
        args = sys.argv
        test_to_run = str(args[1])
    else:
        test_to_run = argv

    if test_to_run == '1':
        predict_passive() 
    elif test_to_run == '2':
        predict_manner()
    elif test_to_run == '3':
        predict_elips()
    elif test_to_run == '4':
        predict_roleset()
    elif test_to_run == '5':
        predict_theme_goal()
    elif test_to_run == '6':
        predict_passive() 
        predict_manner()
        predict_elips()
        predict_roleset()
        predict_theme_goal()

    else:
        'Invalid or no argument given. Please enter a number between 1-5 to select which challenge set to test.'


if __name__ == '__main__':
    main()
