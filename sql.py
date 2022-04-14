from os import close
from flask import Flask,render_template,redirect,request
import sqlite3 as sql
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('sql_home.html')

@app.route('/sql_form')
def sql_form():
    return render_template('sql_form.html')

@app.route('/form_rec',methods=['POST','GET'])
def form_rec():
    if request.method=='POST':
        name=request.form['nm']
        address=request.form['addr']
        city=request.form['city']
        pin=request.form['pincode']
        con = sql.connect('mydb.db')
        try:
            cur=con.cursor()
            cur.execute("insert into emp values (?, ?, ?, ? )",(name,address,city,pin))
            con.commit()
            msg='Record Added Successfully!'
        except:
            con.rollback()
            msg='ERROR in Insertion'
        finally:
            return render_template('sql_result.html', msg=msg)
            con.close()
@app.route('/sql_list')
def sql_list():
    con=sql.connect('mydb.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('select * from emp')
    rows=cur.fetchall()
    return render_template('sql_list.html',rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
