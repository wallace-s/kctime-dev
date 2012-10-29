from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

MONTH_CHOICES = (
    (datetime.date(year=2012, month=1, day=1),"2012年1月"),
    (datetime.date(year=2012, month=2, day=1),"2012年2月"),
    (datetime.date(year=2012, month=3, day=1),"2012年3月"),
    (datetime.date(year=2012, month=4, day=1),"2012年4月"),
    (datetime.date(year=2012, month=5, day=1),"2012年5月"),
    (datetime.date(year=2012, month=6, day=1),"2012年6月"),
    (datetime.date(year=2012, month=7, day=1),"2012年7月"),
    (datetime.date(year=2012, month=8, day=1),"2012年8月"),
    (datetime.date(year=2012, month=9, day=1),"2012年9月"),
    (datetime.date(year=2012, month=10, day=1),"2012年10月"),
    (datetime.date(year=2012, month=11, day=1),"2012年11月"),
    (datetime.date(year=2012, month=12, day=1),"2012年12月"),
)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]



class Timesheet(models.Model):
        sheet_month = models.DateField(choices=MONTH_CHOICES)
        user = models.ForeignKey(User)

        def __unicode__(self):
               return u"time sheet for %s for %s年 %s月" % (self.user.username, self.sheet_month.year, self.sheet_month.month)
        
        class Meta:
            unique_together = (("user", "sheet_month"),)

class TimeDuration(models.Model):
        start_time = models.TimeField(help_text="テスティングのヘルプのテキスト")
        end_time = models.TimeField()
        paid_time_boolean = models.BooleanField(default="TRUE")
        timesheet = models.ForeignKey(Timesheet)

        def __unicode__(self):
                return str(self.start_time) + " to " + str(self.end_time)

        # def timediff(self):
                # return datetime.timedelta(end_time, start_time)
        #add a method here to return the duration between the two times

    