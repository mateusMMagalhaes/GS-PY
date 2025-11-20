from skill_empregos import hardkills_list,softskills_list,empregos_list
class Curriculo:
    def __init__(self, nome, curso, idade):
        self.nome = nome
        self.curso = curso
        self.idade = idade
        self.HardSkills = []
        self.SoftSkills = []
        self.empregoIdeal = []

    def adicionar_hard_skill(self, hardSkill):
        if hardSkill not in self.HardSkills:
            self.HardSkills.append(hardSkill)
        else:
            print("Skill ja adicionada")

    def adicionar_soft_skill (self, softSkill):
        if softSkill not in self.SoftSkills:
            self.SoftSkills.append(softSkill)
        else:
            print("Skill ja adicionada")

    def mostrar_curriculo(self):
        print(f"\nNome: {self.nome} | Idade: {self.idade} | Curso: {self.curso}")
        print("HardSkills:")
        if not self.HardSkills:
            print("Sem hard skills.")
            return
        for s in self.HardSkills:
            print(f" {s}" )
        print("SoftSkills:")
        if not self.SoftSkills:
            print("Sem soft skills.")
            return
        for s in self.SoftSkills:
            print(f" {s}")
        print("Emprego Ideal:")
        if not self.SoftSkills:
            print("Analise o curriculo primeiro!")
            return
        for e in self.empregoIdeal:
            print(f" {e}")

    def calcular_empregoideal(self):
        for i in range(10):
            if hardkills_list[i] in self.HardSkills and softskills_list[i] in self.SoftSkills:
                if empregos_list[i] not in self.empregoIdeal:
                    self.empregoIdeal.append(empregos_list[i])

