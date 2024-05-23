# Generated by Django 4.2.6 on 2024-05-15 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import operation.contact.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('title', models.CharField(choices=[('ceo', 'CEO'), ('company_rep', 'Company Representative'), ('independent_professional', 'Independent Professional'), ('entrepreneur', 'Entrepreneur'), ('student', 'Student')], max_length=50)),
                ('primary_email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('mobile_phone', models.CharField(blank=True, max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('erased', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts_company', to='company.company')),
                ('country', models.ForeignKey(limit_choices_to={'is_selected': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='country.country')),
                ('created_by', models.ForeignKey(on_delete=models.SET(operation.contact.models.get_sentinel_user), related_name='created_contact', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(on_delete=models.SET(operation.contact.models.get_sentinel_user), related_name='last_modified_contact', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_organization', to='organization.organization')),
            ],
        ),
    ]
