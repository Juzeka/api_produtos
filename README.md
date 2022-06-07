# API de Receitas
Api simples de receitas de pratos com suas etapas e ingredientes.
### Models
- Etapa
- Ingrediente
- Receita
### Serializers
#### Etapa
- EtapaAllSerializer
#### Ingrediente
- IngredientesAllSerializers
#### Receitas
- ReceitaAllSerializer
- ReceitaCreateUpdateSerializer
### UML
![Relacionamento](https://github.com/Juzeka/api_receitas/blob/master/relacionamento.png?raw=true)
## Stacks
**Back-end:** Pyhton, Django, Django Rest Framework
## Instalação
```bash
git clone https://github.com/Juzeka/api_receitas.git
python3 -m venv venv
. venv/bin/activate
pip install requirements.txt
python3 manage.py runserver
```