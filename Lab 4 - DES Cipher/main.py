import random
from tables import S_boxes, P_box, E_box

class DesCipher:
    
    @staticmethod
    def generate_Li_minus_1():
        return ''.join(str(random.randint(0, 1)) for _ in range(32))

    @staticmethod
    def generate_Ri_minus_1():
        return ''.join(str(random.randint(0, 1)) for _ in range(32))

    @staticmethod
    def generate_Round_Key():
        return ''.join(str(random.randint(0, 1)) for _ in range(48))

    @staticmethod
    def get_expansion(Ri):
        if len(Ri) != 32:
            raise ValueError("Input must be a 32-bit binary string")

        expanded_Ri = ''.join(Ri[e - 1] for e in E_box)
        return expanded_Ri

    @staticmethod
    def get_box_substitution(bits):
        if len(bits) != 48:
            raise ValueError("Input must be a 48-bit binary string")

        input_blocks = [bits[i:i+6] for i in range(0, 48, 6)]
        result = ''

        for i in range(8):
            block = input_blocks[i]
            row = int(block[0] + block[5], 2)
            col = int(block[1:5], 2)
            s_box_value = S_boxes[i][row][col]
            s_box_result = format(s_box_value, '04b')
            result += s_box_result

        return result

    @staticmethod
    def get_Pbox_permutation(bits):
        if len(bits) != 32:
            raise ValueError("Input must be a 32-bit binary string")

        result = ''.join(bits[p - 1] for p in P_box)
        return result

    @staticmethod
    def calculate_Ri(Li_minus_1, Ri_minus_1, Round_Key):
        
        expanded_Ri_minus_1 = DesCipher.get_expansion(Ri_minus_1)
        print(f"Expansion Permutation of Ri-1: {expanded_Ri_minus_1}. Length = {len(expanded_Ri_minus_1)} bits.")
        
        xor_operation = ''.join(str(int(a) ^ int(b)) for a, b in zip(Round_Key, expanded_Ri_minus_1))
        print(f"The XOR operation between Round Key and the expanded Ri-1: {xor_operation}. Length = {len(xor_operation)} bits.")
        
        S_box_result = DesCipher.get_box_substitution(xor_operation)
        print(f"The bits were ran through S-Boxes: {S_box_result}. Length = {len(S_box_result)} bits.")
        
        P_box_mix = DesCipher.get_Pbox_permutation(S_box_result)
        print(f"P-Box Permutation of the 32-bit output: {P_box_mix}. Length = {len(P_box_mix)} bits.")
        Ri = ''.join(str(int(Li_minus_1[i]) ^ int(P_box_mix[i])) for i in range(32))
        
        return Ri

    @staticmethod
    def print_P_box():
        print("P-box:")
        for i in range(0, len(P_box), 8):
            print(" ".join(f"{num:2d}" for num in P_box[i:i+8]))

    @staticmethod
    def print_E_box():
        print("E-box:")
        for i in range(0, len(E_box), 6):
            print(" ".join(f"{num:2d}" for num in E_box[i:i+6]))

if __name__ == "__main__":
    DesCipher.print_E_box()
    print("\n")
    DesCipher.print_P_box()
    print("\n")
    

    Li_minus_1 = DesCipher.generate_Li_minus_1()
    Ri_minus_1 = DesCipher.generate_Ri_minus_1()
    Round_Key = DesCipher.generate_Round_Key()
    print(f"Li-1: {Li_minus_1}. Length = {len(Li_minus_1)} bits.")
    print(f"Ri-1: {Ri_minus_1}. Length = {len(Ri_minus_1)} bits.")
    print(f"Round Key: {Round_Key}. Length = {len(Round_Key)} bits.")

    Ri = DesCipher.calculate_Ri(Li_minus_1, Ri_minus_1, Round_Key)
    print(f"Ri after the XOR operation with the given Li-1 is: {Ri}. Length = {len(Ri)} bits.\n")



         


