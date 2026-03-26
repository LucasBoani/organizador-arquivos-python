import os
import shutil

# 1. Defina o caminho da pasta que você quer organizar
# DICA: '.' significa a pasta onde o script está agora
caminho = "." 

# 2. Lista de extensões e para onde elas devem ir
formatos = {
    "PDFs": [".pdf", ".txt"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Planilhas": [".xlsx", ".csv"],
    "Scripts": [".py", ".js"]
}

def organizar():
    for arquivo in os.listdir(caminho):
        nome, extensao = os.path.splitext(arquivo)
        
        for pasta, extensoes in formatos.items():
            if extensao.lower() in extensoes:
                # Cria a pasta se ela não existir
                if not os.path.exists(os.path.join(caminho, pasta)):
                    os.mkdir(os.path.join(caminho, pasta))
                
                # Move o arquivo
                old_path = os.path.join(caminho, arquivo)
                new_path = os.path.join(caminho, pasta, arquivo)
                shutil.move(old_path, new_path)
                print(f"✅ Movido: {arquivo} -> {pasta}")

if __name__ == "__main__":
    print("🚀 Iniciando organização...")
    organizar()
    print("✨ Pasta organizada com sucesso!")