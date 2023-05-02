---
layout: default
---

# Inkscape

Postaviti velicinu dokumenta na 400x400mm i scale 1,00 *mm per user unit* unutar
menija `File > Document properties`.

Iz menija `Path > Trace bitmap` kreirati vektorski format, tj od sada radimo
samo sa putanjama.
Uz pomoc obicnih kvadrata, radimo `Path > Union` ili difference **CTRL -**

Kada smo gotovi onda iz menija `Extensions > Gcodetools > Path to Gcode`. To ce
automatski dodati `Extensions > Gcodetools > Orientation points...` i
`Extensions > Gcodetools > Tools library...` izabran `Cylindar`.
Napravice se fajl `output_0001.ngc`.

Ako je slike previse tanka, mozete je podebljati tako sto dodate Stroke i
pretvorite stroke u putanju i uradite union
https://www.youtube.com/watch?v=3Ye0ZGAhYlI

# Druge mogucnosti za kreiranje gcode

Ovde je source koji se koristi u Gcodetools ekstenziji za Inkscape
https://github.com/cnc-club/gcodetools

Ovde mozemo naci druge alate koji automatski generisu gcode
https://github.com/SebKuzminsky/svg2gcode
