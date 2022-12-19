from django.contrib import admin
from .models import *
from .models import *

# Register your models here.


from .models import Category
admin.site.register(Category)

from .models import Opinion
admin.site.register(Opinion)

from .models import Gallery
admin.site.register(Gallery)



