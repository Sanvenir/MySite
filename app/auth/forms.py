from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from app.models import User


class LoginForm(Form):
    email = StringField(
        '邮箱',
        validators=[DataRequired(), Length(1, 64), Email()]
    )
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


class RegistrationForm(Form):
    email = StringField(
        '邮箱',
        validators=[DataRequired(), Length(1, 64), Email()]
    )
    username = StringField('昵称', validators=[
        DataRequired(),
        Length(1, 64)
    ])
    password = PasswordField('密码', validators=[DataRequired(), EqualTo('password2')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册！')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('昵称已注册！')
