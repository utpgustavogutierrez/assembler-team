
import re

# Expresiones regulares
label_pattern = re.compile(r'^\s*([^\s]+):')
instruction_pattern = re.compile(r'^\s*[^#;.].*') 
directive_pattern = re.compile(r'^\s*\..*')
comment_pattern = re.compile(r'^\s*[#;].*')

parentesis_pattern = re.compile(r'\((x.*?)\)')

# Tabla de códigos de operación
opcode_mapping = {
    'add': {
        'opcode': '0110011',
        'funct3': '000',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'sub': {
        'opcode': '0110011',
        'funct3': '000',
        'funct7': '0100000',
        'tipo': 'r'
    },
    'sll': {
        'opcode': '0110011',
        'funct3': '001',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'slt': {
        'opcode': '0110011',
        'funct3': '010',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'sltu': {
        'opcode': '0110011',
        'funct3': '011',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'xor': {
        'opcode': '0110011',
        'funct3': '100',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'srl': {
        'opcode': '0110011',
        'funct3': '101',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'sra': {
        'opcode': '0110011',
        'funct3': '101',
        'funct7': '0100000',
        'tipo': 'r'
    },
    'or': {
        'opcode': '0110011',
        'funct3': '110',
        'funct7': '0000000',
        'tipo': 'r'
    },
    'and': {
        'opcode': '0110011',
        'funct3': '111',
        'funct7': '0000000',
        'tipo': 'r'
    },
    


    'addi': {
        'opcode': '0010011',
        'funct3': '000',
        'tipo': 'i'   
    },
    'xori': {
        'opcode': '0010011',
        'funct3': '100',
        'tipo': 'i'   
    },
    'ori': {
        'opcode': '0010011',
        'funct3': '110',
        'tipo': 'i' 
    },
    'andi': {
        'opcode': '0010011',
        'funct3': '111',
        'tipo': 'i'   
    },

    'slli': {
        'imm7': '"0000000"',
        'opcode': '0010011',
        'funct3': '001',
        'tipo': 'i'   
    },
    'srli': {
        'imm7': '"0000000"',
        'opcode': '0010011',
        'funct3': '101',
        'tipo': 'i'   
    },
    'srai': {
        'imm7': '0100000',
        'opcode': '0010011',
        'funct3': '101',
        'tipo': 'i'  
    },

    'slti': {
        'opcode': '0010011',
        'funct3': '010',
        'tipo': 'i' 
    },

    'sltiu': {
        'opcode': '0010011',
        'funct3': '011',
        'tipo': 'i'  
    },

    'lb': {
        'opcode': '0000011',
        'funct3': '000',
        'tipo': 'i'   
    },
    'lh': {
        'opcode': '0000011',
        'funct3': '001',
        'tipo': 'i'
    },
    'lw': {
        'opcode': '0000011',
        'funct3': '010',
        'tipo': 'i'
    },
    'lbu': {
        'opcode': '0000011',
        'funct3': '100',
        'tipo': 'i'
    },
    'lhu': {
        'opcode': '0000011',
        'funct3': '101',
        'tipo': 'i'
    },
    
    'sb': {
        'opcode': '0100011',
        'funct3': '000',
        'tipo': 's'
    },
    'sh': {
        'opcode': '0100011',
        'funct3': '001',
        'tipo': 's'
    },
    'sw': {
        'opcode': '0100011',
        'funct3': '010',
        'tipo': 's'
    },

    'beq': {
        'opcode': '1100011',
        'funct3': '000',
        'tipo': 'b'
    },
    'bne': {
        'opcode': '1100011',
        'funct3': '001',
        'tipo': 'b'
    },
    'blt': {
        'opcode': '1100011',
        'funct3': '100',
        'tipo': 'b'
    },
    'bge': {
        'opcode': '1100011',
        'funct3': '101',
        'tipo': 'b'
    },
    'bltu': {
        'opcode': '1100011',
        'funct3': '110',
        'tipo': 'b'
    },
    'bgeu': {
        'opcode': '1100011',
        'funct3': '111',
        'tipo': 'b'
    },

    'jal': '1101111',
    'jalr': {
        'opcode': '1100111',
        'funct3': '000' 
    },

    'lui': '0110111',
    'auipc': '0010111',
    
    'ecall': {
        'imm12': '000000000000',
        'rs1': '00000',
        'opcode': '1110011',
        'funct3': '000'  
    },
    'ebreak': {
        'imm12': '000000000001',
        'rs1': '00000',
        'opcode': '1110011',
        'funct3': '000' 
    },

    'mul': '0110011',
    'mulh': '0110011',
    'mulhsu': '0110011',
    'mulhu': '0110011',
    'div': '0110011',
    'divu': '0110011',
    'rem': '0110011',
    'remu': '0110011',

    'lr.w': '0101111',
    'sc.w': '0101111',

    'amoswap.w': '0101111',
    'amoadd.w': '0101111',
    'amoand.w': '0101111',
    'amoor.w': '0101111',
    'amoxor.w': '0101111',
    'amomax.w': '0101111',
    'amomin.w': '0101111',
}

# Diccionario de mapeo de nombres de registro a representaciones binarias
register_mapping = {
    'zero': '00000',
    'ra': '00001',
    'sp': '00010',
    'gp': '00011',
    'tp': '00100',
    't0': '00101',
    't1': '00110',
    't2': '00111',
    's0': '01000',
    'fp': '01000',
    's1': '01001',
    'a0': '01010',
    'a1': '01011',
    'a2': '01100',
    'a3': '01101',
    'a4': '01110',
    'a5': '01111',
    'a6': '10000',
    'a7': '10001',
    's2': '10010',
    's3': '10011',
    's4': '10100',
    's5': '10101',
    's6': '10110',
    's7': '10111',
    's8': '11000',
    's9': '11001',
    's10': '11010',
    's11': '11011',
    't3': '11100',
    't4': '11101',
    't5': '11110',
    't6': '11111',

    'x0': '00000',
    'x1': '00001',
    'x2': '00010',
    'x3': '00011',
    'x4': '00100',
    'x5': '00101',
    'x6': '00110',
    'x7': '00111',
    'x8': '01000',
    'x9': '01001',
    'x10': '01010',
    'x11': '01011',
    'x12': '01100',
    'x13': '01101',
    'x14': '01110',
    'x15': '01111',
    'x16': '10000',
    'x17': '10001',
    'x18': '10010',
    'x19': '10011',
    'x20': '10100',
    'x21': '10101',
    'x22': '10110',
    'x23': '10111',
    'x24': '11000',
    'x25': '11001',
    'x26': '11010',
    'x27': '11011',
    'x28': '11100',
    'x29': '11101',
    'x30': '11110',
    'x31': '11111'
}

def convert_to_twos_complement(num):
    # Verificar si el número es representable en 12 bits con complemento a 2
    if -2048 <= num <= 2047:
        # Si el número es negativo, obtener su representación en complemento a 2
        if num < 0:
            # Calcular el complemento a 2
            complement = (1 << 12) + num  # 1 << 12 representa 2^12
            # Convertir el complemento a su representación binaria
            complement_binary = bin(complement & 0xFFF)[2:].zfill(12)
            return complement_binary
        else:
            # Si el número es positivo, simplemente convertirlo a binario de 12 bits
            binary_rep = bin(num)[2:].zfill(12)
            return str(binary_rep)
    else:
        # Si el número no es representable en 12 bits, lanzar un error
        raise ValueError("Número no representable en 12 bits")

# Función para convertir una instrucción en una línea de 32 bits
def instruction_to_binary(instruction):
    parts = re.split(r'\s|,\s*|\(', instruction)

    result = opcode_mapping.get(parts[0], '0000000')  # Código de operación, si no se encuentra, asume 0000000

    opcode = result['opcode']
    funct3 = result['funct3']
    tipo = result['tipo']

    if parts[-1][-1] == ')':
        parts[-1] = parts[-1][:-1]

        imm = convert_to_twos_complement(int(parts[2]))
        rs1 = register_to_binary(parts[3])

        if tipo == "i":
            rd = register_to_binary(parts[1])
            binary_line = imm + " " + rs1 + " " + funct3 + " " + rd + " " + opcode 
            
        elif tipo == "s":
            parte1 = imm[:7]  # Los primeros 7 bits
            parte2 = imm[7:]  # Los últimos 5 bits
            rs2 = register_to_binary(parts[1])
            binary_line = parte1 + " " + rs2 + " " + rs1 + " " + funct3 + " " + parte2 + " " + opcode  
    else:
        if tipo == "i":
            if parts[0] == "slli" or parts[0] == "slri":
                imm7 = "0000000"
                if int(parts[3]) < 0 or int(parts[3]) > 31:
                    raise ValueError("Constant invalid")
                else:
                    imm = bin(int(parts[3]))[2:].zfill(5)
            elif parts[0] == "srai":
                imm7 = "0100000"
                if int(parts[3]) < 0 or int(parts[3]) > 31:
                    raise ValueError("Constant invalid")
                else:
                    imm = bin(int(parts[3]))[2:].zfill(5)
            else:
                imm7 = ""
                imm = convert_to_twos_complement(int(parts[3]))

            rd = register_to_binary(parts[1])
            rs1 = register_to_binary(parts[2])
            binary_line = imm7 + " " + imm + " " + rs1 + " " + funct3 + " " + rd + " " + opcode 

        elif tipo == "r":
            funct7 = result['funct7']
            rd = register_to_binary(parts[1])
            rs2 = register_to_binary(parts[3])
            rs1 = register_to_binary(parts[2])
            binary_line = funct7 + " " + rs2 + " " + rs1 + " " + funct3 + " " + rd + " " + opcode 
    
    return binary_line

def register_to_binary(rd):
    # Verificar si el nombre del registro es válido
    if rd in register_mapping:
        return register_mapping[rd]  # Devolver la representación binaria del registro
    else:
        # Aquí podrías generar un error o manejar la excepción de otra manera, según tus necesidades
        raise ValueError("Registro no válido: {}".format(rd))

# Archivo de entrada y salida
input_file = 'example.asm'
output_file = 'output.txt'

# Procesamiento del archivo de entrada
with open(input_file, 'r') as infile:
    with open(output_file, 'w') as outfile:
        for line in infile:

            # Ignorar líneas vacías o llenas de espacios
            if not line.strip():
                continue

            # Ignorar comentarios
            if comment_pattern.match(line):
                continue

            if label_pattern.match(line):
                continue

            # Ignorar directivas
            if directive_pattern.match(line):
                continue

            # Procesar instrucciones
            if instruction_pattern.match(line):
                instruction_binary = instruction_to_binary(line.strip())
                if instruction_binary:
                    outfile.write(instruction_binary + '\n')

