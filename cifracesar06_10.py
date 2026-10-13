from pygame import *

def valida_email(email):
    return email[-8:] == "@puc.com"

def possui_maiuscula(senha):
    for carac in senha:
        if 'A' <= carac <= 'Z':
            return True
    return False

def possui_minuscula(senha):
    for carac in senha:
        if 'a' <= carac <= 'z':
            return True
    return False

def possui_numero(senha):
    for carac in senha:
        if carac.isnumeric():
            return True
    return False

def valida_senha(senha):
    if len(senha) < 8:
        return False
    if not possui_maiuscula(senha):
        return False
    if not possui_minuscula(senha):
        return False
    if not possui_numero(senha):
        return False
    return True

def criptografa(senha):
    senha_cripto = ""
    for carac in senha:
        if '0' <= carac <= 'z':
            pos_base = ord(carac) - ord('0')
            pos_nova = (pos_base + 3) % 75
            pos_ascii = pos_nova + ord('0')
            senha_cripto += chr(pos_ascii)
        else:
            senha_cripto += carac
    return senha_cripto

init()
screen = display.set_mode((800, 600))
running = True
clock = time.Clock()

# para a tela de login
fonte_login = font.Font(None, 36)
fonte_erro = font.Font(None, 24)

# 1 = E-mail, 2 = Senha, 3 = Casinha
estado_login = 1
input_email = ""
input_senha = ""
mensagem_erro = ""
senha_criptografada_resultado = ""

caminho_fonte = r"D:\DOWNLOADS_DATA\casinha_batman\batmfa__.ttf"
fonte_customizada = font.Font(caminho_fonte, 48)

texto_surface = fonte_customizada.render("FAZ NEYMAR", True, (0, 47, 108))

mixer.music.load(r"D:\DOWNLOADS_DATA\casinha_batman\batman_1966.mp3")

nuvem_x = 430
nuvem_vel = 100
nuvem2_x = 200
nuvem2_vel = -150
sol_x = 100
sol_y = 100

caminho_neymar = r"D:\DOWNLOADS_DATA\neymar.png"
imagem_ney = image.load(caminho_neymar)
imagem_ney = transform.scale(imagem_ney, (110, 160))
imagem_ney.set_colorkey("#FFFFFF")

musica_tocando = False

