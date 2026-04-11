import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import TFC, Tecnologia

# Caminho para o JSON
json_path = os.path.join(os.path.dirname(__file__), '../data/tfcs.json')

with open(json_path, 'r', encoding='utf-8') as f:
    tfcs = json.load(f)

for tfc_data in tfcs:
    tecnologias = tfc_data.pop("tecnologias", [])
    tfc, created = TFC.objects.get_or_create(**tfc_data)

    for tech_name in tecnologias:
        tech, _ = Tecnologia.objects.get_or_create(nome=tech_name)
        tfc.tecnologias.add(tech)
    
    tfc.save()

print("TFCs importados com sucesso!")