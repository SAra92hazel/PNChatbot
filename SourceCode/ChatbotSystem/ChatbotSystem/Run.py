from flask import Flask, render_template, request,flash
import pandas as pd
import csv
import io
import random
from flask import Response
from DBConnection import DBConnection
import re
from flask import session
from werkzeug.utils import secure_filename
import cv2
import sys
from Accuracy import ml_eval
from Similarity import similarity
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle
app = Flask(__name__)
app.secret_key = "abc"

menus=""
products=""

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/adminhome")
def adminhome():
    return render_template("admin_home.html")


@app.route("/userhome")
def userhome():
    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select * from menu1"
    cursor.execute(sql)
    menus = cursor.fetchall()

    return render_template("userhome.html",rawdata=menus)

@app.route("/shopping")
def shopping():
    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select * from menu1"
    cursor.execute(sql)
    menus = cursor.fetchall()

    return render_template("shopping.html",rawdata=menus)


@app.route('/signupaction',methods =["GET", "POST"])
def signupaction():
    try:
        name = request.form.get('name')
        unm = request.form.get('unm')
        pwd = request.form.get('pwd')
        email = request.form.get('email')
        mno = request.form.get('ph')

        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql = "select count(*) from users where userid='" + unm + "'"
        cursor.execute(sql)
        res = cursor.fetchone()[0]
        if res > 0:

            return render_template("index.html", msg="Username already exists..!")

        else:
            sql = "insert into users values(%s,%s,%s,%s,%s)"
            values = (name, unm, pwd, email, mno)
            cursor.execute(sql, values)
            database.commit()

        return render_template("index.html", msg2="Registered Successfully..! Login Here.")
    except Exception as e:
        print(e)
    return render_template("")


@app.route("/logincheck",methods =["GET", "POST"])
def userlogin():
        uid = request.form.get("unm")
        pwd = request.form.get("pwd")
        print(uid,pwd)
        database = DBConnection.getConnection()
        cursor = database.cursor()


        if uid=='admin' and pwd=='admin':
            return render_template("admin_home.html")

        else:

            sql = "select count(*) from users where userid='" + uid + "' and passwrd='" + pwd + "'"
            cursor.execute(sql)
            res = cursor.fetchone()[0]
            if res > 0:
                session['uid'] = uid

                return render_template("userhome.html")
            else:

                return render_template("index.html", msg3="Invalid Credentials")

        return render_template("")





@app.route("/addcategory")
def addcategory():

    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select *from menu1"
    cursor.execute(sql)
    records = cursor.fetchall()

    return render_template("addcategory.html", rawdata=records)


@app.route("/addproduct")
def addproduct():

    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select *from menu1"
    cursor.execute(sql)
    records = cursor.fetchall()

    return render_template("addproduct.html", rawdata=records)



@app.route("/viewproducts")
def viewproducts():

    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select *from items"
    cursor.execute(sql)
    records = cursor.fetchall()

    return render_template("viewproducts.html", rawdata=records)




@app.route("/product_info/<pid>/")
def product_info(pid):

    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    sql = "select *from items where id="+pid+" "
    cursor.execute(sql)
    records = cursor.fetchall()

    sql2 = "select avg(rating), count(*) from reviews where prodid="+pid+" "
    cursor2.execute(sql2)
    res = cursor2.fetchall()

    for r in res:
        rating=r[0]
        reviews=r[1]

    return render_template("/product_info.html",rawdata=records,rating=rating,reviwes=reviews)





@app.route("/viewlist/<pid>/")
def viewlist(pid):

    mpid=pid
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    sql = "select *from items where menu1id="+mpid+" "
    cursor.execute(sql)
    prdts_list= cursor.fetchall()
    print("prt_lidt=",prdts_list)

    sql2 = "select *from menu1 "
    cursor2.execute(sql2)
    records = cursor2.fetchall()

    for r in records:
        rating=r[0]
        reviews=r[1]

    return render_template("/product_list.html",rawdata=records,products=prdts_list)





@app.route('/category_insert',methods =["GET", "POST"])
def category_insert():
    try:
        catgry = request.form.get('level1')

        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql = "insert into menu1(subject_) values(%s)"
        values = (catgry,)
        cursor.execute(sql, values)
        database.commit()

        sql2 = "select *from menu1"
        cursor.execute(sql2)
        records = cursor.fetchall()

        return render_template("addcategory.html", msg="added",rawdata=records)
    except Exception as e:
        print(e)
    return render_template("")


