import json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Formacao

json_path = os.path.join(os.path.dirname(__file__), '../data/formacoes.json')

with open(json_path, 'r', encoding='utf-8') as f:
    formacoes = json.load(f)

for form_data in formacoes:
    form, created = Formacao.objects.get_or_create(
        nome=form_data["nome"],
        defaults={
            "descricao": form_data["descricao"],
            "ano": form_data["ano"],
            "instituicao": form_data.get("instituicao", "")
        }
    )
    form.save()

print("Formações importadas com sucesso!")