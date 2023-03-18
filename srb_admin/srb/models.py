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


class Classroom(models.Model):
    number = models.CharField(max_length=50, blank=True, null=True, verbose_name='Класс')
    school = models.ForeignKey('School', models.DO_NOTHING, blank=True, null=True, verbose_name='Школа')

    class Meta:
        managed = False
        db_table = 'classroom'
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return str(self.number)


class District(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Район')
    language = models.CharField(max_length=2, blank=True, null=True, verbose_name='Язык')
    region = models.ForeignKey('Region', models.DO_NOTHING, blank=True, null=True, verbose_name='Регион')

    class Meta:
        managed = False
        db_table = 'district'
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return str(self.name)


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


class Finance(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True, verbose_name='User_id')
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Имя')
    amount = models.BigIntegerField(blank=True, null=True, verbose_name='Цена')
    type = models.CharField(max_length=10, blank=True, null=True, verbose_name='Тип')

    class Meta:
        managed = False
        db_table = 'finance'
        verbose_name = 'Финансы'
        verbose_name_plural = 'Финанс'

    def __str__(self):
        return str(self.user_id)


class Quiz(models.Model):
    question = models.CharField(max_length=250, blank=True, null=True, verbose_name='Вопрос')
    language = models.CharField(max_length=2, blank=True, null=True, verbose_name='Язык')
    classes = models.CharField(max_length=2, blank=True, null=True, verbose_name='Класс')

    class Meta:
        managed = False
        db_table = 'quiz'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.question)


class Region(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Регион')
    language = models.CharField(max_length=2, blank=True, null=True, verbose_name='Язык')

    class Meta:
        managed = False
        db_table = 'region'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return str(self.name)


class School(models.Model):
    number = models.CharField(max_length=50, blank=True, null=True,  verbose_name='Школа')
    district = models.ForeignKey(District, models.DO_NOTHING, blank=True, null=True, verbose_name='Район')

    class Meta:
        managed = False
        db_table = 'school'
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return str(self.number)


class Subscribe(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    other_id = models.BigIntegerField(blank=True, null=True)
    other_photo = models.CharField(max_length=150, blank=True, null=True)
    other_name = models.CharField(max_length=100, blank=True, null=True)
    other_lang = models.CharField(max_length=2, blank=True, null=True)
    question = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribe'


class Users(models.Model):
    time_created = models.DateTimeField(blank=True, null=True, verbose_name='Время регистра')
    user_id = models.BigIntegerField(blank=True, null=True, verbose_name='User_id')
    referral = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка')
    ref_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='Рефералка')
    count_ref = models.CharField(max_length=7, blank=True, null=True, verbose_name='Кол-во приглашенных')
    language = models.CharField(max_length=2, blank=True, null=True, verbose_name='Язык')
    full_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Ф/И')
    nickname = models.CharField(unique=True, max_length=50, blank=True, null=True, verbose_name='Никнейм')
    age = models.CharField(max_length=100, blank=True, null=True, verbose_name='Год рождения')
    gender = models.CharField(max_length=50, blank=True, null=True, verbose_name='Пол')
    photo = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фото')
    school = models.CharField(max_length=10, blank=True, null=True, verbose_name='Школа')
    classroom = models.CharField(max_length=50, blank=True, null=True, verbose_name='Класс')
    subscribe = models.BooleanField(default=False, verbose_name='Подписка')
    time_start = models.CharField(max_length=25, blank=True, null=True, verbose_name='Начало подписки')
    time_end = models.CharField(max_length=25, blank=True, null=True, verbose_name='Конец подписки')
    region = models.CharField(max_length=50, blank=True, null=True, verbose_name='Регион')
    district = models.CharField(max_length=100, blank=True, null=True, verbose_name='Район')
    like = models.BigIntegerField(blank=True, null=True, verbose_name='Огоньки')
    ban = models.BooleanField(blank=True, null=True, verbose_name='Блок')

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.user_id)
