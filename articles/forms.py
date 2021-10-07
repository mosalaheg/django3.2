from django import forms
from django.db.models import fields
from .models import Article

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "published_at"]

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if title.endswith("Awesome"):
            self.add_error("title", "Title can't end with 'Awesome' ")

        if content.endswith("Awesome"):
            self.add_error("content", "Content can't contain 'Awesome' ")
        return self.cleaned_data

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #     if title.endswith("Awesome"):
    #         #self.add_error("title", "Title can't end with 'Awesome' ")
    #         raise forms.ValidationError("Error")
    #     return title
    
    # def clean_content(self):
    #     content = self.cleaned_data.get("content")
    #     if content.endswith("Awesome"):
    #         raise forms.ValidationError("Error")
    #         #self.add_error("content", "Content can't contain 'Awesome' ")
    #     return content
    

    def clean(self):
        title = self.cleaned_data.get("title")
        content = self.cleaned_data.get("content")
        if title.endswith("Awesome"):
            self.add_error("title", "Title can't end with 'Awesome' ")

        if content.endswith("Awesome"):
            self.add_error("content", "Content can't contain 'Awesome' ")
        return self.cleaned_data