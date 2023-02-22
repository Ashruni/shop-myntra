from django.contrib import admin

# Register your models here.
from.models import *
# regshopmodels
# shopuploadmodels
# profile
# cart
# wishlist
# buy
# customercard
admin.site.register(regshopmodels)
admin.site.register(shopuploadmodels)
admin.site.register(profile)
admin.site.register(cart)
admin.site.register(buy)
admin.site.register(customercard)
admin.site.register(shopnotification)
admin.site.register(usernotification)