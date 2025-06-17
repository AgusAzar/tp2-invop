\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj1: 1000000 x11 + 100 x12 + 100 x13 + 10000 x14 + 1000000 x15 + 100 x21
       + 1000000 x22 + 100 x23 + 1000000 x24 + 10000 x25 + 100 x31 + 100 x32
       + 1000000 x33 + 1000000 x34 + 10000 x35 + 10000 x41 + 1000000 x42
       + 1000000 x43 + 1000000 x44 + 1000000 x45 + 1000000 x51 + 10000 x52
       + 10000 x53 + 1000000 x54 + 1000000 x55 + 5 r11 + 5 r12 + 5 r13 + 5 r14
       + 5 r15 + 5 r21 + 5 r22 + 5 r23 + 5 r24 + 5 r25 + 5 r31 + 5 r32 + 5 r33
       + 5 r34 + 5 r35 + 5 r41 + 5 r42 + 5 r43 + 5 r44 + 5 r45 + 5 r51 + 5 r52
       + 5 r53 + 5 r54 + 5 r55
Subject To
 Solo_un_deposito#0:             d1 + d2 + d3 + d4 + d5  = 1
 Visitar_una_sola_vez_cliente_1#1: x11 + x21 + x31 + x41 + x51 <= 1
 Visitar_una_sola_vez_cliente_2#2: x12 + x22 + x32 + x42 + x52 <= 1
 Visitar_una_sola_vez_cliente_3#3: x13 + x23 + x33 + x43 + x53 <= 1
 Visitar_una_sola_vez_cliente_4#4: x14 + x24 + x34 + x44 + x54 <= 1
 Visitar_una_sola_vez_cliente_5#5: x15 + x25 + x35 + x45 + x55 <= 1
 distancia_maxima_1_a_1#6:       1000000 r11 <= 5
 distancia_maxima_1_a_2#7:       10 r12 <= 5
 distancia_maxima_1_a_3#8:       10 r13 <= 5
 distancia_maxima_1_a_4#9:       r14 <= 5
 distancia_maxima_1_a_5#10:      1000000 r15 <= 5
 distancia_maxima_2_a_1#11:      10 r21 <= 5
 distancia_maxima_2_a_2#12:      1000000 r22 <= 5
 distancia_maxima_2_a_3#13:      10 r23 <= 5
 distancia_maxima_2_a_4#14:      1000000 r24 <= 5
 distancia_maxima_2_a_5#15:      r25 <= 5
 distancia_maxima_3_a_1#16:      10 r31 <= 5
 distancia_maxima_3_a_2#17:      10 r32 <= 5
 distancia_maxima_3_a_3#18:      1000000 r33 <= 5
 distancia_maxima_3_a_4#19:      1000000 r34 <= 5
 distancia_maxima_3_a_5#20:      r35 <= 5
 distancia_maxima_4_a_1#21:      r41 <= 5
 distancia_maxima_4_a_2#22:      1000000 r42 <= 5
 distancia_maxima_4_a_3#23:      1000000 r43 <= 5
 distancia_maxima_4_a_4#24:      1000000 r44 <= 5
 distancia_maxima_4_a_5#25:      1000000 r45 <= 5
 distancia_maxima_5_a_1#26:      1000000 r51 <= 5
 distancia_maxima_5_a_2#27:      r52 <= 5
 distancia_maxima_5_a_3#28:      r53 <= 5
 distancia_maxima_5_a_4#29:      1000000 r54 <= 5
 distancia_maxima_5_a_5#30:      1000000 r55 <= 5
 r11_sale_desde_cliente_visitado#31: x11 + x21 + x31 + x41 + x51 - r11 + d1
                                 >= 0
 r12_sale_desde_cliente_visitado#32: x11 + x21 + x31 + x41 + x51 - r12 + d1
                                 >= 0
 r13_sale_desde_cliente_visitado#33: x11 + x21 + x31 + x41 + x51 - r13 + d1
                                 >= 0
 r14_sale_desde_cliente_visitado#34: x11 + x21 + x31 + x41 + x51 - r14 + d1
                                 >= 0
 r15_sale_desde_cliente_visitado#35: x11 + x21 + x31 + x41 + x51 - r15 + d1
                                 >= 0
 r21_sale_desde_cliente_visitado#36: x12 + x22 + x32 + x42 + x52 - r21 + d2
                                 >= 0
 r22_sale_desde_cliente_visitado#37: x12 + x22 + x32 + x42 + x52 - r22 + d2
                                 >= 0
 r23_sale_desde_cliente_visitado#38: x12 + x22 + x32 + x42 + x52 - r23 + d2
                                 >= 0
 r24_sale_desde_cliente_visitado#39: x12 + x22 + x32 + x42 + x52 - r24 + d2
                                 >= 0
 r25_sale_desde_cliente_visitado#40: x12 + x22 + x32 + x42 + x52 - r25 + d2
                                 >= 0
 r31_sale_desde_cliente_visitado#41: x13 + x23 + x33 + x43 + x53 - r31 + d3
                                 >= 0
 r32_sale_desde_cliente_visitado#42: x13 + x23 + x33 + x43 + x53 - r32 + d3
                                 >= 0
 r33_sale_desde_cliente_visitado#43: x13 + x23 + x33 + x43 + x53 - r33 + d3
                                 >= 0
 r34_sale_desde_cliente_visitado#44: x13 + x23 + x33 + x43 + x53 - r34 + d3
                                 >= 0
 r35_sale_desde_cliente_visitado#45: x13 + x23 + x33 + x43 + x53 - r35 + d3
                                 >= 0
 r41_sale_desde_cliente_visitado#46: x14 + x24 + x34 + x44 + x54 - r41 + d4
                                 >= 0
 r42_sale_desde_cliente_visitado#47: x14 + x24 + x34 + x44 + x54 - r42 + d4
                                 >= 0
 r43_sale_desde_cliente_visitado#48: x14 + x24 + x34 + x44 + x54 - r43 + d4
                                 >= 0
 r44_sale_desde_cliente_visitado#49: x14 + x24 + x34 + x44 + x54 - r44 + d4
                                 >= 0
 r45_sale_desde_cliente_visitado#50: x14 + x24 + x34 + x44 + x54 - r45 + d4
                                 >= 0
 r51_sale_desde_cliente_visitado#51: x15 + x25 + x35 + x45 + x55 - r51 + d5
                                 >= 0
 r52_sale_desde_cliente_visitado#52: x15 + x25 + x35 + x45 + x55 - r52 + d5
                                 >= 0
 r53_sale_desde_cliente_visitado#53: x15 + x25 + x35 + x45 + x55 - r53 + d5
                                 >= 0
 r54_sale_desde_cliente_visitado#54: x15 + x25 + x35 + x45 + x55 - r54 + d5
                                 >= 0
 r55_sale_desde_cliente_visitado#55: x15 + x25 + x35 + x45 + x55 - r55 + d5
                                 >= 0
 Conservacion_1#56:              x12 + x13 + x14 + x15 - x21 - x31 - x41 - x51
                                  = 0
 Conservacion_2#57:              - x12 + x21 + x23 + x24 + x25 - x32 - x42
                                 - x52  = 0
 Conservacion_3#58:              - x13 - x23 + x31 + x32 + x34 + x35 - x43
                                 - x53  = 0
 Conservacion_4#59:              - x14 - x24 - x34 + x41 + x42 + x43 + x45
                                 - x54  = 0
 Conservacion_5#60:              - x15 - x25 - x35 - x45 + x51 + x52 + x53
                                 + x54  = 0
 cota_u1#61:                     u1 + d1 >= 1
 cota_u2#62:                     u2 + d2 >= 1
 cota_u3#63:                     u3 + d3 >= 1
 cota_u4#64:                     u4 + d4 >= 1
 cota_u5#65:                     u5 + d5 >= 1
 cota_u1#66:                     u1 + 5 d1 <= 5
 cota_u2#67:                     u2 + 5 d2 <= 5
 cota_u3#68:                     u3 + 5 d3 <= 5
 cota_u4#69:                     u4 + 5 d4 <= 5
 cota_u5#70:                     u5 + 5 d5 <= 5
 detour_x12#71:                  4 x12 + 4 r12 + u1 - u2 - 5 d1 - 5 d2 <= 3
 detour_x13#72:                  4 x13 + 4 r13 + u1 - u3 - 5 d1 - 5 d3 <= 3
 detour_x14#73:                  4 x14 + 4 r14 + u1 - u4 - 5 d1 - 5 d4 <= 3
 detour_x15#74:                  4 x15 + 4 r15 + u1 - u5 - 5 d1 - 5 d5 <= 3
 detour_x21#75:                  4 x21 + 4 r21 - u1 + u2 - 5 d1 - 5 d2 <= 3
 detour_x23#76:                  4 x23 + 4 r23 + u2 - u3 - 5 d2 - 5 d3 <= 3
 detour_x24#77:                  4 x24 + 4 r24 + u2 - u4 - 5 d2 - 5 d4 <= 3
 detour_x25#78:                  4 x25 + 4 r25 + u2 - u5 - 5 d2 - 5 d5 <= 3
 detour_x31#79:                  4 x31 + 4 r31 - u1 + u3 - 5 d1 - 5 d3 <= 3
 detour_x32#80:                  4 x32 + 4 r32 - u2 + u3 - 5 d2 - 5 d3 <= 3
 detour_x34#81:                  4 x34 + 4 r34 + u3 - u4 - 5 d3 - 5 d4 <= 3
 detour_x35#82:                  4 x35 + 4 r35 + u3 - u5 - 5 d3 - 5 d5 <= 3
 detour_x41#83:                  4 x41 + 4 r41 - u1 + u4 - 5 d1 - 5 d4 <= 3
 detour_x42#84:                  4 x42 + 4 r42 - u2 + u4 - 5 d2 - 5 d4 <= 3
 detour_x43#85:                  4 x43 + 4 r43 - u3 + u4 - 5 d3 - 5 d4 <= 3
 detour_x45#86:                  4 x45 + 4 r45 + u4 - u5 - 5 d4 - 5 d5 <= 3
 detour_x51#87:                  4 x51 + 4 r51 - u1 + u5 - 5 d1 - 5 d5 <= 3
 detour_x52#88:                  4 x52 + 4 r52 - u2 + u5 - 5 d2 - 5 d5 <= 3
 detour_x53#89:                  4 x53 + 4 r53 - u3 + u5 - 5 d3 - 5 d5 <= 3
 detour_x54#90:                  4 x54 + 4 r54 - u4 + u5 - 5 d4 - 5 d5 <= 3
 Asegurarse_de_visitar_cliente_1#91: x11 + x21 + x31 + x41 + x51 + r11 + r21
                                 + r31 + r41 + r51 + d1 >= 1
 Asegurarse_de_visitar_cliente_2#92: x12 + x22 + x32 + x42 + x52 + r12 + r22
                                 + r32 + r42 + r52 + d2 >= 1
 Asegurarse_de_visitar_cliente_3#93: x13 + x23 + x33 + x43 + x53 + r13 + r23
                                 + r33 + r43 + r53 + d3 >= 1
 Asegurarse_de_visitar_cliente_4#94: x14 + x24 + x34 + x44 + x54 + r14 + r24
                                 + r34 + r44 + r54 + d4 >= 1
 Asegurarse_de_visitar_cliente_5#95: x15 + x25 + x35 + x45 + x55 + r15 + r25
                                 + r35 + r45 + r55 + d5 >= 1
 maximo_una_entrega_refrigerada_desde_1#96: r12 <= 1
 maximo_una_entrega_refrigerada_desde_2#97: r22 <= 1
 maximo_una_entrega_refrigerada_desde_3#98: r32 <= 1
 maximo_una_entrega_refrigerada_desde_4#99: r42 <= 1
 maximo_una_entrega_refrigerada_desde_5#100: r52 <= 1
