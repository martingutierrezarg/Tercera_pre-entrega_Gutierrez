from django.contrib.auth.forms import UserCreationForm
from .models import User
# User Register Form


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['name','email']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
