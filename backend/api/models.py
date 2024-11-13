from django.db import models

# Model host
class Host(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    host_endpoint = models.CharField(max_length=50)
    host_username = models.CharField(max_length=50)
    host_password = models.CharField(max_length=150)
    host_port = models.PositiveIntegerField()
    data_create = models.DateTimeField(auto_now_add=True, editable=False)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Model sql
class SQL(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sql = models.TextField() 
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Model data
class Data(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    sql = models.ForeignKey(SQL, on_delete=models.CASCADE)
    data_cron = models.CharField(max_length=100)
    data_json = models.JSONField()
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Model dashboard
class Dashboard(models.Model):
    CONFIG_THEME_CHOICES = [
        ('light', 'Claro'),
        ('dark', 'Escuro'),
    ]
    
    config_sreem = models.CharField(max_length=5, choices=CONFIG_THEME_CHOICES, default='light')
    config_download = models.BooleanField(default=False)
    config_maintenance = models.BooleanField(default=False)
    config_navigation = models.BooleanField(default=True)

    def __str__(self):
        return f"Dashboard Config - {self.config_sreem}"


# Model chart
class Chart(models.Model):
    CHART_TYPE_CHOICES = [
        ('bar', 'Coluna'),
        ('line', 'Linha'),
        ('pie', 'Pizza'),
    ]

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    type_chart = models.CharField(max_length=5, choices=CHART_TYPE_CHOICES)
    order = models.PositiveIntegerField()  # Ordem para definir exibição
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
