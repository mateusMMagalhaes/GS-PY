# Análise de Currículo

Este projeto é uma aplicação em Python para análise de currículos, permitindo adicionar informações pessoais, habilidades (hard e soft skills) e sugerir empregos ideais com base nas competências informadas.

## Funcionalidades
- Adicionar currículo: Nome, idade e curso.
- Adicionar habilidades:
  - Hard Skills (ex.: Modelagem de Machine Learning, Arquitetura em Cloud).
  - Soft Skills (ex.: Pensamento analítico, Comunicação de insights).
- Mostrar currículo: Exibe todas as informações adicionadas.
- Analisar vagas: Sugere empregos ideais com base nas skills informadas.

## Estrutura do Projeto
```
├── app.py              # Arquivo principal com menu e fluxo da aplicação
├── curriculo.py        # Classe Curriculo e métodos para manipulação
├── skill_empregos.py   # Listas de hard skills, soft skills e empregos
```

## Como funciona?

### 1. Classe `Curriculo` (curriculo.py)
- **Atributos**:
  - nome, curso, idade
  - HardSkills, SoftSkills, empregoIdeal
- **Métodos principais**:
  - adicionar_hard_skill(skill)
  - adicionar_soft_skill(skill)
  - mostrar_curriculo()
  - calcular_empregoideal()

### 2. Listas de referência (skill_empregos.py)
- **Hard Skills**:
  Modelagem de Machine Learning, Estatística avançada, Arquitetura em AWS/Azure/GCP, etc.
- **Soft Skills**:
  Pensamento analítico, Comunicação de insights, Criatividade, etc.
- **Empregos**:
  Engenheiro de IA, Cientista de Dados, Analista de Cibersegurança, etc.

### 3. Menu principal (app.py)
- [1] Adicionar currículo
- [2] Adicionar skills
- [3] Mostrar currículo
- [4] Análise de Vagas
- [0] Sair

## Como executar?

1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```
2. Execute o programa:
```bash
python app.py
```

## Exemplo de uso
```
Analise de Curriculo
[1] Adicionar curriculo
[2] Adicionar skills
[3] Mostrar curriculo
[4] Analise de Vagas
[0] Sair
```

## Melhorias futuras
- Persistência de dados (salvar currículos em arquivo ou banco).
- Interface gráfica ou versão web.
- Algoritmo mais avançado para análise de compatibilidade.
