from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
import sqlite3 as sql
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    SECRET_KEY='secretpass'
)
app.config['TESTING'] = False
#flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#users
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_PASSWORD"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

# login: user1 Password: user1_PASSWORD
users = [User(id) for id in range(1, 20)]

#login form
@app.route("/login", methods=["GET", "POST"])
def login():
    dane = {'tytul': 'Zalgouj się', 'tresc': 'Wypełnij formularz aby się zalogować'}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_PASSWORD":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("main"))
        else:
            return abort(401)
    else:
        return render_template('login_form.html', tytul=dane['tytul'], tresc=dane['tresc'])

# incorrect password
@app.errorhandler(401)
def page_not_found(e):
    dane = {'tytul': 'Niepoprawny login lub hasło!', 'blad': 'Spróbuj ponownie!'}
    return render_template('error.html', tytul=dane['tytul'], blad=dane['blad'])

# wylogowanie
@app.route("/logout")
@login_required
def logout():
    logout_user()
    dane = {'tytul': 'Zostałeś wylogowany...'}
    return render_template('log_out.html', tytul=dane['tytul'])


# uzytkownicy
@login_manager.user_loader
def load_user(userid):
    return User(userid)


#index
@app.route("/")
@login_required
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()