@app.route('/viewprod',methods =["GET", "POST"])
def viewprod():
    try:
        pid = request.form.get('pid')
        print("pid=",pid)
        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql2 = "select * from items where id ="+pid+" "
        cursor.execute(sql2)
        records = cursor.fetchall()

        cursor2 = database.cursor()
        sql2 = "select avg(rating), count(*) from reviews where prodid=" + pid + " "
        cursor2.execute(sql2)
        res = cursor2.fetchall()

        for r in res:
            rating = r[0]
            reviews = r[1]

        return render_template("product.html",rawdata=records,rating=rating,reviwes=reviews)
    except Exception as e:
        print(e)
    return render_template("")


@app.route("/viewproduct/<pid>/")
def viewproduct(pid):
    print("pid=", pid)
    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql2 = "select * from items where id =" + pid + " "
    cursor.execute(sql2)
    records = cursor.fetchall()

    cursor2 = database.cursor()
    sql2 = "select avg(rating), count(*) from reviews where prodid=" + pid + " "
    cursor2.execute(sql2)
    res = cursor2.fetchall()

    for r in res:
        rating = r[0]
        reviews = r[1]

    return render_template("product.html", rawdata=records, rating=rating, reviwes=reviews)

    return render_template("")


@app.route('/productinsert',methods =["GET", "POST"])
def productinsert():
    try:
        catgry = request.form.get('catgry')
        menus=catgry.split(",")
        sub = request.form.get('sub')
        cost = request.form.get('cost')
        mcost = request.form.get('mcost')
        des = request.form.get('des')
        image = request.form.get('picture')
        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql = "insert into items(menu1,menu1id,subject_,cost,mcost,des,pic) values(%s,%s,%s,%s,%s,%s,%s)"
        values = (menus[1],menus[0],sub,cost,mcost,des,image)
        cursor.execute(sql, values)
        database.commit()

        sql = "select *from menu1"
        cursor.execute(sql)
        records = cursor.fetchall()

        return render_template("addproduct.html", msg="Added Successfully",rawdata=records)
    except Exception as e:
        print(e)
    return render_template("")




@app.route('/buy',methods =["GET", "POST"])
def buy():
    try:

        sub = request.form.get('sub')
        cost = request.form.get('cost')
        pid = request.form.get('id')
        tot = request.form.get('tot')

        return render_template("buy.html",sub=sub,cost=cost,pid=pid,qty=tot)
    except Exception as e:
        print(e)
    return render_template("")



@app.route('/buy2',methods =["GET", "POST"])
def buy2():
    try:

        sub = request.form.get('sub')
        cost = request.form.get('cost')
        pid = request.form.get('pid')
        qty = request.form.get('qty')

        uid = session['uid']

        tot=int(cost)*int(qty)
        print(sub,cost,pid,qty,tot)
        database = DBConnection.getConnection()
        cursor = database.cursor()

        sql = "insert into purchase(id, sub, cost, freq, tot_cost, user) values(%s,%s,%s,%s,%s,%s)"
        values = (pid,sub,cost, qty,tot,uid)
        cursor.execute(sql, values)
        database.commit()

        return render_template("buy2.html",sub=sub,cost=cost,qty=qty,tot=tot)
    except Exception as e:
        print(e)



    return render_template("")



@app.route("/writereview/<pid>/")
def writereview(pid):
    return render_template("/writereview.html",pid=pid)


@app.route("/reviews/<pid>/")
def reviews(pid):
    database = DBConnection.getConnection()
    cursor = database.cursor()

    sql2 = "select * from reviews where prodid=" + pid + " "
    cursor.execute(sql2)
    records = cursor.fetchall()
    accuracy_sentmnt(pid)






    return render_template("reviews.html", rawdata=records)



