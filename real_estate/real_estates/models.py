# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    voivodeship = models.CharField(max_length=255, blank=True, null=True)
    amount_of_citizens = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class RealEstates(models.Model):
    url = models.URLField(primary_key=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    rent = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)

    deposit = models.FloatField(blank=True, null=True)
    floor = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    #link = models.ForeignKey(Links, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'real_estates'

    def __str__(self):
        return f'Link do ogłoszenia: {self.url} \n' \
                f'Cena całkowita: {self.total_price} \n' \
                f'Cena: {self.price} \n' \
                f'Czynsz: {self.rent} \n' \
                f'Waluta: {self.currency} \n' \
                f'Powierzchnia: {self.area} \n' \
                f'Pokoje: {self.rooms} \n' \
                f'Depozyt: {self.deposit} \n' \
                f'Piętro: {self.floor} \n' \
                f'Typ: {self.type} \n' \
                f'Status: {self.status}' \
                f'Region: {self.region}'

class Links(models.Model):
    url = models.URLField(primary_key=True)
    city_name = models.CharField(max_length=255, blank=True, null=True)
    type_of_estate = models.CharField(max_length=255, blank=True, null=True)
    type_of_offer = models.CharField(max_length=255, blank=True, null=True)
    used = models.BooleanField(blank=True, null=True)
    #is_active = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.city_name} {self.type_of_estate}"

    class Meta:
        managed = False
        db_table = 'links'

