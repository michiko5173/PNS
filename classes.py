from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateNum(FlaskForm):
    number = TextField('号码')
    name = TextField('姓名')
    package = TextField('套餐类型')
    create = SubmitField('新增')

class DeleteNum(FlaskForm):
    number = TextField('号码')
    delete = SubmitField('删除')

class UpdateNum(FlaskForm):
    number = TextField('号码')
    package = TextField('套餐类型')
    update = SubmitField('更新')

class ResetNum(FlaskForm):
    reset = SubmitField('执行')
class SpiderNum(FlaskForm):
    spider = SubmitField('执行')
    times = TextField('条数')
