from checklist.editor import Editor
from read_write_files import write_to_file


def create_challengeset(output, template, goldlabel, input_list=None):
    
    editor = Editor()



    if input_list:
        checklist_item = []
        # get name cheklist itemname from template
        store =False
        for char in template:
            if char =='{':
                store = True
            elif char == '}':
                store = False
            else:
                if store:
                    checklist_item.append(char)

        checklist_item = ''.join(checklist_item)

        f = editor.template(template, locals()[checklist_item]=input_list, meta=True, nsamples=1000)
        sentences = f.data

    else:
        f = editor.template(template, meta=True, nsamples=1000)
        sentences = f.data


    write_to_file(output, sentences, goldlabel)

