from django import forms

from online_library.web.models import Profile, Book

BOOK_LABELS = {'book_title': 'Title',
               'description': 'Description',
               'image': 'Image',
               'book_type': 'Type',
               }

BOOK_WIDGETS = {
    'book_title': forms.TextInput(
        attrs={
            'placeholder': 'Title'
        }
    ),
    'description': forms.Textarea(
        attrs={
            'placeholder': 'Description'
        }
    ),
    'image': forms.TextInput(
        attrs={
            'placeholder': 'Image'
        }
    ),
    'book_type': forms.TextInput(
        attrs={
            'placeholder': 'Fiction, Novel, Crime..'
        }
    ),
}


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = BOOK_LABELS
        widgets = BOOK_WIDGETS


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

