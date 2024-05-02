import subprocess
from svg2gcode import SvgParser, write_gcode

def generate_gcode_from_svg(svg_file, gcode_file):
    # Parse SVG file
    parser = SvgParser()
    parser.parse(svg_file)

    # Generate G-code
    gcode = write_gcode(parser)
    
    # Save G-code to a file
    with open(gcode_file, 'w') as f:
        f.write(gcode)

def send_gcode_with_ugs(gcode_file):
    # Path to Universal Gcode Sender (change it to your UGS installation path)
    ugs_path = 'path/to/UniversalGcodeSender.jar'

    # Launch UGS and send G-code
    command = ['java', '-jar', ugs_path, '-n', '-f', gcode_file]
    subprocess.run(command)

# Path to your SVG file
svg_file = "../examples/test/boxes.svg"

# Path to save the generated G-code
gcode_file = "../examples/test/boxes.gcode"

# Generate G-code from SVG
generate_gcode_from_svg(svg_file, gcode_file)

# Send G-code using Universal Gcode Sender
send_gcode_with_ugs(gcode_file)