@app.route('/writereview2',methods =["GET", "POST"])
def writereview2():
    pid = request.form.get('id')
    rating = request.form.get('rating')
    review = request.form.get('review')
    uid=session['uid']

    filename ='nn_model.sav'
    train = pickle.load(open(filename, 'rb'))

    database = DBConnection.getConnection()
    cursor = database.cursor()


    sql = "insert into reviews(prodid,rating,review,userid,date_,uname) values(%s,%s,%s,%s,now(),%s)"
    values = (pid, rating, review, uid, uid)
    cursor.execute(sql, values)
    database.commit()


    cursor2 = database.cursor()
    cursor2.execute("select review, sno from reviews where sentiment='non' ")
    row = cursor2.fetchall()

    cursor3 = database.cursor()
    for r in row:
        print(r)
        w = [r[0]]
        predicted_class = train.predict(w)
        print(predicted_class[0])


        cursor3.execute("update reviews set sentiment='" + str(predicted_class[0]) + "' where sno='" + str(r[1]) + "' ")
        database.commit()




    return render_template("/writereview.html",pid=pid,msg="done")




@app.route('/accuracy')
def accuracy():
    ml_eval()

    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select *from accuracy"
    cursor.execute(sql)
    records = cursor.fetchall()
    fig = accuracy_graph()



    return render_template("accuracy.html", rawdata=records)



