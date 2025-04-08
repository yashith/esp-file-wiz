def hex_to_operator(hex_val):
    '''
    0=Equal to
    1=Not equal to
    2=Greater than
    3=Greater than or equal to
    4=Less than
    5=Less than or equal to
    '''
    op=int(bin(int(hex_val,16))[2:5],2)
    return op

