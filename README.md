# Implementação de Relógios Vetoriais

Implementação da lógica de relógios vetoriais em **Python**, utilizando **sockets**.

# Dupla

- Francisco Racklyn Sotero dos Santos (21110615)
- Jucyelle Barros do Nascimento (21110438)

# Instruções

Execute o arquivo vector_clock.py no terminal ou prompt de comando usando o seguinte comando:

```
python vector_clock.py
```

Quando um processo envia uma mensagem para outro processo, temos um retorno semelhante a este:

```
Processo 2 enviando: [0, 0, 1, 0]
Processo 0 recebeu: [0, 0, 1, 0]
Vetor do processo 0: [0, 0, 0, 0]
Vetor resultante no processo 0: [1, 0, 1, 0]
```

Quando um processo realiza um evento interno (ou seja, não envia ou recebe mensagens, mas atualiza seu próprio relógio), o registro será exibido da seguinte forma:

```
Evento interno do processo 0
Vetor do processo 0 atualizado para [2, 0, 1, 0]
```
