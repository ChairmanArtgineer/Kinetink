import bpy
import pathlib


def get_SelfPath(context):
    # check if we are running from the Text Editor
    if context.space_data != None and context.space_data.type == "TEXT_EDITOR":
        # get the path to the SAVED TO DISK script when running from blender
        print("bpy.context.space_data script_path")
        scriptPath = context.space_data.text.filepath
    else:
        print("__file__ script_path")
        # __file__ is built-in Python variable that represents the path to the script
        scriptPath = __file__

    print(f"script_path -> {scriptPath}")
    #get folder where script is in
    scriptDir = pathlib.Path(scriptPath).resolve().parent
    print(f"[pathlib] scriptDir -> {scriptDir}")
    return scriptDir


def add_assLib(libName,libPath,libMethod):
    #create a new library and asign the reference to a variable 
    bpy.ops.preferences.asset_library_add()
    print(f'[Kinetink] {libName} library created!')
    kinetinkLibrary = bpy.context.preferences.filepaths.asset_libraries[-1] 
    #set name to kinetink 
    kinetinkLibrary.name = libName
    # set  the path to kinetink blend file 
    kinetinkLibrary.path = libPath
    # set import method 
    kinetinkLibrary.import_method = libMethod


#remove asset from asset library function :
def remove_assLib(libName):
    for i, assetLib in enumerate(bpy.context.preferences.filepaths.asset_libraries):
        if assetLib.name == libName:
            print( i, assetLib.name)
            bpy.ops.preferences.asset_library_remove(index=i)
            


class add_KinetinkLib(bpy.types.Operator):
    """creates kinetink asset library """
    bl_idname = "add.kinetinklib"
    bl_label = "add kientink library"
    
    def execute(self, context):
        
        #get self path to the addon folder 
        selfDir = get_SelfPath(context)
        # get a path to kinetink asset files 
        kinetinkPath = str(selfDir /"assets"/"kinetikink assets.blend")
        print(f"path_to_file -> {kinetinkPath}")
        
        add_assLib("Kinetink", kinetinkPath, 'LINK')
        return {'FINISHED'}           
        
class remove_KinetinkLib(bpy.types.Operator):
    """deletes kinetink asset library """
    bl_idname = "remove.kinetinklib"
    bl_label = "remove kientink library"
    
    def execute(self, context):
        remove_assLib("Kinetink")
        return {'FINISHED'}
    

            
blenderClasses = [
add_KinetinkLib,
remove_KinetinkLib]

def register():
    for bClass in blenderClasses:
        bpy.utils.register_class(bClass)
    
    
def unregister():
    bpy.ops.remove.kinetinklib()
    for bClass in blenderClasses:
        bpy.utils.unregister_class(bClass)
        

        

