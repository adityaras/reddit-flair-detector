import flask
import pickle
import praw
import nltk
from nltk.corpus import stopwords
import contractions
import inflect
import pandas as pd
import json

def clean(t):    
    en_stops = set(stopwords.words('english'))
    t_old = str(t)
    t_old = t_old.translate({ord(i): None for i in '{[(!@#$|%^.;:?><*=`~\-/_,&+)]}'})
    t_old = t_old.replace('\n','')
    t_old = t_old.replace('"','')
    t_old = t_old.replace("'",'')
    t_old = contractions.fix(t_old)
    t_new = nltk.word_tokenize(t_old)
    words_list=[]
    for word in t_new:
        word1=word.lower()
        words_list.append(word1)
    word_list=[]
    for word in words_list:
        if word not in en_stops:
            word_list.append(word)
    p = inflect.engine()
    new_words = []
    for word in word_list:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    if len(new_words) == 0:
        return ''
    else:
        return new_words

def pos(data):
    reddit = praw.Reddit(client_id='Qq1MxtQ9YVNXgA',client_secret='hg00d83IEYWEAAT0RdFzm50zm5E', user_agent='testing',  username='mic_testing123',password='Cookies')
    try:
        post_data = reddit.submission(url = data)
    except:
        return ("No post with given URL",5000)    
    post = {}
    post = {
    "title":clean(post_data.title),
    "url":str(post_data.url),}
    post_data.comments.replace_more(limit=0)
    comment = ''
    count=0
    for top_level_comment in post_data.comments:
        comment = comment + ' ' + top_level_comment.body
        count=count+1     
        if(count > 20):
            break
    post["comment"] = clean(comment)
    s = str(post["title"])+","+str(post["url"])+","+str(post["comment"])
    a = s.split(',') 
    a1=''
    for item in a:
        item1 = item.replace("[",'')
        item1 = item1.replace("]",'')
        item1 = item1.replace('"','')
        item1 = item1.replace(' ','')
        a1=a1+","+(item1)
    return a1,0

model = pickle.load(open("model/model_final.pkl", 'rb'))

app = flask.Flask(__name__,template_folder = 'template')

@app.route('/', methods = ['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        #print("yaya")
        url = flask.request.form['url']
        input_var,code = pos(str(url))
        if code != 0:
            return flask.render_template('main.html', original_input={'URL':url},result=input_var,)
        else:
            dic={}
            dic["combined"] = input_var
            val = pd.DataFrame([dic])
            prediction1 = str(model.predict(val["combined"]))
            prediction1 = prediction1[2:-2]
            return flask.render_template('main.html', original_input={'URL':url},result=prediction1,)

@app.route('/automated_testing',methods = ['POST'])
def automated_testing():
    if flask.request.method == 'POST':    
        #print(flask.request.files)
        #print("I m here1")
        #print(type(flask.request.files))
        txt = flask.request.files["upload_file"]
        #print("I m here2")
        #print(txt)
        urls = txt.read().decode('utf-8').split('\n')
        dic1 = {}
        for url in urls:
            if url != '':
                input_var,code = pos(str(url))
                dic={}
                dic["combined"] = input_var
                val = pd.DataFrame([dic])
                prediction1 = str(model.predict(val["combined"]))
                dic1[url] = prediction1[2:-2]
                #print(dic1[url])
        return json.dumps(dic1)

if __name__ == "__main__":
    app.run()