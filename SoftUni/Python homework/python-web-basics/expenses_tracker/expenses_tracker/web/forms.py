import os

from django import forms

from expenses_tracker.web.models import Profile, Expense


PROFILE_FIELDS = ('budget', 'first_name', 'last_name', 'profile_image')
PROFILE_LABELS = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'budget': 'Budget',
            'profile_image': 'Profile Image',
        }

EXPENSE_FIELDS = ('title', 'description', 'expense_image', 'price')
EXPENSE_LABELS = {
            'title': 'Title',
            'description': 'Description',
            'expense_image': 'Link to Image',
            'price': 'Price',
        }


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = PROFILE_FIELDS
        labels = PROFILE_LABELS


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = PROFILE_FIELDS
        labels = PROFILE_LABELS


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        self.instance.delete()
        Expense.objects.all().delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = EXPENSE_FIELDS
        labels = EXPENSE_LABELS


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = EXPENSE_FIELDS
        labels = EXPENSE_LABELS


class DeleteExpenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Expense
        fields = EXPENSE_FIELDS
