from django.contrib import admin
from .models import *


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id",
                    "time_created",
                    "user_id",
                    "language",
                    "full_name",
                    "nickname",
                    "age",
                    "gender",
                    "region",
                    "district",
                    "school",
                    "classroom",
                    "photo",
                    "like",
                    "referral",
                    "ref_id",
                    "count_ref",
                    "time_start",
                    "time_end",
                    "subscribe",
                    "ban")
    search_fields = ['full_name']
    search_help_text = ['full_name']
    # list_display_links = ("user_id",)


@admin.register(Quiz)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "language", "classes")


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "language")


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("region", "name", "language")


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("number", "district")


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("school", "number")


@admin.register(Finance)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("user_id", "full_name", "amount", "type")
    search_fields = ['full_name']
    search_help_text = ['full_name']