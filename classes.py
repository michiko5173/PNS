from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField

class CreateTask(FlaskForm):
    number = TextField('号码')
    name = TextField('姓名')
    package = TextField('套餐类型')
    create = SubmitField('新增')

class DeleteTask(FlaskForm):
    number = TextField('号码')
    delete = SubmitField('删除')

class UpdateTask(FlaskForm):
    number = TextField('号码')
    package = TextField('套餐类型')
    update = SubmitField('更新')

class ResetTask(FlaskForm):
    reset = SubmitField('执行')
class SpiderTask(FlaskForm):
    spider = SubmitField('执行')
