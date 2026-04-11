import json
import os
import django

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import UnidadeCurricular, Licenciatura

# Caminho para o JSON
json_path = os.path.join(os.path.dirname(__file__), '../data/ucs.json')

# Obtém a licenciatura (assume que já existe no admin)
lic = Licenciatura.objects.get(nome="Informatica de Gestao")

# Lê os dados do JSON
with open(json_path, 'r', encoding='utf-8') as f:
    ucs = json.load(f)

for uc_data in ucs:
    uc, created = UnidadeCurricular.objects.get_or_create(
        codigo=uc_data["codigo"],
        defaults={
            "nome": uc_data["nome"],
            "ano": uc_data["ano"],
            "semestre": uc_data["semestre"],
            "docente": uc_data["docente"],
            "imagem": uc_data.get("imagem", ""),
            "licenciatura": lic
        }
    )
    uc.save()

print("UCs importadas com sucesso!")