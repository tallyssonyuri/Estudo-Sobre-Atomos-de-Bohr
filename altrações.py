#ALTERAÇOESNA13/14 E 8
import math

# Constantes
h = 6.626e-34  # Constante de Planck em J·s
c = 3.00e8     # Velocidade da luz no vácuo em m/s

def intro():
    print("\nSeja bem-vindo ao Programa de Estudo do Modelo Atômico de Bohr!\n")
    print("Este programa calcula parâmetros do átomo de hidrogênio, incluindo raio da órbita, velocidade do elétron, energia cinética, energia potencial, energia total, comprimento de onda de De Broglie e energia do fóton absorvido ou emitido.\nO usuário pode fornecer diferentes entradas e obter os parâmetros correspondentes como saída.\nO algoritmo é útil para compreender e calcular características do modelo atômico de Bohr com base em diferentes variáveis de entrada. As unidades de medida são rigorosamente aplicadas para garantir precisão nos cálculos.\n")
    print("Autores: Carlos, Tallysson e Cecilia\n")

def exibeMenu():
    print("\nMenu:\n")
    print("1. Explorar o modelo de Bohr para um nível n fornecido.\n")
    print("2. Calcular a energia do fóton absorvido, comprimento de onda e frequência para a transição entre níveis quânticos.\n")
    print("3. Calcular a energia do fóton emitido, comprimento de onda e frequência para a transição entre níveis quânticos.\n")
    print("4. Determinar o nível inicial ni com base no nível final nf e no comprimento de onda do fóton emitido.\n")
    print("5. Determinar o nível inicial ni com base no nível final nf e na frequência do fóton emitido.\n")
    print("6. Determinar o nível final nf com base no nível inicial ni e a frequência do fóton absorvido.\n")
    print("7. Determinar o nível final nf com base no nível inicial ni e o comprimento de onda do fóton absorvido.\n")
    print("8. Determinar o nível final nf com base no nível inicial ni e o comprimento de onda do fóton absorvido (caso n = 1).\n")
    print("9. Determinar o nível inicial ni com base no nível final nf e a frequência do fóton absorvido.\n")
    print("10. Determinar o nível inicial ni com base no nível final nf e o comprimento de onda do fóton absorvido.\n")
    print("11. Calcular a energia de um fóton de luz visível com comprimento de onda 546 nm.\n")
    print("12. Calcular a energia de um fóton de luz visível com frequência 4.367 x 10^14 Hz.\n")
    print("13. Calcular os limites do espectro visível (comprimento de onda e frequência).\n")
    print("14. Sair\n")

def calcular_propriedades_boehr(n):
    # Cálculos
    r = n**2 * 5.29e-11  # raio da órbita em metros
    v = 2.187e6 / n      # velocidade do elétron em m/s
    K = 13.6 / n**2      # energia cinética em eV
    U = -27.2 / n**2     # energia potencial em eV
    E = -13.6 / n**2     # energia total em eV
    λ = h / (9.11e-31 * v) * 1e9  # comprimento de onda de De Broglie em nm

    return r, v, K, U, E, λ

def calcular_energia_foton(n_inicial, n_final):
    E_inicial = -13.6 / n_inicial**2
    E_final = -13.6 / n_final**2
    E_foton = E_final - E_inicial
    λ_foton = h * c / (E_foton * 1.6e-19) * 1e9  # comprimento de onda em nm
    f_foton = c / (λ_foton * 1e-9) #frequencia do foton (HZ)

    return E_foton, λ_foton, f_foton * 1e-12 #Frequencia em THz

def calcular_energia_foton_emissao(n_inicial, n_final):
    E_inicial = -13.6 / n_inicial**2
    E_final = -13.6 / n_final**2
    E_foton = E_inicial - E_final
    λ_foton = h * c / (E_foton * 1.6e-19) * 1e9  # comprimento de onda em nm
    f_foton = c / (λ_foton * 1e-9) #frequencia do foton (HZ)

    return E_foton, λ_foton, f_foton * 1e-12 # frequência em THz

def calcular_n_inicial(λ_foton, n_final):
    E_foton = h * c / (λ_foton * 1e-9)  # energia do fóton em joules
    E_final = -13.6 / n_final**2
    E_inicial = E_final + E_foton / 1.6e-19  # converte para eV
    ni = (math.sqrt(-13.6 / E_inicial))
    
    return ni

def calcular_n_final_foton_fre(n_inicial, f_foton):
    E_foton = h * f_foton * 1e12  # energia do fóton em joules
    E_inicial = -13.6 / n_inicial**2
    E_final = E_inicial - E_foton / 1.6e-19  # converte para eV
    nf = math.sqrt(-13.6 / E_final)
    
    return nf

def calcular_n_final_foton_lam(n_inicial, λ_foton):
    E_foton = h * c / (λ_foton * 1e-9)  # energia do fóton em joules
    E_inicial = -13.6 / n_inicial**2
    E_final = E_inicial - E_foton / 1.6e-19  # converte para eV
    nf = math.sqrt(-13.6 / E_final)
    
    return nf

def calcular_n_inicial_abs(f_foton, n_final):
    E_foton = h * f_foton * 1e12  # energia do fóton em joules
    E_final = -13.6 / n_final**2
    E_inicial = E_final - E_foton / 1.6e-19  # converte para eV
    ni = (math.sqrt(-13.6 / E_inicial))
    
    return ni

