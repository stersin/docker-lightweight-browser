#!/usr/bin/env python2
# python-gtk-webkit presentation program.
# Copyright (C) 2009 by Akkana Peck.
# Share and enjoy under the GPL v2 or later.

import sys
import gobject
import gtk
import webkit
import dbus, dbus.service, dbus.glib

if len(sys.argv) > 1:
  url = sys.argv[1]
else:
  url = 'https://www.google.fr'

class MainApp:
    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self._browser = webkit.WebView()

        sw = gtk.ScrolledWindow()
        sw.add(self._browser)
        self.window.add(sw)
        self.window.show_all()
        self.window.fullscreen()
        
        self.window.connect("destroy", self.destroy)

    def open_url(self, url):
        self._browser.open(url)
        
    def destroy(self, sender):
        gtk.main_quit()

class Service(dbus.service.Object):
    def __init__(self, app):
        self.app = app
        bus_name = dbus.service.BusName('com.service.Workstation', bus = dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/com/service/Workstation')

    @dbus.service.method(dbus_interface='com.service.Workstation')
    def open_url(self, url):
        self.app.open_url(url)
        
if __name__ == "__main__":
    if dbus.SessionBus().request_name("com.service.Workstation") != dbus.bus.REQUEST_NAME_REPLY_PRIMARY_OWNER:
        print "application already running"
        method = dbus.SessionBus().get_object("com.service.Workstation", "/com/service/Workstation").get_dbus_method("open_url")
        method(url)
    else:
        print "running application"
        gobject.threads_init()
        app = MainApp()
        service = Service(app)
        service.open_url(url)
        gtk.main()
