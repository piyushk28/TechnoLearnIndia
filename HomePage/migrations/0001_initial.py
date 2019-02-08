# Generated by Django 2.1.5 on 2019-02-08 16:19

import HomePage.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=HomePage.models.HomeImage.upload_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('about_title_first', models.CharField(max_length=70)),
                ('about_first', models.TextField(max_length=300)),
                ('about_title_second', models.CharField(max_length=70)),
                ('about_second', models.TextField(max_length=300)),
                ('contact_no', models.BigIntegerField()),
                ('conatct_email', models.EmailField(max_length=254)),
                ('facebook_url', models.URLField(blank=True, help_text='Optional,  If added respective site icon will be shown on the home page', null=True)),
                ('instagram_url', models.URLField(blank=True, help_text='Optional,  If added respective site icon will be shown on the home page', null=True)),
                ('twitter_url', models.URLField(blank=True, help_text='Optional,  If added respective site icon will be shown on the home page', null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.BigIntegerField()),
                ('full_name', models.CharField(max_length=60)),
                ('father_name', models.CharField(max_length=60)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField(max_length=250)),
                ('city', models.CharField(choices=[('Delhi', 'Delhi'), ('Gurgaon', 'Gurgaon'), ('Noida', 'Noida'), ('Faridabad ', 'Faridabad '), ('Ghaziabad', 'Ghaziabad'), ('Jaipur', 'Jaipur'), ('Other', 'Other')], max_length=255)),
                ('pin_code', models.PositiveIntegerField()),
                ('school_name', models.CharField(max_length=100)),
                ('student_class', models.CharField(choices=[('5th', 'V'), ('6th', 'VI'), ('7th', 'VII'), ('8th', 'VIII'), ('9th', 'IX'), ('10th', 'X'), ('11th', 'XI'), ('12th', 'XII'), ('Other', 'Other')], max_length=15)),
                ('reference', models.CharField(choices=[('social_site', 'Social Site'), ('pamphlet', 'Pamphlet'), ('website', 'Website'), ('friend', 'Friend'), ('Other', 'Other')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='homeimage',
            name='home_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.HomePage'),
        ),
    ]
