from django.core.management import call_command


def post_update():
    call_command('on_appengine', 'syncdb')
    # call_command('on_appengine', 'migrate')

