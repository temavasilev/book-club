from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from run import app, db
from app.models import User, Book, Review
from app.forms import RegistrationForm, LoginForm, BookForm, ReviewForm, SearchForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
@app.route("/index")
def index():
    books = Book.query.all()
    return render_template("index.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. You can now log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("Login successful.", "success")
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password.", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("index"))


@app.route("/book", methods=["GET", "POST"])
@login_required
def new_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data)
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully.", "success")
        return redirect(url_for("index"))
    return render_template("book.html", title="New Book", form=form)


@app.route('/book/<int:book_id>')
def book_page(book_id):
    book = Book.query.get_or_404(book_id)
    reviews = Review.query.filter_by(book_id=book_id).all()
    return render_template('book.html', book=book, reviews=reviews)


@app.route("/review/int:book_id", methods=["GET", "POST"])
@login_required
def new_review(book_id):
    book = Book.query.get_or_404(book_id)
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(
            content=form.content.data,
            rating=form.rating.data,
            author=current_user,
            book=book,
        )
        db.session.add(review)
        db.session.commit()
        flash("Review added successfully.", "success")
        return redirect(url_for("index"))
    return render_template("review.html", title="New Review", form=form, book=book)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        books = Book.query.filter(Book.title.ilike(f"%{query}%")).all()
        return render_template('search_results.html', books=books, query=query)
    return render_template('search.html', form=form)

@app.route('/user/<string:username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    reviews = Review.query.filter_by(user_id=user.id).all()
    return render_template('user_profile.html', user=user, reviews=reviews)

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('book_page', book_id=book.id))
    return render_template('add_book.html', form=form)