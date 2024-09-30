import math

# Constantes
h = 6.62607015e-34  # Constante de Planck em J·s
c = 3.00e8     # Velocidade da luz no vácuo em m/s
eV_to_J = 1.60218e-19  # Conversão de Joules para eV [J/eV]

def intro():
    print("\nSeja bem-vindo ao Programa de Estudo do Modelo Atômico de Bohr!\n")
    print("Este programa calcula parâmetros do átomo de hidrogênio, incluindo raio da órbita, velocidade do elétron, energia cinética, energia potencial, energia total, comprimento de onda de De Broglie e energia do fóton absorvido ou emitido.\nO usuário pode fornecer diferentes entradas e obter os parâmetros correspondentes como saída.\nO algoritmo é útil para compreender e calcular características do modelo atômico de Bohr com base em diferentes variáveis de entrada. As unidades de medida são rigorosamente aplicadas para garantir precisão nos cálculos.\n")
    print("Autores: Carlos, Tallysson e Cecilia\n")

def exibeMenu():
    print("\nMenu:\n")
    print("1. Explorar o modelo de Bohr para um nível n fornecido.\n")
    print("2. Calcular a energia do fóton absorvido, comprimento de onda e frequência para a transição entre níveis quânticos.\n")
    print("3. Calcular a energia do fóton emitido, comprimento de onda e frequência para a transição entre níveis quânticos.\n")
    print("4. Determinar o nível inicial ni com base no nível final nf e na frequência do fóton emitido.\n")
    print("5. Determinar o nível inicial ni com base no nível final nf e no comprimento de onda do fóton emitido.\n")
    print("6. Determinar o nível final nf com base no nível inicial ni e a frequência do fóton absorvido.\n")
    print("7. Determinar o nível final nf com base no nível inicial ni e o comprimento de onda do fóton absorvido.\n")
    print("8. Determinar o nível final nf com base no nível inicial ni e o comprimento de onda do fóton absorvido (caso n = 1).\n")
    print("9. Determinar o nível inicial ni com base no nível final nf e a frequência do fóton absorvido.\n")
    print("10. Determinar o nível inicial ni com base no nível final nf e o comprimento de onda do fóton absorvido.\n")
    print("11. Calcular a energia de um fóton de luz visível com comprimento de onda 546 nm.\n")
    print("12. Calcular a energia de um fóton de luz visível com frequência 4.367 x 10^14 Hz.\n")
    print("13. Calcular os limites do espectro visível (comprimento de onda e frequência).\n")
    print("14. Sair\n")

#ex1
def calcular_propriedades_boehr(n):
    r = n**2 * 5.29e-11 * 1e9
    v = 2.187e6 / n 
    K = 13.6 / n**2 
    U = -27.2 / n**2 
    E = -13.6 / n**2  
    λ = h / (9.11e-31 * v) * 1e9 

    return r, v, K, U, E, λ

#ex2
def calcular_energia_foton(n_inicial, n_final):
    E_inicial = -13.6 / n_inicial**2
    E_final = -13.6 / n_final**2
    E_foton = E_final - E_inicial
    λ_foton = h * c / (E_foton * 1.6e-19) * 1e9 
    f_foton = c / (λ_foton * 1e-9)

    return E_foton, λ_foton, f_foton * 1e-12

#ex3
def calcular_energia_foton_emissao(n_inicial, n_final):
    E_inicial = -13.6 / n_inicial**2
    E_final = -13.6 / n_final**2
    E_foton = E_inicial - E_final
    λ_foton = h * c / (E_foton * 1.6e-19) * 1e9 
    f_foton = c / (λ_foton * 1e-9)

    return E_foton, λ_foton, f_foton * 1e-12

#ex4
def calcular_n_inicial_abs(f_foton, n_final):
    E_foton = h * f_foton * 1e12
    E_foton_eV = E_foton / 1.60218e-19
    E_final = -13.6 / n_final**2 
    E_inicial = E_final + E_foton_eV
    ni = math.sqrt(13.6 / abs(E_inicial))
    
    return ni

#ex5 | ex9 
def calcular_n_inicial(λ_foton, n_final):
    E_foton = h * c / (λ_foton * 1e-9) 
    E_final = -13.6 / n_final**2
    E_inicial = E_final + E_foton / 1.6e-19
    ni = (math.sqrt(-13.6 / E_inicial))
    
    return ni

#ex6
def calcular_n_final_foton_fre(n_inicial, f_foton):
    E_foton = h * f_foton * 1e12 
    E_inicial = -13.6 / n_inicial**2
    E_final = E_inicial - E_foton / 1.6e-19 
    nf = math.sqrt(-13.6 / E_final)
    
    return nf

