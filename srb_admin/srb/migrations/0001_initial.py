# Generated by Django 4.1.7 on 2023-03-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
                'db_table': 'classroom',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Район')),
                ('language', models.CharField(blank=True, max_length=2, null=True, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
                'db_table': 'district',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='User_id')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('amount', models.BigIntegerField(blank=True, null=True, verbose_name='Цена')),
                ('type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Финансы',
                'verbose_name_plural': 'Финанс',
                'db_table': 'finance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=250, null=True, verbose_name='Вопрос')),
                ('language', models.CharField(blank=True, max_length=2, null=True, verbose_name='Язык')),
                ('classes', models.CharField(blank=True, max_length=2, null=True, verbose_name='Класс')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'db_table': 'quiz',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Регион')),
                ('language', models.CharField(blank=True, max_length=2, null=True, verbose_name='Язык')),
            ],
            options={
                'verbose_name': 'Регион',
                'verbose_name_plural': 'Регионы',
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Школа')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
                'db_table': 'school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True)),
                ('other_id', models.BigIntegerField(blank=True, null=True)),
                ('other_photo', models.CharField(blank=True, max_length=150, null=True)),
                ('other_name', models.CharField(blank=True, max_length=100, null=True)),
                ('other_lang', models.CharField(blank=True, max_length=2, null=True)),
                ('question', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'subscribe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(blank=True, null=True, verbose_name='Время регистра')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='User_id')),
                ('referral', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка')),
                ('ref_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Рефералка')),
                ('count_ref', models.CharField(blank=True, max_length=7, null=True, verbose_name='Кол-во приглашенных')),
                ('language', models.CharField(blank=True, max_length=2, null=True, verbose_name='Язык')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ф/И')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Никнейм')),
                ('age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Год рождения')),
                ('gender', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пол')),
                ('photo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фото')),
                ('school', models.CharField(blank=True, max_length=10, null=True, verbose_name='Школа')),
                ('classroom', models.CharField(blank=True, max_length=50, null=True, verbose_name='Класс')),
                ('subscribe', models.BooleanField(default=False, verbose_name='Подписка')),
                ('time_start', models.CharField(blank=True, max_length=25, null=True, verbose_name='Начало подписки')),
                ('time_end', models.CharField(blank=True, max_length=25, null=True, verbose_name='Конец подписки')),
                ('region', models.CharField(blank=True, max_length=50, null=True, verbose_name='Регион')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name='Район')),
                ('like', models.BigIntegerField(blank=True, null=True, verbose_name='Огоньки')),
                ('ban', models.BooleanField(blank=True, null=True, verbose_name='Блок')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
