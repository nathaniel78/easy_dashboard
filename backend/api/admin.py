from api.execute_query import SQLTaskRunner
from django.contrib import admin
from api.models import Host, SQL, Data
from api.forms import DataForm, HostForm


# TODO: Load information host
@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'host_active', 'data_create')
    search_fields = ('name', 'host_endpoint')
    
    SQLTaskRunner.run_sql()
    SQLTaskRunner.run_data()
    
    # TODO: Use the custom form
    form = HostForm


# TODO: Load information sql
@admin.register(SQL)
class SQLAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'host', 'data_create')
    search_fields = ('name',)
    list_filter = ('host',)
    
    SQLTaskRunner.run_sql()
    SQLTaskRunner.run_data()

# TODO: Load information Data
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sql', 'type_chart', 'emphasis', 'truncated_data_json', 'data_create')
    search_fields = ('name',)
    list_filter = ('type_chart', 'emphasis')
    
    SQLTaskRunner.run_sql()
    SQLTaskRunner.run_data()

    # TODO: Use the custom form
    form = DataForm

    # TODO: Customize the column that displays truncated JSON data
    def truncated_data_json(self, obj):
        max_length = 40
        if len(obj.data_json) > max_length:
            return f"{obj.data_json[:max_length]}..."
        return obj.data_json

    truncated_data_json.short_description = "Data JSON"
    
    # TODO: Override the list data view in the admin to run run_sql and run_data
    def changelist_view(self, request, extra_context=None):
        try:
            print("Chamando SQLTaskRunner na lista do admin...")
            SQLTaskRunner.run_sql()
            SQLTaskRunner.run_data()
        except Exception as e:
            self.message_user(request, f"Erro ao executar SQLTaskRunner: {e}", level="error")
            print(f"Erro ao executar SQLTaskRunner: {e}")

        # TODO: Continue with normal listing page rendering
        return super().changelist_view(request, extra_context=extra_context)

    
    
