# TODO: database modeling
# TODO: profile picture column in user table
# TODO: foreign key relationship between all models

from . import db
from . import login_manager

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique =  True)
    date_of_join = db.Column(db.Date)
    gender = db.Column(db.String(6))                            # ['male', 'female', 'other']
    bio = db.Column(db.Text)
    facebook = db.Column(db.Text)
    twitter = db.Column(db.Text)
    linkedin = db.Column(db.Text)
    website = db.Column(db.Text)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # return current user id
    @property
    def get_user_id(self):
        return self.id

    def __repr__(self) -> str:
        return "<{}\t{}\t{}>\n".format(self.id, self.user_name, self.date_of_join)

# class Admins(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column()

#     def __repr__(self) -> str:
#         return "<{}\t{}>\n".format(self.id, self.user_id)

# class Moderators(db.Model):
#     __tablename__ = 'moderators'
#     id = db.Column(db.Integer, primary_key=True)
#     admin_id = db.Column()

#     def __repr__(self) -> str:
#         return "<{}\t{}>\n".format(self.id, self.admin_id)

# class Posts(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     admin_id = db.Column()
#     title = db.Column(db.Text, nullable = False)
#     subtitle = db.Column(db.Text, nullable = False)
#     body = db.Column(db.Text, nullable = False)
#     date_added = db.Column(db.Date)
#     date_modified = db.Column(db.Date)

#     def __repr__(self) -> str:
#         return "<{}\t{}\t{}\t{}>\n".format(self.id, self.admin_id, self.date_added, self.title)

# class Tags(db.Model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key=True)
#     tag = db.Column(db.String(30), nullable = False, unique = True)
#     post_id = db.Column()

#     def __repr__(self) -> str:
#         return "<{}\t{}\t{}>\n".format(self.id, self.tag, self.post_id)

# class Comments(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column()
#     post_id = db.Column()
#     date_added = db.Column(db.Date)
#     date_modified = db.Column(db.Date)
#     comment = db.Column(db.Text)

#     def __repr__(self) -> str:
#         return "<{}\t{}\t{}\t{}\t{}>\n".format(self.id, self.user_id, self.post_id, self.date_added, self.comment)

# class ReportComment(db.Model):
#     __tablename__ = 'reportcomment'
#     id = db.Column(db.Integer, primary_key=True)
#     comment_id = db.Column()
#     reporter_id = db.Column()
#     date_added = db.Column(db.Date)
#     report = db.Column(db.Text, nullable = False)

# class ReportUser(db.Model):
#     __tablename__ = 'reportuser'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column()
#     reporter_id = db.Column()
#     date_added = db.Column(db.Date)
#     report = db.Column(db.Text, nullable = False)

# class Members(db.Model):
#     __tablename__ = 'members'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column()
#     date_joined = db.Column(db.Date)

class SubscribeModel(db.Model):                                  # subscribed emails model
    __tablename__ = 'subscribemodel'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    date_subscribed = db.Column(db.Date)                        # pyhton3: datetime.date.today()

    def __repr__(self) -> str:                                  # return string representation of a row
        return "\n{}\t{}\t{}\t{}".format(self.id, self.name, self.email, self.date_subscribed)