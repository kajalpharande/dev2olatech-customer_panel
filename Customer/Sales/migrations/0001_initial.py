# Generated by Django 4.2.2 on 2023-07-05 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cl_Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='cl_Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100)),
                ('branch_list', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'RM',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_name', models.CharField(max_length=100)),
                ('branch_list', models.CharField(max_length=100)),
                ('ex_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('type_of_client', models.CharField(blank=True, choices=[('new', 'New Client'), ('existing', 'Existing Client'), ('decline', 'Decline Client'), ('po', 'PO Recieved')], max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_detail', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=254)),
                ('meeting_date', models.DateField()),
                ('next_meeting_date', models.DateField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('activation_date', models.DateField(blank=True, null=True)),
                ('renewal_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('customer_id', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(default='abc@olatechs.com', max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('roles', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cl_Executive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_name', models.CharField(max_length=100)),
                ('manager_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('branch_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sales.cl_branch')),
            ],
            options={
                'db_table': 'executive',
            },
        ),
    ]
