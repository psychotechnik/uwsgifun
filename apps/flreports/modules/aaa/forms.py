from flaskext.wtf import BooleanField, Email, EqualTo, Form, IntegerField, \
    Length, NumberRange, Optional, Required, PasswordField, QuerySelectField, \
    RadioField, SubmitField, TextField, ValidationError

class LoginForm(Form):
    email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    idle_ttl = RadioField('Idle Session Timeout', default='tmp', choices=[
            ('tmp',  '20 minutes'),
            ('day',  '8 hours (a normal business day)'),
            ('week', '8 days (Monday to Monday)'),
            ])
    submit = SubmitField('Login')
    # Tempted to add a Field that would provide a mask for a user's IP
    # address. Defaults to /32, but could be set down to /24 if they're stuck
    # in a totally broken corporate environment.


class ProfileForm(Form):
    password = PasswordField('New Password', validators=[
            Optional(),
            Length(min=8, max=80),
            EqualTo('confirm', message='Passwords must match')
            ])
    confirm = PasswordField('Repeat Password')
    default_ipv4_mask = IntegerField(label='IPv4 Mask', validators=[
            Optional(),
            NumberRange(min=0, max=32, message='IPv4 Mask must between %(min)s and %(max)s'),
            ])
    default_ipv6_mask = IntegerField(label='IPv6 Mask', validators=[
            Optional(),
            NumberRange(min=0, max=128, message='IPv6 Mask must between %(min)s and %(max)s'),
            ])
    timezone = QuerySelectField(get_label='name', allow_blank=True)
    submit = SubmitField('Update Profile')


class RegisterForm(Form):
    email = TextField('Email Address', validators = [Email()])
    password = PasswordField('New Password', validators=[
            Required(),
            Length(min=8, max=80),
            EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', validators = [Required()])
    timezone = QuerySelectField(get_label='name', allow_blank=True)
    submit = SubmitField('Register')
