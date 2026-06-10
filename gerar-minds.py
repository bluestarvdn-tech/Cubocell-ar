"""
CuboCell AR — Gerador de arquivos .mind
Execute ANTES do servidor para compilar os marcadores.

Requer: pip install mind-ar  (se disponível)
Alternativa: use a ferramenta online no link abaixo.
"""

import subprocess, sys, os

def instalar_pacote(pacote):
    subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

print("="*55)
print("  Gerador de marcadores .mind")
print("="*55)

# Tenta usar a ferramenta online via instruções claras
print("""
Como gerar os arquivos .mind (OBRIGATÓRIO antes de testar):

MÉTODO MAIS FÁCIL — Online (sem instalar nada):

1. Acesse no navegador:
   https://hiukim.github.io/mind-ar-js-doc/tools/compile

2. Clique em "Upload Images"

3. Selecione as 3 imagens da pasta markers/:
   - face1-animal.png
   - face2-vegetal.png  
   - face3-procarionte.png

4. Clique em "Start" e aguarde processar

5. Clique em "Export" para baixar os arquivos .mind

6. Renomeie os arquivos baixados para:
   - targets.mind  →  markers/face1-animal.mind
   (repita para cada imagem individualmente)

ATENÇÃO: Faça uma imagem por vez para gerar .mind separados!

Após gerar os 3 arquivos .mind e colocá-los na pasta markers/,
execute: python servidor-local.py
""")
