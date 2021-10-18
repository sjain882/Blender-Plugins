# Copy local axes orientation between meshes. The source mesh should be the active object. Keybind in 3D View > Object Mode
# Originally a script by capt_x, converted to plugin that can be bound to a key and present in the space menu by sjain.
# Keybind in 3D View > Object Mode
# Can also be accessed as "Copy local axes orientation" in the Spacebar action menu.
# Original script source can be found at:
# https://www.fsdeveloper.com/forum/threads/blender-2-6x-axis-orientation-copy.427932/page-2#post-654236
# http://web.archive.org/web/20210906195343/https://www.fsdeveloper.com/forum/threads/blender-2-6x-axis-orientation-copy.427932/page-2#post-654236
# http://web.archive.org/web/20210906195438/https://www.fsdeveloper.com/forum/attachments/axis_orientation_copy-txt.16240/
# https://archive.today/hsSgn
# https://archive.today/UENOK

bl_info = {
    "name": "Copy local axes orientation between meshes",
    "author": "capt_x, sjain",
    "version": (1, 0, 0),
    "blender": (2, 60, 0),
    "location": "Spacebar menu",
    "description": "Copy local axes orientation between meshes. The source mesh should be the active object. Keybind in 3D View > Object Mode",
    "warning": "",
    "wiki_url": "https://www.fsdeveloper.com/forum/threads/blender-2-6x-axis-orientation-copy.427932/page-2#post-654236",
    "tracker_url": "",
    "category": "Object"}


import bpy
import mathutils

class CopyLocalAxesOrientation(bpy.types.Operator):

    bl_idname = "object.copy_local_axes"
    bl_label = "Copy local axes orientation"
    bl_context = "objectmode"
    bl_category = "objectmode"

    def execute(self, context):

        source = bpy.context.active_object
        objects = bpy.context.selected_objects
        mat_source = source.rotation_euler.to_matrix()
        mat_source.invert()

        for ob in objects:
            if ob != source:
                mat_ob = ob.rotation_euler.to_matrix()
                if ob.type == 'MESH':
                    mat = mat_source * mat_ob
                    Rotate(ob.data, mat)
                    ob.rotation_euler = source.rotation_euler

        return {'FINISHED'}


def Rotate(myMesh, mat):
    for v in myMesh.vertices:
        vec = mat * v.co
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
