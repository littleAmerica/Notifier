from app import db

users_streams = db.Table('users_streams',
                         db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                         db.Column('stream_id', db.Integer, db.ForeignKey('streams.id')))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    lessons = db.relationship("Stream",
                              backref="teachers",
                              secondary=users_streams)

    def __repr__(self):
        return '<User %r>' % self.username


class Stream(db.Model):
    __tablename__ = "streams"

    id = db.Column(db.Integer, primary_key=True)
    stream = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<User %r>' % self.stream
