from atexit import register
from django.contrib import admin
from .models import *

#from .models import Catagory
#from .models import Product  -you can use this method to import 

"""class CategoryAdmin(admin.ModelAdmin):
        list_display=('name','image','description')
admin.site.register(Catagory,CategoryAdmin)"""

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)









