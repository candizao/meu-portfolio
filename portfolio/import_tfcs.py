import json
import os
import django

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TFC, Tecnologia, Licenciatura

# Caminho para o ficheiro JSON
json_path = os.path.join(os.path.dirname(__file__), '../data/tfcs.json')

# Pega a licenciatura (assume que já existe no admin)
licenciatura = Licenciatura.objects.get(nome="Informatica de Gestao")

# Lê os TFCs do JSON
with open(json_path, 'r', encoding='utf-8') as f:
    tfcs_data = json.load(f)

for tfc_data in tfcs_data:
    # Remove a lista de tecnologias do dict antes de criar o TFC
    tecnologias = tfc_data.pop("tecnologias", [])

    # Cria ou obtém o TFC
    tfc, created = TFC.objects.get_or_create(
        titulo=tfc_data["titulo"],
        defaults={
            "descricao": tfc_data["descricao"],
            "ano": tfc_data["ano"],
            "licenciatura": licenciatura
        }
    )

    # Associa tecnologias
    for tech_name in tecnologias:
        tech, _ = Tecnologia.objects.get_or_create(nome=tech_name)
        tfc.tecnologias.add(tech)

    tfc.save()

print("TFCs importados com sucesso!")