def accuracy_graph():
    db = DBConnection.getConnection()
    cursor = db.cursor()
    accuracy_list=[]
    accuracy_list.clear()

    cursor.execute("select  *from accuracy")
    acdata=cursor.fetchall()

    for record in acdata:
        accuracy_list.append(float(record[0]))
        accuracy_list.append(float(record[1]))
        accuracy_list.append(float(record[2]))
        accuracy_list.append(float(record[3]))

    height = accuracy_list
    print("height=",height)
    bars = ('NB','SVM','NN','RF')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['red', 'green', 'blue', 'brown'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithms')
    plt.ylabel('Accuracy')
    plt.title('Analysis on ML Accuracies')
    plt.savefig('static/accuracy.png')
    fig = plt.gcf()

    return fig


def accuracy_sentmnt(pid):

    database = DBConnection.getConnection()
    cursor1 = database.cursor()
    cursor2 = database.cursor()
    cursor3 = database.cursor()

    sentmnt_list = []
    sentmnt_list.clear()

    sql1 = "select COUNT(*) FROM reviews WHERE prodid='" + pid + "' and sentiment='positive' "
    cursor1.execute(sql1)
    pos = cursor1.fetchone()[0]
    if pos == 0:
        pos = 0

    sql = "select COUNT(*) FROM reviews WHERE prodid='" + pid + "' and sentiment='negative' "
    cursor2.execute(sql)
    neg = cursor2.fetchone()[0]
    if neg == 0:
        neg = 0

    sql3 = "select COUNT(*) FROM reviews WHERE prodid='" + pid + "' and sentiment='neutral' "
    cursor3.execute(sql3)
    neu = cursor3.fetchone()[0]
    if neu == 0:
        neu = 0

    sentmnt_list.append(pos)
    sentmnt_list.append(neg)
    sentmnt_list.append(neu)

    height = sentmnt_list

    bars = ('Positive','Negative','Neutral')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['green','red','blue'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Sentiments')
    plt.ylabel('Sentiment Scores')
    plt.title('Sentiment Analysis')
    plt.savefig('static/sentiment.png')
    fig = plt.gcf()

    return fig




@app.route("/vieworders")
def vieworders():
    uid = session['uid']
    database = DBConnection.getConnection()
    cursor = database.cursor()
    sql = "select *from purchase where user='"+uid+"' order by sno desc"
    cursor.execute(sql)
    records = cursor.fetchall()

    return render_template("view_orders.html", rawdata=records)

@app.route("/chat")
def chat():
    uid = session['uid']
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    cursor.execute("delete from msgs")
    database.commit()

    cursor.execute("insert into msgs(msg,user_,time_) values('Hello','chatbot',now())")
    database.commit()
    msg="Dear "+uid
    cursor.execute("insert into msgs(msg,user_,time_) values('"+msg+"','chatbot',now())")
    database.commit()
    cursor.execute("insert into msgs(msg,user_,time_) values('How can I help you..', 'chatbot',now())")
    database.commit()

    sql = "select * from msgs order by sno "
    cursor2.execute(sql)
    records = cursor2.fetchall()

    session["action"]="chatbot2"

    return render_template("chatbot.html", rawdata=records,res="")


@app.route("/chatbot2",methods =["GET", "POST"])
def chatbot2():
    dict={}
    uid = session['uid']
    text = request.form.get('text')
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor4 = database.cursor()
    cursor5 = database.cursor()
    cursor.execute("insert into msgs(msg,user_,time_) values('"+text+"','"+uid+"',now())")
    database.commit()

    cursor2 = database.cursor()
    sql = "select keywords,sno from questions"
    cursor2.execute(sql)
    res = cursor2.fetchall()

    for row in res:
        score=similarity(row[0], text)
        dict[row[1]]=score

    key = max(dict, key=dict.get)
    print("Highest value from dictionary:", key)

    if  dict[key]>0.1:
        cursor3 = database.cursor()
        sql2 = "select action,reply from questions where sno='"+str(key)+"' "
        cursor3.execute(sql2)
        res2 = cursor3.fetchall()

        for row2 in res2:
            action=row2[0]
            replay=row2[1]
            session["action"]=action
            cursor4.execute("insert into msgs(msg,user_,time_) values('" + replay + "','chatbot',now())")
            database.commit()

        sql3 = "select * from msgs order by sno "
        cursor5.execute(sql3)
        records = cursor5.fetchall()

        return render_template("chatbot.html", rawdata=records,res="")




    else:
        cursor4.execute("insert into msgs(msg,user_,time_) values('Sorry, I am not understood..','chatbot',now())")
        database.commit()

        sql3 = "select * from msgs order by sno "
        cursor5.execute(sql3)
        records = cursor5.fetchall()

        return render_template("chatbot.html", rawdata=records,res="")

    return render_template("")


@app.route("/details",methods =["GET", "POST"])
def details():
    dict={}
    uid = session['uid']
    text = request.form.get('text')
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    cursor3 = database.cursor()
    cursor4= database.cursor()
    cursor.execute("insert into msgs(msg,user_,time_) values('"+text+"','"+uid+"',now())")
    database.commit()

    text=text.strip()
    search=text.split(" ")
    qry = "select * from  items where subject_ like '%" + text + "%'  ";

    for k in search:
        qry=qry+"  or subject_ like '%"+k+"%' ";

    print("qry=",qry)
    cc = 0
    d = "Select Product to view full details<br><br>";
    cursor2.execute(qry)
    res=cursor2.fetchall()
    for r in res:
        #d = d +"<a href=http://localhost:1234/viewproduct/"+str(r[2])+' target=_blank >'+r[3]+'</a><br>';
        cc=cc+1

    if cc > 0:
        #cursor3.execute("insert into msgs(msg,user_,time_) values('" + str(d) + "','chatbot',now())")
        #database.commit()
        session["action"] = "chatbot2"
        sql2 = "select * from msgs order by sno "
        cursor4.execute(sql2)
        records = cursor4.fetchall()

        return render_template("chatbot.html", rawdata=records,res=res)

    else:
        session["action"] = "chatbot2"
        cursor3.execute("insert into msgs(msg,user_,time_) values('Sorry, I am not understood..','chatbot',now())")
        database.commit()
        sql2 = "select * from msgs order by sno "
        cursor4.execute(sql2)
        records = cursor4.fetchall()

        return render_template("chatbot.html", rawdata=records,res=res)


    return render_template("chatbot.html", rawdata=records,res=res)

@app.route("/bargain",methods =["GET", "POST"])
def bargain():
    dict = {}
    uid = session['uid']
    text = request.form.get('text')
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    cursor3 = database.cursor()
    cursor4 = database.cursor()
    cursor.execute("insert into msgs(msg,user_,time_) values('" + text + "','" + uid + "',now())")
    database.commit()

    text = text.strip()
    search = text.split(" ")
    qry = "select * from  items where subject_ like '%" + text + "%'  ";

    for k in search:
        qry = qry + "  or subject_ like '%" + k + "%' ";

    print("qry=", qry)
    cc = 0
    d = "Select Product to bargain..<br><br>";
    cursor2.execute(qry)
    res2 = cursor2.fetchall()
    session["products"]=res2
    for r in res2:
        # d = d +"<a href=http://localhost:1234/viewproduct/"+str(r[2])+' target=_blank >'+r[3]+'</a><br>';
        cc = cc + 1

    if cc > 0:
        # cursor3.execute("insert into msgs(msg,user_,time_) values('" + str(d) + "','chatbot',now())")
        # database.commit()
        session["action"] = "chatbot2"
        sql2 = "select * from msgs order by sno "
        cursor4.execute(sql2)
        records = cursor4.fetchall()

        return render_template("chatbot.html", rawdata=records, res="",res2=res2)

    else:
        session["action"] = "chatbot2"
        cursor3.execute("insert into msgs(msg,user_,time_) values('Sorry, I am not understood..','chatbot',now())")
        database.commit()
        sql2 = "select * from msgs order by sno "
        cursor4.execute(sql2)
        records = cursor4.fetchall()

        return render_template("chatbot.html", rawdata=records, res="", res2=res2)
    return render_template("chatbot.html", rawdata=records, res="", res2=res2)


@app.route("/product_bargain/<pid>/")
def product_bargain(pid):
    session["product_id"]=pid
    session["action"] = "bargain3"
    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    cursor3 = database.cursor()
    sql2 = "select * from items where id="+pid+" "
    cursor3.execute(sql2)
    rcrds= cursor3.fetchall()
    for r in rcrds:
        msg="Enter your bargain cost for "+r[3]+", Cost:"+r[4]+"/- Rs."
    cursor.execute("insert into msgs(msg,user_,time_) values('"+msg+"','chatbot',now())")
    database.commit()
    #products=session["products"]
    #print("products=",products)

    sql= "select * from msgs order by sno "
    cursor2.execute(sql)
    records = cursor2.fetchall()
    return render_template("chatbot.html", rawdata=records,res="", res2="")


@app.route("/bargain3",methods =["GET", "POST"])
def bargain3():
    dict = {}
    uid = session['uid']
    pid=session["product_id"]
    text = request.form.get('text')

    database = DBConnection.getConnection()
    cursor = database.cursor()
    cursor2 = database.cursor()
    cursor3 = database.cursor()
    cursor.execute("insert into msgs(msg,user_,time_) values('"+text+"','"+uid+"',now())")
    database.commit()

    ucost=int(text)

    sql = "select * from items where id=" + pid + " "
    cursor2.execute(sql)
    rcrds = cursor2.fetchall()
    session["barcost"] = ucost
    for r in rcrds:
        cost=int(r[4])
        min=int(r[5])

    if ucost >= min:
        session["action"] = "chatbot2"

        sql = "select * from msgs order by sno "
        cursor3.execute(sql)
        records = cursor3.fetchall()


        return render_template("chatbot.html", rawdata=records, res="", res2="",bargain_cost=ucost,pid=pid)


    else:
        msg="Sorry we cannot accept your offering price of"+str(ucost) + "/-"
        cursor.execute("insert into msgs(msg,user_,time_) values('"+msg+"','chatbot',now())")
        database.commit()

        sql = "select * from msgs order by sno "
        cursor3.execute(sql)
        records = cursor3.fetchall()

        diff = cost - min;
        diff = (diff * 50) / 100;
        diff = cost - diff;

        session["barcost"] = int(float(diff))

        #msg = "We offering you by the cost of " + str(diff) + "/-"
        #cursor.execute("insert into msgs(msg,user_,time_) values('" + msg + "','chatbot',now())")
        #database.commit()

        session["action"] = "bargain3"

    return render_template("chatbot.html", rawdata=records, res="", res2="", discount=diff, pid=pid)



@app.route('/payment/<pid>/')
def payment(pid):
    try:
        amnt=session["barcost"]
        database = DBConnection.getConnection()
        cursor = database.cursor()
        sql2 = "select * from items where id =" + pid + " "
        cursor.execute(sql2)
        records = cursor.fetchall()

        for rec in records:
            sub=rec[3]


        return render_template("payment.html",sub=sub,cost=amnt,pid=pid)
    except Exception as e:
        print(e)
    return render_template("")


@app.route('/payment2',methods =["GET", "POST"])
def payment2():
    try:

        sub = request.form.get('sub')
        cost = request.form.get('cost')
        pid = request.form.get('pid')
        qty = request.form.get('tot')

        uid = session['uid']

        tot=int(cost)*int(qty)
        print(sub,cost,pid,qty,tot)
        database = DBConnection.getConnection()
        cursor = database.cursor()

        sql = "insert into purchase(id, sub, cost, freq, tot_cost, user) values(%s,%s,%s,%s,%s,%s)"
        values = (pid,sub,cost, qty,tot,uid)
        cursor.execute(sql, values)
        database.commit()

        return render_template("buy2.html",sub=sub,cost=cost,qty=qty,tot=tot)
    except Exception as e:
        print(e)



    return render_template("")












if __name__ == '__main__':
    app.run(host="localhost", port=1234, debug=True)
