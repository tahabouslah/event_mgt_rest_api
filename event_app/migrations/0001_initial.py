# Generated by Django 4.2.6 on 2023-11-16 10:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import event_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNumber', models.PositiveIntegerField(default=0)),
                ('street', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zipCode', models.PositiveIntegerField(default='')),
            ],
            options={
                'db_table': 'addresses',
                'ordering': ['zipCode'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, validators=[event_app.models.validate_alphanumeric])),
                ('description', models.TextField(default='', max_length=1000)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('poster', models.ImageField(upload_to='event_app/images/')),
                ('url', models.URLField(blank=True)),
                ('category', models.CharField(choices=[('CONF', 'Conference'), ('SEMI', 'Seminar'), ('CONG', 'Congress'), ('COUR', 'Course'), ('CONC', 'Concert'), ('FEST', 'Festival'), ('EXHI', 'Exhibition'), ('TOUR', 'Tournament'), ('OTHE', 'Other')], default='OTHE', max_length=4)),
            ],
            options={
                'db_table': 'events',
                'ordering': ['name', 'date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=150)),
                ('lastName', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=150, unique=True)),
                ('phone', models.CharField(default='', max_length=150)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.address')),
            ],
            options={
                'db_table': 'participants',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('nbPlaces', models.PositiveIntegerField(default=1)),
                ('reservationType', models.CharField(choices=[('VIP', 'Very important Person'), ('STD', 'Standard')], default='STD', max_length=10)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.event')),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.participant')),
            ],
            options={
                'db_table': 'reservations',
                'unique_together': {('event', 'participant')},
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('barCode', models.CharField(blank=True, max_length=150, null=True)),
                ('reservation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event_app.reservation')),
            ],
            options={
                'db_table': 'tickets',
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='participation',
            field=models.ManyToManyField(through='event_app.Reservation', to='event_app.event'),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=150)),
                ('phone', models.CharField(default='', max_length=150)),
                ('OrganizerEvents', models.ManyToManyField(to='event_app.event')),
            ],
            options={
                'db_table': 'organizers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=1000)),
                ('attitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.address')),
            ],
            options={
                'db_table': 'locations',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event_app.location'),
        ),
        migrations.CreateModel(
            name='Animator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=150)),
                ('lastName', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(default='', max_length=150, unique=True)),
                ('phone', models.CharField(default='', max_length=150)),
                ('url', models.URLField(blank=True, max_length=100, null=True)),
                ('AnimatorEvents', models.ManyToManyField(to='event_app.event')),
            ],
            options={
                'db_table': 'animators',
            },
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('name', 'date', 'time')},
        ),
    ]
