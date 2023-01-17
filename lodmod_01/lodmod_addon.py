import bpy
from mathutils import Vector

class DecimateModifierOperator(bpy.types.Operator):
    """Applies a decimate modifier set to collapse at 0.5 on the selected object and duplicate it 5 times"""
    bl_idname = "object.decimate_modifier_operator"
    bl_label = "Lodmod"

    def execute(self, context):
        # Get the selected objects
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            original_name = obj.name
            if (bpy.context.scene.add_lod0_name):
                obj.name = original_name + "_LOD0"
            if (bpy.context.scene.make_collections):
                new_collection = bpy.data.collections.new(original_name)
                bpy.context.scene.collection.children.link(new_collection)
                obj.users_collection[0].objects.unlink(obj)
                new_collection.objects.link(obj)
            for i in range(bpy.context.scene.lod_count):
                # Duplicate the selected object
                duplicate = obj.copy()
                duplicate.data = obj.data.copy()
                duplicate.name = original_name + "_LOD" + str(i+1)
                bpy.context.collection.objects.link(duplicate)
                if (bpy.context.scene.make_collections):
                    duplicate.users_collection[0].objects.unlink(duplicate)
                    new_collection.objects.link(duplicate)
                # Create an undo context
                bpy.ops.ed.undo_push(message="Duplicate Location Change")
                # move the object on x axis
                duplicate.location += Vector((bpy.context.scene.lineup_offset * (i+1), 0, 0))
                # Close the undo context
                bpy.ops.ed.undo_push(message="Duplicate Location Change")




                # Check if the duplicate object already has a decimate modifier
                decimate_modifier = None
                for mod in duplicate.modifiers:
                    if mod.type == 'DECIMATE':
                        decimate_modifier = mod
                        break

                # If the object does not have a decimate modifier, add one
                if decimate_modifier is None:
                    decimate_modifier = duplicate.modifiers.new(name="Decimate", type='DECIMATE')

                # Set the decimate modifier ratio based on the current iteration

                decimate_modifier.ratio = (bpy.context.scene.decimate_ratio) ** (i + 1)

                # Apply the modifier if checkbox enabled
                if (bpy.context.scene.apply_modifs):
                    bpy.context.view_layer.objects.active = duplicate
                    bpy.ops.object.modifier_apply(modifier="Decimate")

        return {'FINISHED'}
