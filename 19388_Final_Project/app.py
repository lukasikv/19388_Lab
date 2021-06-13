from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
import sqlite3 as sql
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

app.config.update(
    DEBUG=False,
    SECRET_KEY='secretpass'
)
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
def index():
    return render_template('index.html')

@app.route("/center")
@login_required
def main():
    dane = {'tytul': 'Strona główna', 'tresc': 'Witaj na stronie głównej.'}
    return render_template('addcenter.html', tytul=dane['tytul'], tresc=dane['tresc'])

#dodaj pracownika
@app.route("/dodaj")
@login_required
def dodaj():
    dane = {'tytul': 'Dodaj pracownika', 'tresc': 'Dodaj pracownika.'}
    return render_template('add.html', tytul=dane['tytul'], tresc=dane['tresc'])

#dodawanie rekordu do bazy danych
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            imienazwisko = request.form['imienazwisko']
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pracownicy (imienazwisko, nrpracownika, adres) VALUES (?, ?, ?)",
                            (imienazwisko, nrpracownika, adres))
                con.commit()
                msg = "Gratulacje, dodałes nowy rekord!"
        except:
            con.rollback()
            msg = "Przykro nam, nie udało się dodać rekordu..."
        finally:
            return render_template("res.html", tytul="Rezultat", tresc=msg)
            con.close()

#Lista pracowników
@app.route("/lista")
@login_required
def lista():
    dane = {'tytul': 'Lista aktualnych pracowników', 'tresc': 'Lista pracowników'}
    con = sql.connect('database.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM pracownicy")
    rekordy = cur.fetchall()
    con.close()
    return render_template('lista.html', tytul=dane['tytul'], tresc=dane['tresc'], rekordy=rekordy)


if __name__ == "__main__":
    app.run(debug=True)