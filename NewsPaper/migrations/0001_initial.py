# Generated by Django 4.2 on 2023-04-11 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(default=0)),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_post', models.CharField(choices=[('AR', 'статья'), ('NE', 'новость')], default='NE', max_length=2, verbose_name='Тип поста')),
                ('datetime_post', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время поста')),
                ('header', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField()),
                ('rating_post', models.IntegerField(default=0)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.author', verbose_name='Имя автора')),
            ],
            options={
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='SubscribersCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.category')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Категории подписчиков',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
            ],
            options={
                'verbose_name_plural': 'Категории постов',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category_post',
            field=models.ManyToManyField(through='NewsPaper.PostCategory', to='NewsPaper.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField(max_length=255, verbose_name='Текст комментария')),
                ('datetime_comment', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время комментария')),
                ('rating_comment', models.IntegerField(default=0, verbose_name='Рейтинг комментария')),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='NewsPaper.SubscribersCategory', to=settings.AUTH_USER_MODEL),
        ),
    ]
