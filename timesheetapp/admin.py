﻿from timesheetapp.models import Timesheet, TimeDurationfrom django.contrib import adminclass TimeDurationInline(admin.StackedInline):	model = TimeDuration	extra = 0	fieldsets = (	("Time Stamps", {"fields":("start_time","end_time"),						"classes":("collapse",)}),	)	class TimesheetAdmin(admin.ModelAdmin):	fieldsets = ((None, {"fields":("sheet_month","user")}),)	inlines = [TimeDurationInline]admin.site.register(Timesheet, TimesheetAdmin)