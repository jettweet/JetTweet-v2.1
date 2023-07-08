# Generated by Django 4.2 on 2023-07-06 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ادرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا می خواید نمییش داداه شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='مقاله ی پست')),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='عکس برای پست')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('private', models.BooleanField(default=False, verbose_name='خصوصی')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='ویدیو')),
                ('video_not_music', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='ویدیوی بی صدا')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='articles', to='pages.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ['-publish'],
            },
        ),
    ]