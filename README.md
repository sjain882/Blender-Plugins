# Blender-Plugins

Assorted Blender plugins for different versions. For archival purposes only.

***

### `2.79\local_axes_orientation_copy_updated.py`:

**Copy local axes orientation between objects - Blender 2.79**

This feature used to ship with Blender 2.5x and below, but was removed in 2.6. I found a [forum post](https://www.fsdeveloper.com/forum/threads/blender-2-6x-axis-orientation-copy.427932/page-2#post-654236) with it restored to 2.6 as a script. I've turned it into a plugin and added a keyboard shortcut for it (CTRL + ALT + C by default). It is undoable as well.

This can be a timesaver when animating things in OMSI 2, e.g., you can simply create a single edge/vert/empty and rotate the axes to the desired orientation, then copy that orientation to every needle on a dashboard binnacle. This saves having to rotate in object mode and un-rotate in edit mode over and over again.

I'm aware you can sort of do similar by merging the objects with CTRL + J, but that can be destructive for object names (and modifiers I've read, but not tested). Plus this is quicker.

To use it, select the objects you would like to copy the local axes to, then select the source object last, so it is the active object. Then either access "Copy local axes orientation" from the spacebar action menu or use the keyboard shortcut.

***

### `2.80+\local_axes_orientation_copy_updated_28x.py`:

**Copy local axes orientation between objects - Blender 2.80+**

Same as above, but for Blender 2.80 and above - tested on Blender 2.93.7 LTS.

The entire code was just copy pasted into the same plugin format as above for some friends who wanted it out of the box - it is NOT my work!

