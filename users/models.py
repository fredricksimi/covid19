from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	def __str__(self):
		return self.username

# class Doctor(AbstractUser):
# 	first_name = models.CharField(blank = True, max_length = 20)
# 	last_name = models.CharField(blank = True, max_length = 20)
# 	phone_number = models.CharField(blank = True, max_length=20)
# 	# - - - Some more User fields according to your need s


# 	# This is the most important part to look upon to  define the custom permissions related to User.
# 	class Meta:
# 		permissions = (("can_go_in_non_ac_bus", "To provide non-AC Bus facility"),
# 						("can_go_in_ac_bus", "To provide AC-Bus facility"),
# 						("can_stay_ac-room", "To provide staying at AC room"),
# 						("can_stay_ac-room", "To provide staying at Non-AC room"),
# 						("can_go_dehradoon", "Trip to Dehradoon"),
# 						("can_go_mussoorie", "Trip to Mussoorie"),
# 						("can_go_haridwaar", "Trip to Haridwaar"),
# 						("can_go_rishikesh", "Trip to Rishikesh"))