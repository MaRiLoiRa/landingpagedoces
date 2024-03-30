import barcode
from barcode.writer import ImageWriter
from PIL import Image

def generate_barcode(product_name, barcode_value, filename):
    # Gerar o código de barras
    code128 = barcode.get_barcode_class('code128')
    barcode_instance = code128(barcode_value, writer=ImageWriter())
    barcode_filename = barcode_value + "_" + product_name.replace(" ", "_")
    barcode_instance.save(barcode_filename)

    # Abrir a imagem gerada
    img = Image.open(barcode_filename + '.png')

    # Mostrar o código de barras
    img.show()

if __name__ == "__main__":
    product_name = "Cocada Caseira"
    barcode_value = "0742832650014"  # Aqui você pode inserir o código específico do seu produto
    filename = "cocada_barcode"
    generate_barcode(product_name, barcode_value, filename)
