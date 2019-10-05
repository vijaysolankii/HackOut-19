from django.contrib import admin

# Register your models here.
from . models import User
from . models import Consultant
from . models import Taken
from . models import Chat
from . models import Appointment


admin.site.register(User)
admin.site.register(Consultant)
admin.site.register(Taken)
admin.site.register(Chat)
admin.site.register( Appointment)





