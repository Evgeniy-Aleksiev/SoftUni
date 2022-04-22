from django import forms

from recipes.web.models import Recipe

RECIPE_LABELS = {'time': 'Time (Minutes)',
                 'image_url': 'Image URL',
                 }


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = RECIPE_LABELS


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = RECIPE_LABELS


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = RECIPE_LABELS
