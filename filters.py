from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, CharFilter, DateFilter
from .models import Post, User
from django import forms


class PostFilter(FilterSet):
    avtor = ModelChoiceFilter(field_name='author__user', queryset=User.objects.all(), label='автор')
    head = CharFilter(field_name='head', lookup_expr='contains', label='заголовок')
    datetime_in = DateFilter(
        field_name='datetime_in',
        lookup_expr='gte',  # lookup_expr='lt',
        label='дата добавления',
        widget=forms.DateInput(attrs={'type': 'date'})
    )


   # class Meta:
   #     model = Post
   #     fields = {
   #         'headline': ['icontains'],
   #         'author': ['exact'],
   #     }