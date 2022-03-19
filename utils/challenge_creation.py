from checklist.editor import Editor
from read_write_files import write_to_file


def create_challengeset(output, template, goldlabel, input_list=None, input_name=None):
    
    editor = Editor()



    if input_list:
        f = editor.template(template, input_name=input_list, meta=True, nsamples=1000)
        sentences = f.data

    else:
        f = editor.template(template, meta=True, nsamples=1000)
        sentences = f.data


    write_to_file(output, sentences, goldlabel)

