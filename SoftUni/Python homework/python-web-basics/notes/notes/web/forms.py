from django import forms

from notes.web.models import Profile, Note

PROFILE_LABELS = {
    'first_name': 'First Name',
    'last_name': 'Last Name',
    'age': 'Age',
    'image_url': 'Link to Profile Image',
}


NOTE_FIELDS = ('note_title', 'content', 'note_image_url',)
NOTE_LABELS = {
    'note_title': 'Title',
    'note_image_url': 'Link to Image',
    'content': 'Content'
}


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = PROFILE_LABELS


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = NOTE_FIELDS
        labels = NOTE_LABELS


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = NOTE_FIELDS
        labels = NOTE_LABELS


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Note
        fields = NOTE_FIELDS
        labels = NOTE_LABELS