#ex7
def calcular_nivel_final(n_inicial, λ_foton):
    E_foton_joules = h * c / (λ_foton * 1e-9)
    E_foton_eV = E_foton_joules / eV_to_J
    E_inicial = -13.6 / n_inicial**2
    E_final = E_inicial - E_foton_eV

    if E_final == -13.6:
        nf = 1
    else:
        nf = math.sqrt(-13.6 / E_final)

    return nf

#ex8
def calcular_n_final_foton_lam(n_inicial, λ_foton):
    E_foton = h *  λ_foton * 1e12
    E_inicial = -13.6 / n_inicial**2 
    E_inicial_joules = E_inicial * 1.6e-19
    E_final_joules = E_inicial_joules + E_foton
    E_final = E_final_joules / 1.6e-19
    nf = math.sqrt(-13.6 / E_final)
    return nf

#ex10
def calcular_n_inicial_abs_freq(f_foton, n_final):
    f_foton_hz = f_foton * 1e12
    E_foton_joules = h * f_foton_hz
    E_foton_eV = E_foton_joules / eV_to_J
    E_final = -13.6 / n_final**2
    E_inicial = E_final - E_foton_eV
    ni = math.sqrt(-13.6 / E_inicial)
    
    return ni

#ex11
def calcular_nivel_inicial_hidrogenio(lambda_nm, nf):
    lambda_m = lambda_nm * 1e-9
    E_foton_J = (h * c) / lambda_m
    E_foton_eV = E_foton_J / eV_to_J
    E_final = -13.6 / nf**2
    E_inicial = E_final - E_foton_eV
    ni = math.sqrt(13.6 / abs(E_inicial))
    
    return ni

#ex12
def calcular_energia_foton_comprimento(lambda_nm):
    lambda_m = lambda_nm * 1e-9
    E_joules = (h * c) / lambda_m
    E_eV = E_joules / eV_to_J
    
    return E_joules, E_eV

#ex13
def calcular_energia_foton_frequencia(f_foton):
    E_joules = h * f_foton
    E_eV = E_joules / eV_to_J
    
    return E_joules, E_eV

#ex14
def calcular_espectro_visivel(E_min_eV, E_max_eV):
    E_min_J = E_min_eV * eV_to_J
    E_max_J = E_max_eV * eV_to_J
    λ_min = (h * c) / E_max_J
    λ_max = (h * c) / E_min_J
    λ_min_nm = λ_min * 1e9
    λ_max_nm = λ_max * 1e9
    f_min = E_min_J / h
    f_max = E_max_J / h 
    f_min_1014 = f_min / 1e14
    f_max_1014 = f_max / 1e14
    
    return λ_min_nm, λ_max_nm, f_min_1014, f_max_1014

