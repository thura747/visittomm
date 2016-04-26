from django import forms


# class TweetForm(forms.Form):
#     text = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 85, 'class': 'form-control post-tweet', 'placeholder': 'Post a new Tweet'}), max_length=160)
#     country = forms.CharField(widget=forms.HiddenInput())


class IndexSearchTripForm(forms.Form):
    origin = forms.CharField(label='Enter a keyword to search for',
                             widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control search-query'}))
    destinations = forms.CharField(label='Enter a keyword to search for',
                                   widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control search-query'}))
