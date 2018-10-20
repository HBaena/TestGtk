import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class GenericWindow(Gtk.Window):
    """docstring for MyWindow"""
    def __init__(self, *args):
        Gtk.Window.__init__(self, title = args[0])
        self.connect("destroy", Gtk.main_quit)
