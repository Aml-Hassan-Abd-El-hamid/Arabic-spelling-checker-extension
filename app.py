from ar_corrector.corrector import Corrector
from flask import Flask as f, jsonify,request
#from flask import render_template

corr = Corrector()
app = f(__name__)

def call_corr(word):
    return corr.spell_correct(word)

@app.route('/')
def home():
    #return render_template('home.html')
    #return jsonify(message='hi')
    word= request.args.get("word")
    return jsonify(words=call_corr(word))

if __name__ == '__main__':
    app.run()