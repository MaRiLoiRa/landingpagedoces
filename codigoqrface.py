import pyqrcode

# URL do seu perfil do Facebook
perfil_facebook_url = "https://www.facebook.com/neusadocescaseiros"

# Gerar o QR code
qr_code_facebook = pyqrcode.create(perfil_facebook_url)

# Salvar o QR code como uma imagem PNG
qr_code_facebook.png("facebook_qr_code.png", scale=8)

print("QR code do Facebook gerado com sucesso!")



