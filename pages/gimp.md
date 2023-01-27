---
layout: default
title: GIMP
lastbgclr: red-50
current: 1
---

# GIMP

Postaviti velicinu dokumenta na 400x400mm `File > Document properties`

Iz menija `Path > Trace bitmap` kreirati vektorski format, tj od sada radimo samo sa putanjama.
Uz pomoc obicnih kvadrata, radimo `Path > Union` ili difference **CTRL +**

Na kraju iz `Extensions > Gcodetools > Orientation points...` i `Apply`
Pa dodamo `Extensions > Gcodetools > Tools library...` izaberemo `Cylindar`
i na kraju `Extensions > Gcodetools > Path to Gcode`.


Switch to edge version of inkspace
```
sudo snap refresh --edge inkscape
sudo snap refresh --stable inkscape
```

Extension source https://github.com/cnc-club/gcodetools
Report for inkspace https://gitlab.com/inkscape/inbox/-/issues/new
