from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.
from .models import Drone

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    # viewing expire the current sessions

    list_display=('session_key', 'username', 'expire_date','expire_session')

    def username(self,obj):
        session_data = obj.get_decoded()
        user_id = session_data.get('_auth_user_id')

        if user_id:
            user = User.objects.get(id=user_id)
            return user.username
        return None
    
    def expire_session(self, obj):
        return format_html('<a href="{}" class="btn">Expire session</a>', reverse('expire_session', args=[obj.pk]))
    
admin.site.register(Drone)