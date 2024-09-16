import qrcode
import qrcode.image.svg
import os

while True:
    directTo = input("Eingabe: ")

    factory = qrcode.image.svg.SvgPathImage
    svg_image = qrcode.make(str(directTo), image_factory=factory)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    svg_file_path = os.path.join(current_dir, "qrcode.svg")
    svg_image.save(svg_file_path)

    print(f"QR-Code image copied to {svg_file_path}")