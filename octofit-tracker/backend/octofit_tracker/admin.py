from django.contrib import admin

from octofit_tracker.models import ActivityLog, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(ActivityLog)
admin.site.register(LeaderboardEntry)
admin.site.register(WorkoutSuggestion)
