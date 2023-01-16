import bpy

class DecimateModifierOperator(bpy.types.Operator):
    """Applies a decimate modifier set to collapse at 0.5 on the selected object and duplicate it 5 times"""
    bl_idname = "object.decimate_modifier_operator"
    bl_label = "Lodmod"

    def execute(self, context):
        # Get the selected objects
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            for i in range(bpy.context.scene.lod_count):
                # Duplicate the selected object
                duplicate = obj.copy()
                duplicate.data = obj.data.copy()
                duplicate.name = obj.name.replace("_LOD"+str(i),"") + "_LOD" + str(i+1)
                bpy.context.collection.objects.link(duplicate)

                # Add a decimate modifier to the duplicate object
                mod = duplicate.modifiers.new(name="Decimate", type='DECIMATE')

                # Set the decimate modifier to collapse at 0.5
                mod.ratio = bpy.context.scene.decimate_ratio
                obj = duplicate

                # Apply the modifier if checkbox enabled
                if (bpy.context.scene.apply_modifs):
                    bpy.context.view_layer.objects.active = duplicate
                    bpy.ops.object.modifier_apply(modifier="Decimate")
            #obj.select_set(False)
            #obj = duplicate
        return {'FINISHED'}
