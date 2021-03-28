import datetime as dt

from flask import Flask, render_template, request

x=dt.datetime.now()
sdt=x.strftime("%d-%b-%Y %H:%M:%S")
#print(f"hello world today is : {sdt}")

app = Flask(__name__)
entries=[]

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
        entries.append(content_dict)    
                
        #print(entries)
    return render_template("home.html" , entries=entries)
    


