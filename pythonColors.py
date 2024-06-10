#\033[style;text;backm
while True:
    try:
        hora = int(input("\033[1;35mDIGITE AS HORAS (SEM OS MINUTOS): "))
        minute = int(input("Digite os minutos: "))
        if hora >= 16 and hora <= 23:
            print("\033[1;31m{:.0f}:{:.0f} É HORA DO FUTEBOL\033[m".format(hora, minute))
            break 
        else:
            print("\033[1;34mINFELIZMENTE {:.0f}:{:.0f} NÃO É HORA DO FUTEBOL ;-;\033[m".format(hora, minute))
            break 
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")
        


       



        

 




