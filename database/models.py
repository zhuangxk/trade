from database import DB

# 用户表
class IbmUser(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    tel = DB.Column(DB.String(50))
    email = DB.Column(DB.String(50))


class Config(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    ibm_user_index = DB.Column(DB.String(50))