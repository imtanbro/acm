from django.contrib import admin
from .models import Post ,Updates , upcomingEvents ,pastEvents

admin.site.register(Post)
admin.site.register(Updates)
admin.site.register(upcomingEvents)
admin.site.register(pastEvents)
