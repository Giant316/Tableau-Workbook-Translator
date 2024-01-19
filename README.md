# Tableau Workbook Translator
This tool allows you to translate the texts in your Tableau Workbook (.TWB) to your choose language using a [free translation python library - translators](https://pypi.org/project/translators/). Here are many languages available in this service. I only included a few languages for demonstration purposes. Feel free to include other supported languages listed in the translators library by modifying the two lines in my Python script.

`c = Combobox(frame, values=['German', 'French', 'Spanish', 'Mandarin', 'Japanese'], textvariable=options)`

`supported_languages = {"German": "de", "French": "fr", "Spanish": "es", "Mandarin": "zh", "Japanese":"ja"}`

## How to use?
Download this project and extract the zip file. You can run the twb.translator_v2.py file from the command line if you have Python installed on your machine. 
If you are using Windows and do not have Python installed on your machine, I have you covered. I have compiled the code into an executable for Windows. Unzip the twb.translator_v2 file and then double-click the twb.translator_v2.exe. Most likely, you will see a warning message prompted by Windows Defender to alert you to the risk of running this application. Just click on More info and "Run anyway. There is no virus, no worries! 😉

A simple GUI window will pop up. Select the desired target language and then click on the "Translate a Workbook" button to choose your Tableau Workbook. Wait for a while, and a translated Tableau Workbook will be generated in the same directory as your original Workbook.

### What to do if you have a Tableau packaged Workbook?
This tool only supports the TWB format, and if your Tableau workbook has the .TWBX extension, a workaround is to extract the packaged Workbook as if it's a zip file and then you can find the .TWB file in the folder. Check this [blog](https://www.thedataschool.co.uk/jia-yan-ng/saving-workbook-in-tableau-twb-vs-twbx-whats-the-difference/) of mine that explains the differences between them in more detail.

## Known Issues
The tool is far from perfect, and there are several issues that need to be addressed before it can be used in production. These are the bugs reported during my initial testing that are yet to be fixed for further improvement.
+ Inaccurate translation might occurs when the text is formatted with multiple newlines
+ Trailing spaces are replaced after translation
+ Text from the mix of parameter and text string can't be isolated

