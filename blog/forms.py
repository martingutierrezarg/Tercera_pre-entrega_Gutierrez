from urllib import request
from django.forms import ModelForm
from .models import Blog
#---------------------------------------------------------------------------------------
class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
        exclude=['blogger']

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
#---------------------------------------------------------------------------------------