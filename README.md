# Blender-Plugins

Assorted Blender plugins for different versions.

***

### `local_axes_orientation_copy_updated.py`:

**Copy local axes orientation between objects - Blender 2.79**

This feature used to ship with Blender 2.5x and below, but was removed in 2.6. I found a [forum post](https://www.fsdeveloper.com/forum/threads/blender-2-6x-axis-orientation-copy.427932/page-2#post-654236) with it restored to 2.6 as a script. I've turned it into a plugin and added a keyboard shortcut for it (CTRL + ALT + C by default). It is undoable as well.

This can be a timesaver when animating things in OMSI 2, e.g., you can simply create a single edge/vert/empty and rotate the axes to the desired orientation, then copy that orientation to every needle on a dashboard binnacle. This saves having to rotate in object mode and un-rotate in edit mode over and over again.

I'm aware you can sort of do similar by merging the objects with CTRL + J, but that can be destructive for object names (and modifiers I've read, but not tested). Plus this is quicker.

To use it, select the objects you would like to copy the local axes to, then select the source object last, so it is the active object. Then either access Copy local axes orientation from the space action menu or use the keyboard shortcut.

***

### `local_axes_orientation_copy_updated_28x.py`:

**Copy local axes orientation between objects - Blender 2.80+**

Same as above, but for Blender 2.80 and above - tested on Blender 2.93.7 LTS.

The entire code was just copy pasted into the same plugin format as above for some friends who wanted it out of the box - it is NOT my work!

[Original code source](https://blender.stackexchange.com/questions/230321/rotate-origin-only-to-match-other-object-rotation/230574#230574) - credit: batFINGER

***

### `io_import_multiple_objs_filename.py`

**Import multiple Wavefront (.obj) meshes in batch - Blender 2.79**

Original script by poor. Modified by [BlueOrange](https://github.com/BlueOrange775) to retain filenames (as object names) and by me to shade all mesh UV's smooth after import.
