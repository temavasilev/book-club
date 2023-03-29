from app import app, db


@app.before_first_request
def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
