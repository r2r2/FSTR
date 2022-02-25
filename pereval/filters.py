from django_filters import rest_framework as filters

from pereval.models import Added


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UserProfileFilter(filters.FilterSet):
    """Фильтрации по данным пользователя (ФИО, телефон, почта)"""
    name = CharFilterInFilter(field_name='user__name', lookup_expr='in', label='Имя')
    fam = CharFilterInFilter(field_name='user__fam', lookup_expr='in', label='Фамилия')
    otc = CharFilterInFilter(field_name='user__otc', lookup_expr='in', label='Отчество')
    phone = CharFilterInFilter(field_name='user__phone', lookup_expr='in', label='Телефон')
    email = CharFilterInFilter(field_name='user__email', lookup_expr='in', label='email')

    class Meta:
        model = Added
        fields = ('user',)
