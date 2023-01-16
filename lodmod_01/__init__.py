import bpy
from bpy.types import Scene
from .lodmod_addon import DecimateModifierOperator
from bpy.types import Panel


bl_info = {
    "name": "lodmod_01",
    "author": "Matty Wyett-Simmonds",
    "blender" : (3, 4, 1),
    "version" : (1, 0),
    "location": "View3D > N-Panel > lodmod addon",
    "description": "Adds 5 iterations of lods to the selected model",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
    }

class VIEW3D_PT_lodmod_object_lodmod(Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "LODMOD Settings"
    bl_category = "LODMOD"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator(DecimateModifierOperator.bl_idname, text="Create LOD's")
        IntProperty = layout.prop(context.scene, "lod_count")
        FloatProperty = layout.prop(context.scene, "decimate_ratio")


classes = (DecimateModifierOperator, VIEW3D_PT_lodmod_object_lodmod)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.lodmod_addon = bpy.props.BoolProperty(name="lodmod_addon", default=False)
    bpy.types.Scene.lod_count = bpy.props.IntProperty(name="Number of LODs", default=5, min=1, max=10)
    bpy.types.Scene.decimate_ratio = bpy.props.FloatProperty(name="Decimation Ratio", default=0.5, min=0, max=1)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.lodmod_addon
    del bpy.types.Scene.lod_count
    del bpy.types.Scene.decimate_ratio



if __name__ == "__main__":
   register()
