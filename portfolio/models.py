from django.db import models


# 1. Licenciatura
class Licenciatura(models.Model):
    nome = models.CharField(max_length=100, default="Informatica de Gestao")
    ano_inicio = models.IntegerField(default=2024)
    ano_previsto_fim = models.IntegerField(default=2027)
    instituicao = models.CharField(max_length=100, default="Universidade Lusófona")
    descricao = models.TextField(max_length=2000, blank=True, default="")

    def __str__(self):
        return self.nome


# 2. Unidade Curricular
class UnidadeCurricular(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    imagem = models.ImageField(upload_to='media/uc_images/', null=True, blank=True)
    docente = models.CharField(max_length=100)
    pagina_docente = models.URLField(null=True, blank=True)
    licenciatura = models.ForeignKey('Licenciatura', on_delete=models.CASCADE, related_name='ucs')

    def __str__(self):
        return f"{self.codigo} - {self.nome}"


# 3. Tipo de Tecnologia
class TipoTecnologia(models.Model):
    TIPOS = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('base_dados', 'Base de Dados'),
        ('storage', 'Storage'),
        ('outros', 'Outros'),
    ]
    nome = models.CharField(max_length=50, choices=TIPOS, unique=True)

    def __str__(self):
        return self.get_nome_display()


# 4. Tecnologia
class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media/tecnologias/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    nivel_interesse = models.IntegerField(default=0)
    descricao = models.TextField(null=True, blank=True)
    tipo = models.ForeignKey('TipoTecnologia', on_delete=models.SET_NULL, null=True, blank=True, related_name='tecnologias')

    def __str__(self):
        return self.nome


# 5. Projeto
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    conceitos = models.TextField()
    tecnologias = models.ManyToManyField('Tecnologia', blank=True)
    unidade_curricular = models.ForeignKey('UnidadeCurricular', on_delete=models.CASCADE, related_name='projetos')
    imagem = models.ImageField(upload_to='media/projeto_images/', null=True, blank=True)
    video_demo = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.titulo


# 6. TFC
class TFC(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    tecnologias = models.ManyToManyField('Tecnologia', blank=True)
    licenciatura = models.ForeignKey('Licenciatura', on_delete=models.CASCADE, related_name='tfcs')
    interesse = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


# 7. Competência
class Competencia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    projetos = models.ManyToManyField('Projeto', blank=True)
    tecnologias = models.ManyToManyField('Tecnologia', blank=True)
    formacoes = models.ManyToManyField('Formacao', blank=True)

    def __str__(self):
        return self.nome


# 8. Formação
class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


# 9. MakingOf
class MakingOf(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    fotos = models.ImageField(upload_to='media/makingof/', null=True, blank=True)
    erros = models.TextField(null=True, blank=True)
    decisoes = models.TextField(null=True, blank=True)
    entidade_relacionada = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.titulo