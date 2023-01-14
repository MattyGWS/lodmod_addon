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

import bpy
from .lodmod_addon import DecimateModifierOperator

classes = (DecimateModifierOperator, )

def register():
        bpy.utils.register_class(DecimateModifierOperator)
        bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
        bpy.utils.unregister_class(DecimateModifierOperator)
        bpy.types.VIEW3D_MT_object.remove(menu_func)

def menu_func(self, context):
    self.layout.operator(DecimateModifierOperator.bl_idname)

if __name__ == "__main__":
    register()