Bounds
 0 <= x11 <= 1
 0 <= x12 <= 1
 0 <= x13 <= 1
 0 <= x14 <= 1
 0 <= x15 <= 1
 0 <= x21 <= 1
 0 <= x22 <= 1
 0 <= x23 <= 1
 0 <= x24 <= 1
 0 <= x25 <= 1
 0 <= x31 <= 1
 0 <= x32 <= 1
 0 <= x33 <= 1
 0 <= x34 <= 1
 0 <= x35 <= 1
 0 <= x41 <= 1
 0 <= x42 <= 1
 0 <= x43 <= 1
 0 <= x44 <= 1
 0 <= x45 <= 1
 0 <= x51 <= 1
 0 <= x52 <= 1
 0 <= x53 <= 1
 0 <= x54 <= 1
 0 <= x55 <= 1
 0 <= r11 <= 1
 0 <= r12 <= 1
 0 <= r13 <= 1
 0 <= r14 <= 1
 0 <= r15 <= 1
 0 <= r21 <= 1
 0 <= r22 <= 1
 0 <= r23 <= 1
 0 <= r24 <= 1
 0 <= r25 <= 1
 0 <= r31 <= 1
 0 <= r32 <= 1
 0 <= r33 <= 1
 0 <= r34 <= 1
 0 <= r35 <= 1
 0 <= r41 <= 1
 0 <= r42 <= 1
 0 <= r43 <= 1
 0 <= r44 <= 1
 0 <= r45 <= 1
 0 <= r51 <= 1
 0 <= r52 <= 1
 0 <= r53 <= 1
 0 <= r54 <= 1
 0 <= r55 <= 1
 0 <= u1 <= 4
 0 <= u2 <= 4
 0 <= u3 <= 4
 0 <= u4 <= 4
 0 <= u5 <= 4
 0 <= d1 <= 1
 0 <= d2 <= 1
 0 <= d3 <= 1
 0 <= d4 <= 1
 0 <= d5 <= 1
Binaries
 x11  x12  x13  x14  x15  x21  x22  x23  x24  x25  x31  x32  x33  x34  x35 
 x41  x42  x43  x44  x45  x51  x52  x53  x54  x55  r11  r12  r13  r14  r15 
 r21  r22  r23  r24  r25  r31  r32  r33  r34  r35  r41  r42  r43  r44  r45 
 r51  r52  r53  r54  r55  d1  d2  d3  d4  d5 
Generals
 u1  u2  u3  u4  u5 
End
