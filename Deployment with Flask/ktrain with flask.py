from flask import Flask, render_template, request
import ktrain
import re
import AraBERTpreprocess
model_name = "aubmindlab/bert-base-arabertv2"

arabert_prep = AraBERTpreprocess.ArabertPreprocessor(model_name=model_name,
                                                     remove_html_markup = False,
                                                     replace_urls_emails_mentions = False,
                                                     strip_tashkeel = True,
                                                     strip_tatweel = True,
                                                     insert_white_spaces = False,
                                                     remove_non_digit_repetition = False,
                                                     replace_slash_with_dash = None,
                                                     map_hindi_numbers_to_arabic = True,
                                                     apply_farasa_segmentation = None)

def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0010FFFF"  # wider range
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
def preprocessing_text(text):
    text=remove_emoji(text)
    pat1 = '@[^ ]+'  # Remove mentions
    pat2 = '#'  #
    pat3 = '[0-9]'  # remove Number
    pat4 = '[A-Za-z]'  # remove english charctares
    combined_pat = '|'.join((pat1, pat2, pat3, pat4))
    text = re.sub(combined_pat, '', text)
    text = re.sub('[ى]', 'ي', text)
    text = re.sub('[إأٱآا]', 'ا', text)
    text = re.sub('[ؤئ]', 'ء', text)
    text = re.sub('[ة]', 'ه', text)
    text = re.sub('[\n]', ' ', text)
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,،-./:;<=>؟?@[\]^_`{|}~"""), '', text)  # remove punctuation
    text = re.sub(r'(.)\1+', r'\1', text)  # remove repeated char like هههه

    text = remove_emoji(text)

    text = arabert_prep.preprocess(text)

    return text




predictor = None

def load_predictor():
    global predictor
    print("Loading model ....")
    predictor = ktrain.load_predictor('E:\elec\Machine learning\Projects\Ktrain with flask\Final model')
    print("Loaded Successfully! ....")

app = Flask(__name__,template_folder=r"E:\elec\Machine learning\Projects\Ktrain with flask\templates")

@app.route('/')

def prediction():
    return render_template('prediction.html')

@app.route('/Result', methods=['POST', 'GET'])
def result():
    input_data = request.form['Data']
    print("Before pre-processing : ", input_data)
    input_data=preprocessing_text(input_data)
    print("After pre-processing : ", input_data)
    prediction = predictor.predict(input_data)

    return render_template('Result.html', result=prediction, text=input_data)


if __name__ =='__main__':
    load_predictor()
    app.run(debug=True)
    app.run
