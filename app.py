import os
from flask import Flask,render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
# Configure MySQL connection
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB')


def initDB():
    mysql = MySQL()
    mysql.init_app(app)
    conn=mysql.connect()
    cursor=conn.cursor()
    return cursor

dbCusror=initDB()
def fetchColor(flag):
    key='background_color_'+flag
    dbCusror.execute("SELECT value FROM style_colors WHERE `key`='"+key+"'  LIMIT 1")
    color = dbCusror.fetchone()[0]
    return color


@app.route("/")
def main():
    try:

        return render_template('index.html',color=fetchColor("success"), result='Success', image='thumbs_up.png')
    except Exception as e:
        print(e)
        return render_template('index.html',color=fetchColor("failure"), result='Failure', image='thumbs_up.png')

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8080")