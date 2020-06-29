from widget_jsmol import WidgetJmol
import ipywidgets as widgets

w = WidgetJmol()
display(w)

load_button = widgets.Button(description = 'Load Structure')
rotate_button = widgets.Button(description = 'Rotate')
invert_button = widgets.Button(description = 'Invert')
rotoinversion_button = widgets.Button(description = 'Rotoinversion')
reset_button = widgets.Button(description = 'Reset')
symops_button = widgets.Button(description = 'List All SymOps')

out = widgets.Output()

def load_structure(self):
    with out:
        w.script = 'load http://localhost:8888/tree/Crystallography/jmol_AMS_DATA_(2).cif'
        
def rotate(self):
    with out:
        w.script = 'rotate y 90 90'

def invert(self):
    with out:
        w.script = 'invertSelected'
        
def rotoinversion(self):
    with out:
        w.script = 'rotate y 90 90; delay 0.5; invertSelected'
        
def symops(self):
    with out:
        w.script = 'show SYMOP'


load_button.on_click(load_structure)
rotate_button.on_click(rotate)
invert_button.on_click(invert)
rotoinversion_button.on_click(rotoinversion)
reset_button.on_click(load_structure)
symops_button.on_click(symops)

bottom_row = widgets.HBox([rotate_button, invert_button, rotoinversion_button, out])
top_row = widgets.HBox([load_button, reset_button, out])
widgets.VBox([top_row, bottom_row])
