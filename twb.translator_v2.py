import tkinter as tk
import translators as ts
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Label, Combobox

def open_file():
    """
    Open a twb file for translating.
    Add suffix to the output twb file: _translated_[translated_language]
    Display error message when language option is not selected.
    """
    # constraint the user to open only the twb Tableau workbook
    filepath = askopenfilename(
        filetypes=[("Tableau Workbook", "*.twb")]
    )
    n = filepath.count("/")
    x = filepath.split("/",n)
    # get the twb filename
    filename = x[-1].split(".", 1)
    # remove last item in the list
    *x, _ = x
    # construct the filepath for the output twb file
    output_filepath = "/".join(x) + '/' + filename[0] + '_translated_' + options.get() + '.twb'
    if not filepath:
        return
    if options.get() == '':
        msg_display.set("Please select a language to be translated in the dropdown menu")
    else:
        # read twb file as xml
        tree = ET.parse(filepath)
        root = tree.getroot()
        # retrieve the child element of all <run> tags as a list
        text_list = [r.text for r in root.iter("run") if not(r.text.strip().startswith('<') and r.text.strip().endswith('>'))]
        # make sure each item in the list is unique
        unique_list = list(dict.fromkeys(text_list))
        # remove the all texts that contain the character 'Æ'
        clean_list = [l for l in unique_list if not 'Æ' in l]
        # translate all items in the list to the targeted language and construct a dictionary
        translated_list =[ts.translate_text(i, translator = 'google', to_language = supported_languages[options.get()]) for i in clean_list]
        translated_dict = dict(zip(clean_list, translated_list))
        '''
        The twb file is not read as XML using ElementTree package. Since the twb file isn't a standard XML file, 
        some of the special characters e.g. &quot; will be omitted in some attribute nodes.
        This will affect certain sets and actions built in the dashboard. 
        Hence, it will be read as txt file using readlines() instead. 
        '''
        # read/write the twb file line by line
        with open(filepath, encoding='utf-8') as rfile, \
        open(output_filepath, "w", encoding='utf-8') as wfile:
            lines = rfile.readlines()
            for line in lines:
                # check the lines with <run> tags and replace the text to its respective translated text
                if '<run' in line:
                    temp_result = [l for l in clean_list if l in line]
                    if temp_result != []:
                        line = line.replace(temp_result[0], translated_dict[temp_result[0]])
                wfile.write(line)
        window.title(f"Tableau Workbook Translator - {filepath}")
        msg_display.set("Translated workbook is saved at the same folder as the selected file")

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Tableau Translator")
    frame = tk.Frame(window)
    frame.pack(fill='both', expand=1, padx=10, pady=10)
    language_options = Label(frame, text="Available Languages: ", width=20)
    language_options.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    # create a dropdown menu with listed options
    options = tk.StringVar()
    c = Combobox(frame, values=['German', 'French', 'Spanish', 'Mandarin', 'Japanese'], textvariable=options)
    c.grid(row=0, column=1, sticky="e", padx=10, pady=10)
    # language dictionary for mapping
    supported_languages = {"German": "de", "French": "fr", "Spanish": "es", "Mandarin": "zh", "Japanese":"ja"}
    frame2 = tk.Frame(window)
    frame2.pack(fill='both', expand=1, padx=10, pady=5)
    # create a button allowing user to select a twb file
    btn_open = tk.Button(frame2, text="Translate a Workbook", command=open_file)
    btn_open.pack(side='bottom')
    # dynamically display a message according to the user action
    msg_display = tk.StringVar()
    msg_display.set("")
    frame3 = tk.Frame(window)
    frame3.pack(fill='both', expand=1, padx=10, pady=5)
    message = Label(frame3, textvariable=msg_display, width=60)
    message.pack(side = "bottom")
    window.mainloop()