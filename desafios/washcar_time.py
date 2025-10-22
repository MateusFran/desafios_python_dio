from datetime import datetime, timedelta

car_types = {
    'P': timedelta(minutes=10),
    'M': timedelta(minutes=20),
    'G': timedelta(minutes=30)
}


def get_wash_time(car_type):
    # Retorna timedelta de 0 minutos
    if car_type.upper() not in car_types:
        return None, "Tipo de carro inválido. Use P, M ou G."
    return car_types.get(car_type.upper(), timedelta(minutes=0)), True


while True:

    print(
        f'''
                Bem-vindo ao Lava Rápido do DIO!

                Tipos de carros:
                P - Pequeno (Lavagem em {car_types['P'].seconds // 60} minutos)
                M - Médio (Lavagem em {car_types['M'].seconds // 60} minutos)
                G - Grande (Lavagem em {car_types['G'].seconds // 60} minutos)

        '''
    )

    input_car_type = input("Informe o tipo do carro: ").upper()

    now = datetime.now()
    wash_end_time, erro = now + get_wash_time(input_car_type)

    if erro:
        print(f"Erro ao obter o tempo de lavagem: {erro}")
    else:
        print(f"Tempo de lavagem estimado: {wash_end_time}")
