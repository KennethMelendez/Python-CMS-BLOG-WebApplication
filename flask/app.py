from flask import Flask, render_template, flash, redirect, url_for,session, logging, request
# from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)


#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'articles'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL

mysql = MySQL(app)

# Previously used an object in order to call the articles later changed to MySQL
# articles = Articles()


@app.route('/')
def display_index():
    return render_template('home.html')

@app.route('/about')
def display_about():
    return render_template('about.html')

@app.route('/articles')
def display_articles():

    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('articles.html',articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('articles.html', msg=msg)    

@app.route('/article/<string:id>/')
def display_article(id):
    cur = mysql.connection.cursor()

    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    return render_template('article.html',article=article)

# Register form class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email',[validators.Length(min=6, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/register',methods=['GET','POST'])
def display_register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)" , (name, email, username, password))

        # commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('display_index'))
    return render_template('register.html', form=form)

# USER LOGIN
@app.route('/login', methods=['GET','POST'])
def display_login():
    if request.method == 'POST':
            # Get Form Fields
            username = request.form['username']
            # for logging in need to compare passwords
            password_candidate = request.form['password']

            #Create cursor
            cur = mysql.connection.cursor()

            # Get user by username
            result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

            if result > 0:
                # Get stored hash
                data = cur.fetchone()
                # dictionary value
                password = data['password']

                # Compare passwords
                if sha256_crypt.verify(password_candidate, password):
                    app.logger.info('PASSWORD MATCHED')
                    session['logged_in'] = True;
                    session['username'] = username
                    # return render_template('dashboard.html')
                    return redirect(url_for('display_dashboard'))
                else:
                    app.logger.info('PASSWORD NOT MATCHED')
                    error = 'Invalid login'
                    return render_template('login.html', error=error)    
            else:
                error = 'Username not found'
                return render_template('login.html', error=error)    
    return render_template('login.html')


# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')    
            return redirect(url_for('display_login'))
    return wrap

# logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('display_login'))

@app.route('/dashboard')
@is_logged_in
def display_dashboard():

    # create cursor

    cur = mysql.connection.cursor()

    # get articles

    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()

    if result > 0:
        return render_template('dashboard.html',articles=articles)
    else:
        msg = 'No Articles Found'
        return render_template('dashboard.html', msg=msg)

    # Close connection
    cur.close()    
    

# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1,max=200)])
    body = TextAreaField('Body', [validators.Length(min=30)])

@app.route('/add_article', methods=['GET','POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        #create cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)",(title, body, session['username']))

        # commit to DB
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('display_dashboard'))
    return render_template('add_article.html', form=form)


# edit article
@app.route('/edit_article/<string:id>', methods=['GET','POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()

    form = ArticleForm(request.form)
    # Populate article from form fields
    form.title.data = article['title']
    form.body.data = article['body']
    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        #create cursor
        cur = mysql.connection.cursor()

        # Execute
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id = %s",(title, body, id))

        # commit to DB
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('Article Updates', 'success')

        return redirect(url_for('display_dashboard'))
    return render_template('edit_article.html', form=form)


#Delete Article
@app.route('/delete_article/<string:id>',methods=['POST'])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = mysql.connection.cursor()
    #Excecute
    cur.execute("DELETE FROM articles WHERE id = %s", [id])
    #commit and then close db
    mysql.connection.commit()
    cur.close()
    flash('Article Deleted', 'success')
    return redirect(url_for('display_dashboard'))


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)


# can add debug=True in order to start in development mode