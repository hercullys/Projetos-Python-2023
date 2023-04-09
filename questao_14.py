#  Questão 14: Peça para o usuário digitar uma 
#  velocidade inicial (em m/s), uma posição inicial 
#  (em m) e um instante de tempo (em s) e imprima a
#  posição de um projétil nesse instante de tempo. 
#  Use a fórmula matemática: y(t) = y(0) + v(0)*t + (g*(t**2)/2) Onde,
#  g é a aceleração da gravidade (-10m/s²), y(t) é a posição final,
#  y(0) é a posição inicial, v(0) é a velocidade 
#  inicial e t é o instante de tempo.

#  Definindo funções auxiliares

def posic_projetil():
    g = 9.81
    posic_inicial = float(input('What is the initial position of the object? (m) '))
    vel_inicial = float(input('What is the initial velocity of the object? (m/s)'))
    time = float(input('Whats the time of the object? (s)'))

    result_projetil = posic_inicial + vel_inicial* time + (g*(time**2)/2)
    return result_projetil

def ascent_time():
    g = 9.81
    initial_launch_speed = float(input('What is initial launch speed of the object? (m/s): '))
    timeToReachTheHighestPoint = (initial_launch_speed / g)
    return timeToReachTheHighestPoint

# Definir o menu:
def menu():
    print('Select the option: ')
    print('1. Projectile Position')
    print('2. Ascent time ')
    op = int(input("Enter the option: "))
    return op

# Função calculadora
def calculator():
    op = menu()
    if op == 1:
        result = posic_projetil()
        result_str = 'The position of the projectile: {:.2f} meters'.format(result)
    elif op == 2:
        result = ascent_time()
        result_str = 'The time to reach the highest point is: {:.2f} seconds'.format(result)
    else:
        result_str = 'Invalid option!'
    return result_str

print(calculator())
