import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont


def criar_imagem_arredondada_com_texto(text, font_size, radius, color, border_color, border_width):
    # Carregar a fonte padrão do sistema
    font = ImageFont.truetype("arial.ttf", font_size)

    # Calcular o tamanho da imagem baseada no texto usando textbbox
    temp_img = Image.new('RGBA', (1, 1))
    draw_temp = ImageDraw.Draw(temp_img)
    text_bbox = draw_temp.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    width = text_width + 20  # Adiciona um pouco de padding
    height = text_height + 10

    # Criar uma nova imagem com fundo transparente
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Desenhar o retângulo arredondado
    draw.rounded_rectangle(
        (border_width, border_width, width - border_width, height - border_width),
        radius,
        fill=color,
        outline=border_color,
        width=border_width
    )

    # Adicionar o texto no centro da imagem
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), text, fill='black', font=font)

    return img


# Especificações CSS convertidas para Pillow
text = "Clique Aqui"
font_size = 22
border_width = 1
color = 'white'  # Cor de fundo do botão
border_color = 'black'  # Cor da borda do botão
border_radius = 1000  # Raio grande para borda totalmente arredondada

# Criar a imagem com Pillow
imagem_arredondada = criar_imagem_arredondada_com_texto(text, font_size, border_radius, color, border_color,
                                                        border_width)
imagem_arredondada.save("borda_arredondada.png")

# Configurar a imagem para CustomTkinter
imagem_ctk = ctk.CTkImage(light_image=imagem_arredondada, size=(imagem_arredondada.width, imagem_arredondada.height))

# Criação da Janela Principal
janela = ctk.CTk()
janela.title('CustomTkinter Exemplo')
janela.geometry("400x300")

# Adicionar um botão com a imagem arredondada como fundo
botao = ctk.CTkButton(janela, image=imagem_ctk, text="", command=lambda: print("Botão clicado"))
botao.pack(pady=50)

# Iniciar o Loop Principal
janela.mainloop()
