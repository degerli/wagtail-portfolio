# Generated by Django 2.1.5 on 2019-02-10 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your name', max_length=255)),
                ('heading', models.CharField(help_text='Your title', max_length=255)),
                ('email', models.CharField(help_text='Your email', max_length=255)),
                ('telephone', models.CharField(help_text='Your telephone', max_length=255)),
                ('social_linkedin', models.URLField(max_length=255, null=True)),
                ('social_twitter', models.URLField(max_length=255, null=True)),
                ('social_github', models.URLField(max_length=255, null=True)),
                ('profile_pic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