while running == True:
    dt = clock.get_time() / 1000
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        
        # Tela login
        if estado_login == 1 or estado_login == 2:
            if ev.type == KEYDOWN:
                if ev.key == K_BACKSPACE:
                    if estado_login == 1:
                        input_email = input_email[:-1]
                    else:
                        input_senha = input_senha[:-1]
                elif ev.key == K_RETURN:
                    if estado_login == 1:
                        if valida_email(input_email):
                            estado_login = 2
                            mensagem_erro = ""
                        else:
                            mensagem_erro = "E-mail inválido! Deve terminar com '@puc.com'."
                    elif estado_login == 2:
                        if valida_senha(input_senha):
                            senha_criptografada_resultado = criptografa(input_senha)
                            estado_login = 3 #casinha
                            mensagem_erro = ""
                            mixer.music.play(-1)
                            musica_tocando = True
                        else:
                            mensagem_erro = "Senha fraca! Mín. 8 caracteres, 1 maiúscula, 1 minúscula e 1 número."
                else:
                    if ev.unicode:
                        if estado_login == 1:
                            input_email += ev.unicode
                        elif estado_login == 2:
                            input_senha += ev.unicode

        # Eventos Casinha Liberados após o login
        elif estado_login == 3:
            if ev.type == MOUSEMOTION:
                sol_x, sol_y = ev.pos

    if estado_login == 1:
        screen.fill((240, 240, 240))
        titulo = fonte_login.render("Digite seu e-mail (@puc.com):", True, (0, 0, 0))
        screen.blit(titulo, (100, 150))
        draw.rect(screen, (255, 255, 255), (100, 200, 600, 50))
        draw.rect(screen, (0, 0, 0), (100, 200, 600, 50), 2)
        txt_render = fonte_login.render(input_email, True, (0, 0, 0))
        screen.blit(txt_render, (110, 210))
        if mensagem_erro:
            erro_render = fonte_erro.render(mensagem_erro, True, (200, 0, 0))
            screen.blit(erro_render, (100, 260))

    elif estado_login == 2:
        screen.fill((240, 240, 240))
        titulo = fonte_login.render("Digite sua senha segura:", True, (0, 0, 0))
        screen.blit(titulo, (100, 150))
        draw.rect(screen, (255, 255, 255), (100, 200, 600, 50))
        draw.rect(screen, (0, 0, 0), (100, 200, 600, 50), 2)
        txt_render = fonte_login.render("*" * len(input_senha), True, (0, 0, 0))
        screen.blit(txt_render, (110, 210))
        if mensagem_erro:
            erro_render = fonte_erro.render(mensagem_erro, True, (200, 0, 0))
            screen.blit(erro_render, (100, 260))

    elif estado_login == 3:
        # CONTROL C + V DA CASITA ULTIMARE
        keys = key.get_pressed()
        mouse_x, mouse_y = mouse.get_pos()

        if keys[K_RIGHT]:
            sol_x = sol_x + 200 * dt

        elif keys[K_LEFT]:
            sol_x = sol_x - 200 * dt

        if keys[K_DOWN]:
            sol_y = sol_y + 200 * dt

        elif keys[K_UP]:
            sol_y = sol_y - 200 * dt

        if sol_x < 100:
            sol_x = 100

        elif sol_x > 700:
            sol_x = 700

        if sol_y < 100:
            sol_y = 100

        elif sol_y > 500:
            sol_y = 500

        nuvem_x = nuvem_x + nuvem_vel * dt
        nuvem2_x = nuvem2_x + nuvem2_vel * dt

        if nuvem_x > 605:
            nuvem_x = 605
            nuvem_vel = -nuvem_vel

        elif nuvem_x < 45:
            nuvem_x = 45
            nuvem_vel = -nuvem_vel

        if nuvem2_x > 665:
            nuvem2_x = 665
            nuvem2_vel = -nuvem2_vel

        elif nuvem2_x < 30:
            nuvem2_x = 30
            nuvem2_vel = -nuvem2_vel

        if sol_x <= 400:
            progresso = (sol_x - 100) / 300
            fundo_r = int(151 + (245 - 151) * progresso)
            fundo_g = int(209 + (178 - 209) * progresso)
            fundo_b = int(250 + (64 - 250) * progresso)
        else:
            progresso = (sol_x - 400) / 300
            fundo_r = int(245 + (10 - 245) * progresso)
            fundo_g = int(178 + (20 - 178) * progresso)
            fundo_b = int(64 + (60 - 64) * progresso)

        screen.fill((fundo_r, fundo_g, fundo_b))

        draw.line(screen, "#FFF251", (sol_x - 80, sol_y - 80), (sol_x + 80, sol_y + 80), 8)
        draw.line(screen,"#FFF251", (sol_x - 80, sol_y + 80), (sol_x + 80, sol_y - 80), 8)
        draw.line(screen,"#FFF251", (sol_x, sol_y - 95), (sol_x, sol_y + 95), 8)
        draw.line(screen,"#FFF251", (sol_x - 95, sol_y), (sol_x + 95, sol_y), 8)
        draw.circle(screen, "#FFF251",(int(sol_x), int(sol_y)), 50)

        draw.rect(screen, "#489D25", (0,500,800,100))
        draw.rect(screen, "#646464", (100, 300, 200, 200))
        draw.rect(screen, "#0D1764", (120, 380, 50, 70))
        draw.rect(screen, "#784D1A", (200, 360, 70, 140))
        draw.circle(screen,"#000000",(215,430),7)
        draw.polygon(screen, "#F2883B",((100,300),(200,200),(300,300)))
        draw.rect(screen, "#784D1A", (510, 355, 50, 145))
        draw.circle(screen,"#479C25",(535,320),80)
    
        if imagem_ney:
            screen.blit(imagem_ney, (365, 350))
        draw.circle(screen, "#FFFFFF", (int(nuvem_x), 100), 45)
        draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 50, 100), 45)
        draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 100, 100), 45)
        draw.circle(screen, "#FFFFFF", (int(nuvem_x) + 150, 100), 45)
        draw.circle(screen, "#FFFFFF", (int(nuvem2_x), 170), 30)
        draw.circle(screen, "#FFFFFF", (int(nuvem2_x) + 35, 170), 30)
        draw.circle(screen, "#FFFFFF", (int(nuvem2_x) + 70, 170), 30)
        draw.circle(screen, "#FFFFFF", (int(nuvem2_x) + 105, 170), 30)
        screen.blit(texto_surface, (250, 500))

    display.update()
