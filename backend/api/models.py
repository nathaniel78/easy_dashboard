from django.db import models
from django.core.exceptions import ValidationError

# TODO: Model host
class Host(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    host_db_drive = models.PositiveIntegerField()
    host_endpoint = models.CharField(max_length=50, blank=False, null=False)
    host_db_name = models.CharField(max_length=50, blank=False, null=False)
    host_username = models.CharField(max_length=50, blank=False, null=False)
    host_password = models.CharField(max_length=150)
    host_port = models.PositiveIntegerField()
    host_active = models.BooleanField(default=True)
    data_create = models.DateTimeField(auto_now_add=True, editable=False)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        
        # Valida o campo type_chart no modelo
        if self.host_db_drive not in [1, 2]:
            raise ValidationError(
                "Valores aceitos: 1 (postgres), 2 (mysql)"
            )
    
    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)


# TODO: Model sql
class SQL(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    sql = models.TextField(blank=False, null=False) 
    result = models.JSONField(blank=True, null=True)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# TODO: Model data
class Data(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    sql = models.ForeignKey(SQL, on_delete=models.CASCADE)
    data_json = models.TextField(default='{}')
    type_chart = models.IntegerField(default=1, blank=False, null=False)
    emphasis = models.BooleanField(default=False)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        super().clean()
        
        # Valida o campo type_chart no modelo
        if self.type_chart not in [1, 2, 3, 4]:
            raise ValidationError(
                "Valores aceitos: 1 (barra empilhada), 2 (área empilhada), 3 (bolha empilhada), 4 (barra horizontal)"
            )
    
    def save(self, *args, **kwargs):
        self.clean()  # Chama a validação personalizada antes de salvar
        super().save(*args, **kwargs)

