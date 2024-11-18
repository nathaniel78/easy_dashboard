from django.db import models

# Model host
class Host(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    host_endpoint = models.CharField(max_length=50, blank=False, null=False)
    host_username = models.CharField(max_length=50, blank=False, null=False)
    host_password = models.CharField(max_length=150)
    host_port = models.PositiveIntegerField()
    data_create = models.DateTimeField(auto_now_add=True, editable=False)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Model sql
class SQL(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    sql = models.TextField(blank=False, null=False) 
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Model data
class Data(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=100)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    sql = models.ForeignKey(SQL, on_delete=models.CASCADE)
    data_cron = models.CharField(max_length=100)
    data_json = models.TextField(default='{}')
    type_chart = models.IntegerField(default=1, blank=False, null=False)
    emphasis = models.BooleanField(default=False)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

