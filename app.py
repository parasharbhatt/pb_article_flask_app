import datetime as dt
import database
from flask import Flask, render_template, request



#print(f"hello world today is : {sdt}")

app = Flask(__name__)
#entries=[]
database.fn_create_article_table()

@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
    #print("calling Home route")
    if request.method == "POST":
        content_dict={}
        for key, val in request.form.items():
            if key == "title":
                content_dict[key] = val
            elif key == "content":
                content_dict[key] = val
                #request.form.get(key)
            sdt=dt.datetime.now().strftime("%d-%b-%Y %H:%M:%S")
            content_dict['articledate']=sdt
        #entries.append(content_dict)
        #print(entries)
        database.fn_create_article(content_dict['title'],content_dict['articledate'], content_dict['content'])    
    #return render_template("home.html" , entries=entries)
    return render_template("home.html" , entries=database.fn_retrieve_articles())
