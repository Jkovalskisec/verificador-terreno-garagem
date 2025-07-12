

        # Projeto verificador de terreno para garagem!
        # Autor: Jean Kovalski
        # Objetivo: Verificar se um terreno comporta uma garagem de 20m² sem ultrapassar 20% da área total

def verificar_terreno(largura, comprimento):
    area_terreno = largura * comprimento
    limite_garagem = area_terreno * 0.20
    garagem_necessaria = 20

    print(f"\nÁrea do terreno: {area_terreno: .2f} m²")
    print(f"20% da área do terreno: {limite_garagem: .2f} m²")
    print(f"Garagem necessária: {garagem_necessaria} m²")

    if garagem_necessaria <= limite_garagem:
        print("✅ Terreno compatível com os requisitos da garagem.")
    else:
        print("❌ Terreno incompatível com os requisitos da garagem.")



#Entrada do usuário
try:
    largura = float(input("Digite a largura do terreno (em metros)"))
    comprimento = float(input("Digite o comprimento do terreno (em metros): "))

    verificar_terreno(largura, comprimento)

except ValueError:
    print("Por favor, digite apenas números válidos.")