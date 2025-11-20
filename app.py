from curriculo import Curriculo
from skill_empregos import hardkills_list, softskills_list
def add_curriculo():
    nome = input("Digite o nome: ")
    idade = input("Digite o idade: ")
    curso = input("Digite o curso: ")
    curriculo0 = Curriculo(nome, curso, idade)
    return curriculo0

def add_skills(curriculo):
    print("soft ou hard skills?")
    print("1 - Hard Skill")
    print("2 - Soft Skill")
    print("0 - sair")
    op = input("Escolha: ").strip()
    if op == "1":
        print("escolha uma hard skill")
        print("1 - Modelagem de Machine Learning")
        print("2 - Estatística avançada")
        print("3 - Análise de vulnerabilidades")
        print("4 - Arquitetura em AWS/Azure/GCP")
        print("5 - Automação com CI/CD")
        print("6 - Programação de smart contracts")
        print("7 - Programação embarcada")
        print("8 - Visão computacional")
        print("9 - Análise de sequências biológicas")
        print("10 - Modelagem e integração 3D")
        print("0 - sair")
        op = int(input("Escolha: "))
        if 0 < op <= 10:
            skill = hardkills_list[op-1]
            curriculo.adicionar_hard_skill(skill)
        elif op == "0":
            main()
        else:
            print("Opção inválida.")
    elif op == "2":
        print("escolha uma soft skill")
        print("1 - Pensamento analítico")
        print("2 - Comunicação de insights")
        print("3 - Atenção aos detalhes")
        print("4 - Planejamento estratégico")
        print("5 - Trabalho em equipe")
        print("6 - Pensamento lógico")
        print("7 - Resolução de problemas")
        print("8 - Tomada de decisão")
        print("9 - Raciocínio crítico")
        print("10 - Criatividade")
        print("0 - sair")
        op = int(input("Escolha: "))
        if 0 < op <= 10:
            skill = softskills_list[op - 1]
            curriculo.adicionar_soft_skill(skill)
        elif op == "0":
            main()
        else:
            print("Opção inválida.")
    elif op == "0":
        main()
    else:
        print("Opção inválida.")

def mostrar_curriculo(curriculo):
    curriculo.mostrar_curriculo()

def analisar_curriculo(curriculo):
    curriculo.calcular_empregoideal()
    curriculo.mostrar_curriculo()


def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            curriculo0 = add_curriculo()
        elif op == "2":
            add_skills(curriculo0)
        elif op == "3":
            mostrar_curriculo(curriculo0)
        elif op == "4":
            analisar_curriculo(curriculo0)
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


def print_menu():
    print("\nAnalise de Curriculo")
    print("[1] Adicionar curriculo")
    print("[2] Adicionar skills")
    print("[3] Mostrar curriculo")
    print("[4] Analise de Vagas")
    print("[0] Sair")


if __name__ == "__main__":
    main()