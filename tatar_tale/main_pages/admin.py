from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import AllInfoTales, TalesInfo, LearnedWords, Characteristic, Profile, AllLessons


class AllInfoTalesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_tales', 'author', 'count_lessons')


class TalesInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'all_info_tales', 'percent_progress')
    list_filter = ('all_info_tales',)


class LearnedWordsAdmin(admin.ModelAdmin):
    list_display = ('words',)


class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('pk','all_completed_lessons', 'completed_tales', 'last_completed_tales', 'display_learned_words')

    def display_learned_words(self, obj):
        return ", ".join([word.words for word in obj.learned_words.all()])

    display_learned_words.short_description = 'Learned Words'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'email', 'language_level', 'image_preview', 'characteristic', 'display_progress_user')
    list_filter = ('language_level', 'characteristic')

    def image_preview(self, obj):
        # Отображение изображения в админке
        if obj.profile_image:
            image_id = obj.pk
            url = reverse('get_image', args=[image_id])
            return format_html('<img src="{}" alt="Image" style="max-width: 100px; max-height: 100px;" />', url)
        return None

    image_preview.short_description = 'Image Preview'

    def display_progress_user(self, obj):
        return ", ".join([f"{tale_info.all_info_tales.name_tales}: {tale_info.percent_progress}%" for tale_info in obj.tales_info_progress_id.all()])

    display_progress_user.short_description = 'Progress'


class AllLessonsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'all_info_tales', 'lessons_file')
    list_filter = ('all_info_tales',)


admin.site.register(AllInfoTales, AllInfoTalesAdmin)
admin.site.register(TalesInfo, TalesInfoAdmin)
admin.site.register(LearnedWords, LearnedWordsAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(AllLessons, AllLessonsAdmin)
