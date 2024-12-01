import os
import sys

from django.core.wsgi import get_wsgi_application

project_home = "/home/yurahaurylenka/test_task_referral"
if project_home not in sys.path:
    sys.path.append(project_home)

activate_this = "/home/your-username/your-project/venv/bin/activate_this.py"
exec(open(activate_this).read(), dict(__file__=activate_this))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "referral_test_task.settings")

application = get_wsgi_application()
