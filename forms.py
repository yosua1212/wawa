from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField 
from flask_ckeditor import CKEditorField

class BlogPostForm(FlaskForm):
    title = StringField('Title')
    content = CKEditorField('Content')
    #scontent = TextAreaField('Content')
    image = FileField('Image')
    read_time = StringField('Read Time')

class EditBlogPostForm(FlaskForm):
    title = StringField('Title')
    content = CKEditorField('Content')
    image = FileField('Image')
    read_time = StringField('Read Time')
