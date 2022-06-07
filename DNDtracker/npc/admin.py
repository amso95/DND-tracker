from django.contrib import admin
from .models import Race, NPC, Names, MaleNames, FemaleNames, FamilyNames

admin.site.register(Race)
admin.site.register(NPC)
admin.site.register(Names)
admin.site.register(MaleNames)
admin.site.register(FemaleNames)
admin.site.register(FamilyNames)