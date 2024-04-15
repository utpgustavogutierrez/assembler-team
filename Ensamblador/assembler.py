
import re

# Expresiones regulares
label_pattern = re.compile(r'^\s*([^\s]+):')
instruction_pattern = re.compile(r'^\s*[^#;.].*') 
directive_pattern = re.compile(r'^\s*\..*')
comment_pattern = re.compile(r'^\s*[#;].*')

# Tabla de códigos de operación
opcode_mapping = {
    'add': {
        'opcode': '0110011',
        'funct3': '000',
        'funct7': '0000000'
    },
    'sub': {
        'opcode': '0110011',
        'funct3': '000',
        'funct7': '0100000'
    },
    'sll': {
        'opcode': '0110011',
        'funct3': '001',
        'funct7': '0000000'
    },
    'slt': {
        'opcode': '0110011',
        'funct3': '010',
        'funct7': '0000000'
    },
    'sltu': {
        'opcode': '0110011',
        'funct3': '011',
        'funct7': '0000000'
    },
    'xor': {
        'opcode': '0110011',
        'funct3': '100',
        'funct7': '0000000'
    },
    'srl': {
        'opcode': '0110011',
        'funct3': '101',
        'funct7': '0000000'
    },
    'sra': {
        'opcode': '0110011',
        'funct3': '101',
        'funct7': '0100000'
    },
    'or': {
        'opcode': '0110011',
        'funct3': '110',
        'funct7': '0000000'
    },
    'and': {
        'opcode': '0110011',
        'funct3': '111',
        'funct7': '0000000'
    },
    
    'addi': '0010011',
    'xori': '0010011',
    'ori': '0010011',
    'andi': '0010011',


    'slli': '0010011',
    'srli': '0010011',
    'srai': '0010011',


    'slti': '0010011',
    'sltiu': '0010011',

    'lb': '0000011',
    'lh': '0000011',
    'lw': '0000011',
    'lbu': '0000011',
    'lhu': '0000011',
    
    'sb': '0100011',
    'sh': '0100011',
    'sw': '0100011',

    'beq': '1100011',
    'bne': '1100011',
    'blt': '1100011',
    'bge': '1100011',
    'bltu': '1100011',
    'bgeu': '1100011',

    'jal': '1101111',
    'jalr': '1100111',

    'lui': '0110111',
    'auipc': '0010111',
    
    'ecall': '1110011',
    'ebreak': '1110011',

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

# Función para convertir una instrucción en una línea de 32 bits
def instruction_to_binary(instruction):
    parts = re.split(r'\s|,\s', instruction)

    # Eliminar elementos vacíos (por ejemplo, si hay espacios consecutivos)
    parts = [part.strip() for part in parts if part.strip()]
    
    opcode = opcode_mapping.get(parts[0], '0000000')  # Código de operación, si no se encuentra, asume 0000000

    rd = register_to_binary(parts[1])

    rs1 = register_to_binary(parts[2])
    
    rs2 = register_to_binary(parts[3])
    
    # Combinar opcode con los bits restantes (en este caso, los bits están en la posición 0-24)
    binary_line = '0' * 7 + " " + rs2 + " " + rs1 + " 000 " + rd + " " + opcode  # Coloca el opcode al final, después de los ceros
    
    # Asegurar que la longitud sea de 32 bits
    # binary_line = binary_line[-32:]
    
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

