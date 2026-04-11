import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Tecnologia

json_path = os.path.join(os.path.dirname(__file__), '../data/tecnologias.json')

with open(json_path, 'r', encoding='utf-8') as f:
    tecnologias = json.load(f)

for tech_data in tecnologias:
    tech, created = Tecnologia.objects.get_or_create(
        nome=tech_data["nome"],
        defaults={
            "logo": tech_data.get("logo", ""),
            "website": tech_data.get("website", ""),
            "nivel_interesse": tech_data.get("nivel_interesse", "")
        }
    )
    tech.save()

print("Tecnologias importadas com sucesso!")