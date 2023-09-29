bl_info = {
    "name": "Kinetink",  # The name in the addon search menu
    "author": "phillip the Artgineer",
    "description": "a set of tools to create, style and rigg lines on 3D characters",
    "blender": (3, 6, 0),  # Lowest version to use
    "location": "View3D",
    "category": "Rigging",
}
import bpy
from . import libraryManagement

class kinetinkPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__
    
    def execute(self, context):
        print("hello world")
    
    def draw(self, context):
        layout = self.layout
        if bpy.context.preferences.filepaths.asset_libraries.get("kinetink test") is None:
            layout.operator('add.kinetinklib', icon= 'GEOMETRY_NODES')



def register():
    libraryManagement.register()
    bpy.utils.register_class(kinetinkPrefs)
    	
    
    

def unregister():
    libraryManagement.unregister()
    bpy.utils.unregister_class(kinetinkPrefs)
    
    


if __name__ == "__main__":
        register()




