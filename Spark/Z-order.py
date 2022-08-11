import numpy as np
import pandas as pd

def dec_to_bin(dec: int):
    s = list('00000000')
    for i in range(8, 0, -1):
        if dec > 0:
            dec = dec // 2
            rem = dec % 2
            s[i - 1] = str(rem)
    binstring = ''.join(s)
    return binstring

def bin_to_dec(bin: str):
    dec = 0
    bits = 16
    for i in range(bits, 0, -1):
        dec += pow(2, i - 1) * int(bin[bits - i])

    return dec

def cal_z_value(table: tuple):
    z_values = []
    for tup in table:
        value = ''
        num1_bin = dec_to_bin(tup[0])
        num2_bin = dec_to_bin(tup[1])
        for i in range(8):
            value += num2_bin[i]
            value += num1_bin[i]
        z_values.append(bin_to_dec(value))

    return z_values

def show_table(t: list, cols: list):
    cols_num = len(cols)
    boder_length = 16 * cols_num + 1
    thead_format = "|     {0:<10s}|"
    tbody_format = "|       {0:<8d}|"
    for i in range(1,cols_num):
            thead_format+="     {"+str(i)+":<10s}|"
            tbody_format+="       {"+str(i)+":<8d}|"

    print('\n'*3)
    print(' ' * 80 + '=' * boder_length)
    print(' ' * 80 + thead_format.format(*tuple(cols)))
    print(' ' * 80 + '-' * boder_length)
    for item in t:
        print(' ' * 80 + tbody_format.format(*tuple(item)))
    print(' ' * 80 + '=' * boder_length)

if __name__ == '__main__':
    # x = [1,2,3,4,5,6,7,8,9,100]
    x = np.random.randint(low=1, high=255, size=500, dtype='i')
    y = np.random.randint(low=1, high=255, size=500, dtype='i')
    # x = [i for i in range(1,50,1)]
    # y = [i for i in range(50,1,-1)]
    table = list(zip(x, y))
    z_values = cal_z_value(table)
    z_orderd_table = list(zip(z_values, x, y))
    show_table(sorted(table),["col_X","col_Y"])
    show_table(sorted(z_orderd_table), ["z-value", "col_X", "col_Y"])
