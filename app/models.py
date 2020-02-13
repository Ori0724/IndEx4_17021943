from app import db


class city(db.Model):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.Text, nullable=False)
    forecast = db.relationship("forecast")

    def __repr__(self):
        return '<city {}>'.format(self.city)


class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    forecast = db.relationship("forecast")

    def __repr__(self):
        return '<user {} {}>'.format(self.username, self.email)


class forecast(db.Model):
    __tablename__ = 'forecast'
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False, primary_key=True)
    forecast_datetime = db.Column(db.Text, nullable=False)
    forecast = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<forecast {} {} {}>'.format(self.forecast, self.forecast_datetime, self.comment)



