import serial.tools.list_ports
import os

nome = input("Digite o nome do arquivo: ").strip('\n').strip('.txt').strip() + '.txt'
baud = 115200

while os.path.exists(nome):
    inp = input(f"O arquivo '{nome}' já existe. Deseja sobrescrever? (s/n): ").strip().lower()
    if inp in ['n','nao', 'nn','0']:
        nome = input("Digite o nome do arquivo: ").strip('\n').strip('txt') + '.txt'
    else:
        break

print()

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

if len(ports) == 0:
    print("Nenhuma porta serial encontrada")
    exit()

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))
print()

val = input("Selecione a porta: COM")

for x in range(0, len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portVar = 'COM' + str(val)

serialInst.baudrate = baud
serialInst.port = portVar
serialInst.open()

arquivo = open(nome, 'w')
print("\nGravando dados...\nCtrl+C para parar")
print()

while 1:
    if serialInst.in_waiting:
        val = serialInst.readline()
        val = val.decode("utf").strip()

        arquivo.write(val+'\n')
        print(val)
