from django.contrib import admin

# Register your models here.



# from django.contrib import admin
#
# from models import Test
#
# # Register your models here.
# admin.site.register(Test)

# from django.contrib import admin
# from models import Test, Contact, Tag
#
# # Register your models here.
# admin.site.register([Test, Contact, Tag])


# from django.contrib import admin
# from models import Test, Contact, Tag
#
#
# # Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ('name', 'email')
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])


# from django.contrib import admin
# from models import Test, Contact, Tag
#
#
# # Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),  # CSS
#             'fields': ('age',),
#         }]
#     )
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test, Tag])


# from django.contrib import admin
# from models import Test, Contact, Tag
#
#
# # Register your models here.
# class TagInline(admin.TabularInline):
#     model = Tag
#
#
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [TagInline]  # Inline
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),
#             'fields': ('age',),
#         }]
#
#     )
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test])


# from django.contrib import admin
# from models import Test, Contact, Tag
#
#
# # Register your models here.
# class TagInline(admin.TabularInline):
#     model = Tag
#
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'email')  # list
#     inlines = [TagInline]  # Inline
#     fieldsets = (
#         ['Main', {
#             'fields': ('name', 'email'),
#         }],
#         ['Advance', {
#             'classes': ('collapse',),
#             'fields': ('age',),
#         }]
#
#     )
#
#
# admin.site.register(Contact, ContactAdmin)
# admin.site.register([Test])


from django.contrib import admin
from models import Test, Contact, Tag


# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])