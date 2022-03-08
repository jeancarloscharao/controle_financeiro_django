from django.contrib import admin
from .models import ContaPagar, StatusContaPagar
from django.contrib.auth.models import User


class ListandoStatusContaPagar(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id',)
    list_per_page = 10


admin.site.register(StatusContaPagar, ListandoStatusContaPagar)


class ListandoContaPagar(admin.ModelAdmin):
    readonly_fields = ('usuario', 'emissao')
    list_display = ('id', 'descricao', 'valor', 'emissao_br', 'data_vencimento', 'usuario', 'status')
    list_display_links = ('id',)
    fields = ['descricao', 'valor', 'emissao', 'data_vencimento', 'status', 'usuario']
    search_fields = ('descricao',)
    # list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        usuario = request.user
        obj.usuario = usuario
        super(ListandoContaPagar, self).save_model(request, obj, form, change)

    def emissao_br(self, obj):
        return obj.emissao.strftime("%d %b %Y %H:%M:%S")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)


admin.site.register(ContaPagar, ListandoContaPagar)
