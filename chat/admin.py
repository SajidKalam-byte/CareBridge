from django.contrib import admin
from .models import Chat, DoctorAIResponse, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "parent", "doctor")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "chat", "sender", "text", "created_at")


@admin.register(DoctorAIResponse)
class DoctorAIResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "chat", "doctor", "parent", "child", "created_at")