def calcular_n_inicial_abs_lam(λ_foton, n_final):
    E_foton = h * c / (λ_foton * 1e-9)  # energia do fóton em joules
    E_final = -13.6 / n_final**2
    E_inicial = E_final - E_foton / 1.6e-19  # converte para eV
    ni = (math.sqrt(-13.6 / E_inicial))
    
    return ni

def calcular_energia_foton_luz_visivel(λ):
    E_joules = h * c / (λ * 1e-9)  # energia em joules
    E_eV = E_joules / 1.602e-19  # conversão para eV
    return E_joules, E_eV

def calcular_energia_foton_fre(f):
    E_joules = h * f  # energia em joules
    E_eV = E_joules / 1.602e-19  # conversão para eV
    return E_joules, E_eV

def calcular_comprimento_fre(energia):
    return h * c / energia  # comprimento em metros

def calcular_frequencia(energia):
    return energia / h  # frequência em Hz

def menu():
    while True:
        exibeMenu()
        escolha = input("\nDigite o número correspondente à opção desejada: ")

        if escolha == "1":
            n = int(input("Digite o número quântico principal n: "))
            r, v, K, U, E, λ = calcular_propriedades_boehr(n)
            print(f"\nRaio da órbita (r): {r:.3e} m")
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
            n_inicial = int(input("Digite o nível inicial n: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton emitido (nm): "))
            ni = calcular_n_inicial(λ_foton, n_inicial)
            print(f"\nNível inicial (ni): {ni:.2f}")

        elif escolha == "5":
            n_final = int(input("Digite o nível final n (estado mais baixo): "))
            f_foton = float(input("Digite a frequência do fóton emitido (THz): "))
            ni = calcular_n_inicial_abs(f_foton, n_final)
            print(f"\nNível inicial (ni): {ni:.2f}")

        elif escolha == "6":
            n_inicial = int(input("Digite o nível inicial n: "))
            f_foton = float(input("Digite a frequência do fóton absorvido (THz): "))
            nf = calcular_n_final_foton_fre(n_inicial, f_foton)
            print(f"\nNível final (nf): {nf:.2f}")

        elif escolha == "7":
            n_inicial = int(input("Digite o nível inicial n: "))
            λ_foton = float(input("Digite o comprimento de onda do fóton absorvido (nm): "))
            nf = calcular_n_final_foton_lam(n_inicial, λ_foton)
            print(f"\nNível final (nf): {nf:.2f}")

        elif escolha == "8":
            n_inicial = 1
            λ_foton = 3082.69  # nm
            nf = calcular_n_final_foton_lam(n_inicial, λ_foton)
            print(f"\nNível final (nf) após absorver o fóton de comprimento de onda {λ_foton} nm: {nf:.2f}")

        elif escolha == "9":
            n_final = int(input("Digite o nível final nf: "))
            f_foton = 616.54  # THz
            ni = calcular_n_inicial_abs(f_foton, n_final)
            print(f"\nNível inicial (ni) ao absorver o fóton de frequência {f_foton} THz: {ni:.2f}")

        elif escolha == "10":
            n_final = int(input("Digite o nível final nf: "))
            λ_foton = 102.6397  # nm
            ni = calcular_n_inicial_abs_lam(λ_foton, n_final)
            print(f"\nNível inicial (ni) ao absorver o fóton de comprimento de onda {λ_foton} nm: {ni:.2f}")

        elif escolha == "11":
            λ_foton = 546  # nm
            E_joules, E_eV = calcular_energia_foton_luz_visivel(λ_foton)
            print(f"\nEnergia do fóton com comprimento de onda {λ_foton} nm:")
            print(f"Resposta para parte 1: {E_joules:.3e} J")
            print(f"Resposta para parte 2: {E_eV:.3e} eV")

        elif escolha == "12":
            f_foton = 4.367e14  # Hz
            E_joules, E_eV = calcular_energia_foton_fre(f_foton)
            print(f"\nEnergia do fóton com frequência {f_foton:.3e} Hz:")
            print(f"Resposta para parte 1: {E_joules:.3e} J")
            print(f"Resposta para parte 2: {E_eV:.3e} eV")

        elif escolha == "13":
            print("\nCálculo dos limites do espectro visível:")
            E_min = 2.84e-19  # J
            E_max = 4.969e-19  # J
            
            λ_min = h * c / E_max * 1e9  # comprimento de onda mínimo em nm
            λ_max = h * c / E_min * 1e9  # comprimento de onda máximo em nm
            
            f_min = E_min / h  # frequência mínima em Hz
            f_max = E_max / h  # frequência máxima em Hz

            print(f"\nParte 1: Menor comprimento do espectro visível (λ_min): {λ_min:.3f} nm")
            print(f"Parte 2: Maior comprimento do espectro visível (λ_max): {λ_max:.3f} nm")
            print(f"Parte 3: Menor frequência do espectro visível (f_min): {f_min / 1e12:.3f} × 10^12 Hz")
            print(f"Parte 4: Maior frequência do espectro visível (f_max): {f_max / 1e12:.3f} × 10^12 Hz")

        elif escolha == "14":
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
