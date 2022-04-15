# Copy local axes orientation between meshes. The source mesh should be the active object. Keybind in 3D View > Object Mode
# Originally a script by batFINGER, converted to plugin that can be bound to a key and present in the space menu by sjain.
# Keybind in 3D View > Object Mode
# Can also be accessed as "Copy local axes orientation" in the Spacebar action menu.
# Original script source can be found at:
# https://blender.stackexchange.com/questions/230321/rotate-origin-only-to-match-other-object-rotation/230574#230574
# https://web.archive.org/web/20220407173521/https://blender.stackexchange.com/questions/230321/rotate-origin-only-to-match-other-object-rotation/230574
# https://archive.today/JbvrQ
# Short link: https://blender.stackexchange.com/a/230574/116468

bl_info = {
    "name": "Refresh materials",
    "author": "sjain",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Spacebar menu",
    "description": "For all selected objects, deletes their materials and adds a new blank Principled BSDF nodes material. Can be needed to fix some material things when copying models from Blender 27x sessions to 28x sessions.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}


import bpy
from mathutils import Matrix
from bpy import context

class RefreshMaterials(bpy.types.Operator):

    bl_idname = "object.refresh_materials"
    bl_label = "Refresh materials"
    bl_context = "objectmode"
    bl_category = "objectmode"



    def execute(self, context):


        for obj in bpy.context.selected_objects:

            obj.active_material_index = 0

            for i in range(len(obj.material_slots)):
                bpy.ops.object.material_slot_remove({'object': obj})

            bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=False)

            bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

            obj.data.materials.append(newMaterial())


        return {'FINISHED'}



def newMaterial():

    mat = bpy.data.materials.new("Material")

    mat.use_nodes = True

    return mat


# Registration

addon_keymaps = []

def register():
    bpy.utils.register_class(RefreshMaterials)



def unregister():
    bpy.utils.unregister_class(RefreshMaterials)


if __name__ == "__main__":
    register()
