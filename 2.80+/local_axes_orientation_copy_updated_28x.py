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
    "name": "Copy local axes orientation between meshes",
    "author": "batFINGER, sjain",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Spacebar menu",
    "description": "Copy local axes orientation between meshes. The source mesh should be the active object. Keybind in 3D View > Object Mode",
    "warning": "",
    "wiki_url": "https://blender.stackexchange.com/questions/230321/rotate-origin-only-to-match-other-object-rotation/230574#230574",
    "tracker_url": "",
    "category": "Object"}


import bpy
from mathutils import Matrix
from bpy import context

class CopyLocalAxesOrientation(bpy.types.Operator):

    bl_idname = "object.copy_local_axes"
    bl_label = "Copy local axes orientation"
    bl_context = "objectmode"
    bl_category = "objectmode"



    def execute(self, context):

        ob = context.object
        mw = ob.matrix_world
        # rotational part
        R = mw.to_3x3().normalized().to_4x4()

        for o in context.selected_objects:
            if o is ob:
                continue
            mw = o.matrix_world
            Rloc = mw.to_3x3().normalized().to_4x4().inverted() @ R
            o.matrix_world = (
                Matrix.Translation(mw.translation) @
                R @
                Matrix.Diagonal(mw.to_scale()).to_4x4()
            )

            o.data.transform(Rloc.inverted())

        return {'FINISHED'}


def Rotate(myMesh, mat):
    for v in myMesh.vertices:
        vec = mat @ v.co
        v.co = vec


# Registration

addon_keymaps = []

def register():
    bpy.utils.register_class(CopyLocalAxesOrientation)
    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new(CopyLocalAxesOrientation.bl_idname, 'C', 'PRESS', ctrl=True, alt=True)
        addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(CopyLocalAxesOrientation)
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

if __name__ == "__main__":
    register()
