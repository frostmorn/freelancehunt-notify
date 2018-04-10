from dbus.exceptions import DBusException
try:
    import gi
    gi.require_version('Notify', '0.7')
    from gi.repository import Notify

    class Notifier(object):
        def __init__(self, app_name, icon):
            self.icon = icon
            try:
                if Notify is not None:
                    Notify.init(app_name)
                    self.notifier = Notify
                self.enabled = True
            except DBusException:
                print("WARNING: No notification daemon found! "
                    "Notifications will be ignored.")
                self.enabled = False

        def notify(self, title, message, icon=None):
            if not self.enabled:
                return
            if icon is None:
                icon = self.icon
            if Notify is not None:
                notice = self.notifier.Notification.new(title, message, icon)
            notice.set_hint_string('x-canonical-append', '')
            try:
                notice.show()
            except:
                pass
except:

    pass