from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()], render_kw={"placeholder": "Title"})
    subtitle = StringField("Subtitle", validators=[DataRequired()], render_kw={"placeholder": "Subtitle"})
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()], render_kw={"placeholder": "Image URL"})
    body = CKEditorField("Blog Content", validators=[DataRequired()], render_kw={"placeholder": "Content"})
    submit = SubmitField("Submit Post")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email", "autofocus": True})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password", "autofocus": True})
    submit = SubmitField("Let me in.", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email", "autofocus": True})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password"})
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Name"})
    submit = SubmitField("Sign me up.", validators=[DataRequired()])

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()], render_kw={"placeholder": "Comment"})
    submit = SubmitField("Submit Comment", validators=[DataRequired()])