# 🧫 CuboCell AR — Realidade Aumentada no Navegador

Projeto educacional com células 3D projetadas sobre cubo físico.
Sem instalação de app — funciona direto no navegador do celular.

## 📁 Estrutura

```
cubocell-ar/
├── celula-animal.html      ← Site AR célula animal
├── celula-vegetal.html     ← Site AR célula vegetal
├── procarionte.html        ← Site AR procarionte
├── cubo-impressao.html     ← Guia + molde para imprimir
├── models/
│   ├── celula-animal.glb   ← Modelo 3D célula animal
│   └── celula-vegetal.glb  ← Modelo 3D célula vegetal
├── markers/
│   ├── face1-animal.png    ← Imagem marcadora (célula animal)
│   ├── face2-vegetal.png   ← Imagem marcadora (célula vegetal)
│   ├── face3-procarionte.png ← Imagem marcadora (procarionte)
│   ├── face1-animal.mind   ← Marcador compilado (gerado pelo script)
│   ├── face2-vegetal.mind  ← Marcador compilado
│   └── face3-procarionte.mind ← Marcador compilado
└── README.md
```

## ⚠️ PASSO OBRIGATÓRIO — Gerar os arquivos .mind

Os arquivos `.mind` são os marcadores compilados que o MindAR usa.
Você precisa gerá-los UMA VEZ antes de publicar.

### Como gerar (2 opções):

**Opção A — Online (mais fácil):**
1. Acesse: https://hiukim.github.io/mind-ar-js-doc/tools/compile
2. Faça upload das 3 imagens PNG da pasta markers/
3. Clique em "Start" e aguarde
4. Baixe os 3 arquivos .mind gerados
5. Coloque na pasta markers/

**Opção B — Node.js local:**
```bash
npx mind-ar-js compile --input markers/face1-animal.png --output markers/face1-animal.mind
npx mind-ar-js compile --input markers/face2-vegetal.png --output markers/face2-vegetal.mind
npx mind-ar-js compile --input markers/face3-procarionte.png --output markers/face3-procarionte.mind
```

## 🚀 Publicar no GitHub Pages

1. Crie conta em github.com
2. Crie repositório público chamado `cubocell-ar`
3. Faça upload de TODOS os arquivos desta pasta
4. Vá em Settings → Pages → Source: main / root
5. Aguarde 2 minutos

**IMPORTANTE:** O GitHub Pages usa HTTPS automaticamente.
A câmera do celular SÓ funciona com HTTPS — não funciona abrindo o arquivo local!

## 📱 URLs após publicar

```
https://SEU_USUARIO.github.io/cubocell-ar/celula-animal.html
https://SEU_USUARIO.github.io/cubocell-ar/celula-vegetal.html
https://SEU_USUARIO.github.io/cubocell-ar/procarionte.html
```

## 🖨️ Imprimir o cubo

1. Abra cubo-impressao.html no navegador
2. Imprima as imagens de markers/ (face1, face2, face3)
3. Cole cada marcador na face correspondente do cubo
4. Dobre e cole o molde
5. Gere os QR Codes em qr.io com as URLs acima
