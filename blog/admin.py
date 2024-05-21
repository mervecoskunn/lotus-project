from django.contrib import admin
from .models import Post, Contact, Newsletter, DraftPost


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(DraftPost)
