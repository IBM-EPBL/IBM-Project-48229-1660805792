from flask import Flask, render_template

#import ibm_db
#conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xvn67110;PWD=fNSpdoYIUVJsfND3",'','')
##print(conn)
print("connection successful...")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ASDFGHJKL'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/home")
def aboutpage():
    return render_template("index.html")
 

if __name__ == "__main__":
    app.run()
