import json, os, django

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from portfolio.models import Projeto, UnidadeCurricular, Tecnologia

# Caminho para o JSON
json_path = os.path.join(os.path.dirname(__file__), '../data/projetos.json')

# Lê os dados do JSON
with open(json_path, 'r', encoding='utf-8') as f:
    projetos = json.load(f)

# Itera e importa
for proj_data in projetos:
    # Obtém a UC correspondente
    uc = UnidadeCurricular.objects.get(codigo=proj_data["unidade_curricular_codigo"])
    tecnologias = proj_data.pop("tecnologias", [])

    # Cria o projeto
    projeto, created = Projeto.objects.get_or_create(
        titulo=proj_data["titulo"],
        defaults={
            "descricao": proj_data["descricao"],
            "unidade_curricular": uc,
            "imagem": proj_data.get("imagem", ""),
            "video_demo": proj_data.get("video_demo", "")
        }
    )

    # Associa tecnologias
    for tech_name in tecnologias:
        tech, _ = Tecnologia.objects.get_or_create(nome=tech_name)
        projeto.tecnologias.add(tech)

    projeto.save()

print("Projetos importados com sucesso!")