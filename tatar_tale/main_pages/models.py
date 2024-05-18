from django.contrib.auth.models import User
from django.db import models


class AllInfoTales(models.Model):
    name_tales = models.CharField(max_length=40)
    author = models.CharField(max_length=20)
    count_lessons = models.IntegerField()


class TalesInfo(models.Model):
    all_info_tales = models.ForeignKey(AllInfoTales, on_delete=models.CASCADE)
    percent_progress = models.IntegerField()


class LearnedWords(models.Model):
    words = models.CharField(max_length=30)


class Characteristic(models.Model):
    all_completed_lessons = models.IntegerField(default=0)
    learned_words = models.ManyToManyField(LearnedWords, null=True, blank=True)
    completed_tales = models.IntegerField(default=0)
    last_completed_tales = models.ForeignKey(TalesInfo, on_delete=models.CASCADE, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=30)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE)
    language_level = models.IntegerField(default=0)
    profile_image = models.ImageField(upload_to='profiles_image/', blank=True, null=True)
    tales_info_progress_id = models.ManyToManyField(TalesInfo, null=True, blank=True)


class AllLessons(models.Model):
    all_info_tales = models.ForeignKey(AllInfoTales, on_delete=models.CASCADE)
    lessons_file = models.FileField(upload_to='lessons/', blank=True, null=True)