[Original code source](https://blender.stackexchange.com/questions/230321/rotate-origin-only-to-match-other-object-rotation/230574#230574) - credit: batFINGER

***

### `2.79\io_import_multiple_objs_filename.py`

**Import multiple Wavefront (.obj) meshes in batch - Blender 2.79**

Original script by poor. Modified by [BlueOrange](https://github.com/BlueOrange775) to retain filenames (as object names) and by me to shade all mesh UV's smooth after import.

***

### `2.80+\io_batch_import_objs_2.93_retainsFilename.py`

**Import multiple Wavefront (.obj) meshes in batch - Blender 2.92 - 3.0.1 (only)**

Original script by p2or, I've just ported [BlueOrange](https://github.com/BlueOrange775)'s method to retain filenames (as object names) after import.

[Original code source](https://blender.stackexchange.com/questions/5064/how-to-batch-import-wavefront-obj-files/31825#31825) - credit: p2or. Version for 2.80+ is available there.

***

### `2.80+\refresh_materials_27x_to_28x_above.py`

Created by me - for all selected objects, deletes their materials and adds a new blank Principled BSDF nodes material. Can be needed to fix some material things when copying models from Blender 27x sessions to 28x sessions.

WARNING: Mostly intended for fresh blends where you copy a set of models freshly imported from a 2.7x blend to a 2.8x blend. This purges all orphaned data blocks and can be destructive.

Select the objects you wish to apply this action to then access "Refresh materials" from the spacebar action menu to use it.

***
***
***

# OMSI 2 - Useful Blender Plugins

### `2.79`



**Blender-O3D-IO-Public**

• https://github.com/space928/Blender-O3D-IO-Public

• Imports entire vehicles & sceneryobjects in one go - models, materials & various features like interior lights and exports individual O3D models



**O3D Model Exporter (MichauSto)**

• https://strefa-omsi.pl/Watek-OMSI-1-2-Eksporter-plikow-o3d-blender-2-79-2-80-3-0--27096

• Exports o3d model files with options to specify material texture, specular strength, etc...



**Modify Pivot**

• https://github.com/Anonim17PL/modify_pivot

• Easily adjust local axes / transformation orientation / model animation (feature included in Blender 2.8+)



**Configuration file exporter**

• Download: https://forum.omnibussimulator.de/forum/index.php?thread/29488-blender-addon-omsi-konfigurationsdateien-exporter-v1-2-neu-passengercabinexporte/

• Tutorial: https://www.youtube.com/watch?v=LN1u5uJMy-I

• Dummy models pack: https://cdn.discordapp.com/attachments/491327427314712577/898959187126669402/OMSI_Passengercabin__Paths_Configuration.7z

• Dummy models pack original source: https://discord.com/channels/563856915981926411/764884741144838225/887034889545875497



**DirectX (`*.x`) Model Importer**

• https://github.com/spamandeggs/directX_blender



**DirectX (`*.x`) Model Exporter**

• https://github.com/cdbfoster/io_scene_x



**Misc. plugins**

• https://github.com/sjain882/Blender-Plugins/tree/main/2.79

• 1. Import multiple Wavefront .obj model files and retain their filenames (useful for 3D Object Converter batch o3d -> obj)

• 2. Copy local axes / transformation orientation / model animation between multiple objects easily

• Documentation: https://github.com/sjain882/Blender-Plugins



***



### `2.80+`



**Blender-O3D-IO-Public**

• https://github.com/space928/Blender-O3D-IO-Public

• Imports entire vehicles & sceneryobjects in one go - models, materials & various features like interior lights and exports individual O3D models



**O3D Model Exporter (MichauSto)**

• https://strefa-omsi.pl/Watek-OMSI-1-2-Eksporter-plikow-o3d-blender-2-79-2-80-3-0--27096

• Exports o3d model files with options to specify material texture, specular strength, etc...



**O3D Model Exporter (Road-Hog123)**

• https://github.com/Road-hog123/Blender-OMSI-Exporter

• Exports o3d model files with advanced support for Blender Cycles materials



**Configuration file exporter**

• https://strefa-omsi.pl/Watek-OMSI-2-Automatyczny-generator-pojazdow-i-obiektow-scenerii-blender-2-8--27135

• Automatically generate various fragments of model & sceneryobject configuration files, **including AI paths (partial replacement of OMSI Crossing Editor)**



**DirectX (`*.x`) Model Importer**

• https://github.com/oguna/Blender-XFileImporter

• https://github.com/poikilos/io_import_x (Blender 2.80)



**DirectX (`*.x`) Model Exporter**

• https://github.com/DodgeeSoftware/io_scene_directx (Blender 2.8+)

• https://github.com/Anonim17PL/io_scene_x (Blender 2.83)

• https://github.com/arite/io_scene_x (Blender 2.9+)



**Misc Plugins**

• https://github.com/sjain882/Blender-Plugins/tree/main/2.80%2B

• 1. Import multiple Wavefront .obj model files and retain their filenames (useful for 3D Object Converter batch o3d -> obj)

• 2. Copy local axes / transformation orientation / model animation between multiple objects easily

• 3. Replace all materials on all objects with new blank Principled BSDF materials (for 2.8+ --> 2.79 or GPU dumping)

• Documentation: https://github.com/sjain882/Blender-Plugins



***



### **Decrypt base game OMSI models for importing**

*only applies to base game content e.g, MAN SD202 - not DLC buses*

• https://github.com/CrIcKeT98/OMSI_Decoder



***



### **Convert Blender 2.79 blend file to Blender 2.8+**



• <https://gist.github.com/nebadon2025/8266e6dd8cec22d098011231eff15461>

1. Download this file to `C:\Program Files\Blender Foundation\Blender\2.79\scripts\addons`

2. Enable plugin in preferences

3. Backup blend file, then open blend in 2.79

4. Select any object > Go to materials tab on the right > Scroll to bottom > Click on `BLENDER &gt; CYCLES`

5. It will convert all the materials in the blend (not just this one), be patient if its slow

6. Switch render to `Blender Cycles` from `Blender Render` at the top

7. Save blend

8. Open blend in Blender 2.8+
