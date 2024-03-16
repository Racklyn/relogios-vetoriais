import socket
import threading
import time
import random

# Configuração inicial dos relógios vetoriais para 4 processos
clocks = [[0, 0, 0, 0] for _ in range(4)]
ports = [5001, 5002, 5003, 5004]

# Função para atualizar o relógio vetorial
def update_clock(clock, sender_id, receiver_id):
    # Atualiza o relógio vetorial com o maior valor entre o relógio local e o relógio recebido para cada entrada
    for i in range(len(clock)):
        clock[i] = max(clock[i], clocks[sender_id][i])
    clock[receiver_id] += 1 # Incrementa o valor do relógio para o processo receptor, indicando um novo evento (recebimento da mensagem)
    return clock

# Função para enviar mensagens de um processo para outro
def send_message(sender_id):
    while True:
        time.sleep(random.uniform(1, 4))  # Intervalo aleatório entre 1s e 4s
        receiver_id = random.choice([i for i in range(4)]) # Escolhe um processo aleatório para enviar a mensagem, excluindo o próprio processo
        if (receiver_id == sender_id):
            clocks[sender_id][sender_id] += 1
            print(f'Evento interno do processo {sender_id}')
            print(f'Vetor do processo {sender_id} atualizado para {clocks[sender_id]}\n')
            continue

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', ports[receiver_id])) # Conecta ao processo receptor
            clocks[sender_id][sender_id] += 1 # Incrementa o relógio do processo remetente
            message = f'Processo {sender_id} enviando: {clocks[sender_id]}'
            print(message)
            s.sendall(str(clocks[sender_id]).encode()) # Envia a mensagem com o relógio do remetente

# Função para receber mensagens de outros processos
def receive_message(receiver_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', ports[receiver_id])) # Liga o socket ao endereço e porta do processo receptor
        s.listen()
        while True:
            conn, _ = s.accept() # Aceita conexões de entrada
            with conn:
                data = conn.recv(1024) # Recebe dados da conexão
                if data:
                    sender_clock = eval(data.decode()) # Converte os dados recebidos para um relógio
                    print(f'Processo {receiver_id} recebeu: {sender_clock}')
                    print(f'Vetor do processo {receiver_id}: {clocks[receiver_id]}')
                    clocks[receiver_id] = update_clock(clocks[receiver_id], sender_clock.index(max(sender_clock)), receiver_id) # Atualiza o relógio do processo receptor
                    print(f'Vetor resultante no processo {receiver_id}: {clocks[receiver_id]}\n')

# Iniciando threads para enviar e receber mensagens
for i in range(4):
    threading.Thread(target=send_message, args=(i,)).start()
    threading.Thread(target=receive_message, args=(i,)).start()
