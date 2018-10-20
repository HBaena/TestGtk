import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BtnAddNote(Gtk.Button):
    """docstring for BtnAddNote"""
    def __init__(self, *arg):
        Gtk.Button.__init__(self, label = arg[0])
        
    def on_addnote_click(self, widget, window):
        add_note(window.notebook, window.entry, window.number_notes)
        window.number_notes += 1

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Simple Notebook Example')
        self.set_border_width(3)

        self.notebook = Gtk.Notebook()
        self.number_notes = 1
        page1 = Gtk.Box()
        page1.set_border_width(10)
        page1.add(Gtk.Label('Default Page!'))
        self.notebook.append_page(page1, Gtk.Label('Plain Title'))

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL) 
        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL) 
        self.entry = Gtk.Entry()
        label = Gtk.Label()
        label.set_markup('Enter new note!')
        button  =  BtnAddNote("Hola") 
        button.connect('clicked', button.on_addnote_click, self)
        self.entry.connect('key_press_event', self.on_addnote_keypress)
        self.hbox.pack_start(label, True, True, 0)
        self.hbox.pack_start(self.entry, True, True, 0)
        self.hbox.pack_start(button, True, True, 0)

        self.vbox.pack_start(self.notebook, True, True, 0)
        self.vbox.pack_start(self.hbox,     True, True, 0) 
        self.add(self.vbox)

    def on_addnote_keypress(self, widget, keyEvent):
        if keyEvent.keyval == 65293 and self.entry.get_text() != '':
            add_note(self.notebook, self.entry, self.number_notes)
            self.number_notes += 1

        
        

def make_note(txt):
    note = Gtk.Box()
    note.set_border_width(10)
    note.add(Gtk.Label(txt))
    return note
def add_note(notebook,entry, number):
    notebook.append_page(make_note(entry.get_text()), Gtk.Label('Note ' + str(number)))                        
    notebook.show_all()
    entry.set_text("")


#print dir(Gdk.EventKey.props)
win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()