def menu():
    while True:
        exibeMenu()
        escolha = input("\nDigite o número correspondente à opção desejada: ")

        if escolha == "1":
            n = int(input("Digite o número quântico principal n: "))
            r, v, K, U, E, λ = calcular_propriedades_boehr(n)
            print(f"\nRaio da órbita (r): {r:.3e} nm")
            print(f"Velocidade do elétron (v): {v:.3e} m/s")
            print(f"Energia cinética (K): {K:.3e} eV")
            print(f"Energia potencial (U): {U:.3e} eV")
            print(f"Energia total (E): {E:.3e} eV")
            print(f"Comprimento de onda de De Broglie (λ): {λ:.3e} nm")

        elif escolha == "2":
            n_inicial = int(input("Digite o nível inicial n: "))
            n_final = int(input("Digite o nível final n: "))
            E_foton, λ_foton, f_foton = calcular_energia_foton(n_inicial, n_final)
            print(f"\nEnergia do fóton absorvido (E_foton): {E_foton:.3e} eV")
            print(f"Comprimento de onda do fóton absorvido (λ_foton): {λ_foton:.3e} nm")
            print(f"Frequência do fóton absorvido (f_foton): {f_foton:.3e} THz")

        elif escolha == "3":
            n_inicial = int(input("Digite o nível inicial n: "))
            n_final = int(input("Digite o nível final n: "))
            E_foton, λ_foton, f_foton = calcular_energia_foton_emissao(n_inicial, n_final)
            print(f"\nEnergia do fóton emitido (E_foton): {E_foton:.3e} eV")
            print(f"Comprimento de onda do fóton emitido (λ_foton): {λ_foton:.3e} nm")
            print(f"Frequência do fóton emitido (f_foton): {f_foton:.3e} THz")

        elif escolha == "4":
            n_final = int(input("Digite o nível final n (estado mais baixo): "))
            f_foton = float(input("Digite a frequência do fóton emitido (THz): "))
            ni = calcular_n_inicial_abs(f_foton, n_final)
            print(f"\nNível inicial (ni): {ni:.3f}")

        elif escolha == "5":
            n_inicial = int(input("Digite o nível inicial n: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton emitido (nm): "))
            ni = calcular_n_inicial(λ_foton, n_inicial)
            print(f"\nNível inicial (ni): {int(ni)}")

        elif escolha == "6":
            n_inicial = int(input("Digite o nível inicial n: "))
            f_foton = float(input("Digite a frequência do fóton absorvido (THz): "))
            nf = calcular_n_final_foton_fre(n_inicial, f_foton)
            print(f"\nNível final (nf): {nf:.2f}")

        elif escolha == "7":
            n_inicial = int(input("Digite o nível inicial n: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton absorvido (nm): "))
            nf = calcular_nivel_final(n_inicial, λ_foton) 
            print(f"\nNível final (nf): {nf:.2f}")

        elif escolha == "8":
            n_inicial = float(input("Digite o nível inicial (n_inicial): "))
            f_foton = float(input("Digite a frequência do fóton (em THz): "))

            nf = calcular_n_final_foton_lam(n_inicial, f_foton)
            print(f"\nNível final (nf) após absorver o fóton de frequência {f_foton} THz: {int(nf)}")

        elif escolha == "9":
            n_final = int(input("Digite o nível final nf: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton absorvido (nm): ")) 
            ni = calcular_n_inicial(λ_foton, n_final)
            print(f"\nNível inicial (ni) ao absorver o fóton de comprimento de onda {λ_foton:.3f} nm: {int(ni)}")

        elif escolha == "10":
            n_final = int(input("Digite o nível final nf: "))
            f_foton = float(input("Digite a frequência do fóton absorvido (THz): "))
            ni = calcular_n_inicial_abs_freq(f_foton, n_final)
            print(f"\nNível inicial (ni) ao absorver o fóton de frequência {f_foton} THz: {ni:.2f}")

        elif escolha == "11":
            λ_foton = float(input("Digite o comprimento de onda do fóton absorvido (nm): "))
            n_final = int(input("Digite o nível final nf: "))
            ni = calcular_nivel_inicial_hidrogenio(λ_foton, n_final)
            print(f"\nNível inicial (ni) ao absorver o fóton de comprimento de onda {λ_foton} nm e transitar para nf = {n_final}: {ni:.2f}")
        
        elif escolha == "12":
            lambda_foton = float(input("Digite o comprimento de onda do fóton (em nm): "))
            E_joules, E_eV = calcular_energia_foton_comprimento(lambda_foton)
            print(f"\nEnergia do fóton com comprimento de onda {lambda_foton} nm:")
            print(f"Resposta para parte 1: {E_joules:.3e} J")
            print(f"Resposta para parte 2: {E_eV:.3e} eV")

        elif escolha == "13":
            f_foton = float(input("Digite a frequência do fóton (em Hz): "))
            E_joules, E_eV = calcular_energia_foton_frequencia(f_foton)
            print(f"\nEnergia do fóton com frequência {f_foton:.3e} Hz:")
            print(f"Resposta para parte 1: {E_joules:.3e} J")
            print(f"Resposta para parte 2: {E_eV:.3e} eV")

        elif escolha == "14":
            E_min_eV = float(input("Digite a energia mínima do espectro visível (em eV): "))
            E_max_eV = float(input("Digite a energia máxima do espectro visível (em eV): "))
            λ_min, λ_max, f_min, f_max = calcular_espectro_visivel(E_min_eV, E_max_eV)
            print(f"\nMenor comprimento do espectro visível: {λ_min:.3f} nm")
            print(f"Maior comprimento do espectro visível: {λ_max:.3f} nm")
            print(f"Menor frequência do espectro visível: {f_min:.3f} ×10^14 Hz")
            print(f"Maior frequência do espectro visível: {f_max:.3f} ×10^14 Hz")

        elif escolha == "15":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

def main():
    intro()
    
    while True:
        acessa = input("Deseja acessar o programa? 1 (Sim) e 2 (Não): ")
        
        if acessa == "1":
            menu()
            break
        elif acessa == "2":
            print("Saindo do programa...")
            break
        else:
            print("\nOpção inválida!\n")

if __name__ == "__main__":
    main()
