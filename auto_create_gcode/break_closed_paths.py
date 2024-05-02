from svgpathtools import svg2paths, Path, Line, disvg
from copy import deepcopy

def break_closed_paths(svg_file, output_file):
    # Load SVG paths from file
    paths, attributes = svg2paths(svg_file)

    # Create a list to store modified paths
    modified_paths = []

    # Iterate over each path
    for path in paths:
        # If the path is closed, break it into separate line segments
        if isinstance(path, Path) and path.isclosed():
            # Get the points of the closed path
            points = path.poly().points()

            # Create line segments between consecutive points
            for i in range(len(points)):
                start_point = points[i]
                end_point = points[(i + 1) % len(points)]  # Wrap around to the first point

                # Create a Line segment from the start to end point
                line_segment = Line(start_point, end_point)

                # Append the line segment to modified paths
                modified_paths.append(line_segment)
        else:
            # If the path is not closed, add it as it is
            modified_paths.append(deepcopy(path))

    # Save the modified paths to a new SVG file
    disvg(modified_paths, attributes=attributes, filename=output_file)

# Path to the input SVG file
svg_file = "../examples/test/boxes.svg"

# Path to save the modified SVG file
output_file = "../examples/test/boxes_no_closed_path.gcode"

# Break closed paths in the SVG file
break_closed_paths(svg_file, output_file)
