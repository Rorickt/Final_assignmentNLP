from passive import predict_passive
from manner import predict_manner
# from rel_clause import predict_rel_clause
# from roleset import predict_roleset
# from theme_goal import predict_theme_goal
import sys

def main(argv=None):

    # 'predict_passive', 'predict_manner', 'predict_rel_clause', 'predict_roleset', 'predict_theme_goal'
    if argv==None:
        args = sys.argv
        test_to_run = str(args[1])
    else:
        test_to_run = argv
    print(test_to_run)

    if test_to_run == '1':
        predict_passive()
    elif test_to_run == '2':
        predict_manner()
    # elif test_to_run == 3:
    #     predict_rel_clause()
    # elif test_to_run == 4:
    #     predict_roleset()
    # elif test_to_run == 5:
    #     predict_theme_goal()
    else:
        'Invalid or no argument given. Please enter a number between 1-5 to select which challenge set to test.'


if __name__ == '__main__':
    main()

