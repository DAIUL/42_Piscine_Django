from django.conf import settings
import random, time

def inject_username(request):
	username = request.session.get("username")
	username_expires_at = request.session.get("username_expires_at")

	now = int(time.time())
	if not username or not username_expires_at or now > username_expires_at:
		username = random.choice(settings.USERNAMES)
		request.session["username"] = username
		request.session["username_expires_at"] = now + 42

	return {"username": username}