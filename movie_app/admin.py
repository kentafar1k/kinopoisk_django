from django.contrib import admin, messages
from movie_app.models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)
#admin.site.register(DressingRoom)

@admin.register(DressingRoom)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):

    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<4', 'Низкий'),
            ('от 4 до 5', 'Средний'),
            ('от 6 до 7', 'Высокий'),
            ('>=8', 'Топ'),
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<4':
            return queryset.filter(rating__lt=4)
        if self.value() == 'от 4 до 5':
            return queryset.filter(rating__gte=4).filter(rating__lte=5)
        if self.value() == 'от 6 до 7':
            return queryset.filter(rating__gte=6).filter(rating__lte=7)
        if self.value() == '>=8':
            return queryset.filter(rating__gte=8)
        return queryset




@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'director', 'rating_status']
    list_editable = ['year', 'budget', 'director']
    filter_horizontal = ['actors']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-rating']
    list_per_page = 10
    actions = ['set_dollars', 'set_euro']
    search_fields = ['name', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, obj: Movie):
        if obj.rating < 5:
            return 'не стоит смотреть'
        if obj.rating < 7:
            return 'разок можно глянуть'
        if obj.rating <= 8:
            return 'норм'
        return 'топ'

    @admin.action(description='Установить валюту в доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(request,
                          f'Было обновлено {count_updated} записей',
                          messages.INFO
                          )


