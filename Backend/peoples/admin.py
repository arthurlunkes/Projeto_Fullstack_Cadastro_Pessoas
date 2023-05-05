from django.contrib import admin

class Cliente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'email', 'data_nascimento', 'tipo_cliente')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
