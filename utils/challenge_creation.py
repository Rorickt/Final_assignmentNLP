from checklist.editor import Editor


def create_challengeset(template, samples=100, input_list=None, input_name=None):
    
    editor = Editor()



    if input_list:
        editor.add_lexicon(input_name, input_list)
        
        f = editor.template(template, meta=True, nsamples=samples, remove_duplicates=True)
        sentences = f.data

    else:
        f = editor.template(template, meta=True, nsamples=samples, remove_duplicates=True)
        sentences = f.data

    return sentences