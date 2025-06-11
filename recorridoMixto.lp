\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj1: 1000000 x11 + 5 x12 + 8 x13 + 5 x21 + 1000000 x22 + 6 x23 + 8 x31
       + 6 x32 + 1000000 x33 + r11 + r12 + r13 + r21 + r22 + r23 + r31 + r32
       + r33
Subject To
 Solo_un_deposito#0:             d1 + d2 + d3  = 1
 Visitar_una_sola_vez_cliente_1#1: x11 + x21 + x31 <= 1
 Visitar_una_sola_vez_cliente_2#2: x12 + x22 + x32 <= 1
 Visitar_una_sola_vez_cliente_3#3: x13 + x23 + x33 <= 1
 distancia_maxima_1_a_1#4:       1000000 r11 <= 100
 distancia_maxima_1_a_2#5:       10 r12 <= 100
 distancia_maxima_1_a_3#6:       12 r13 <= 100
 distancia_maxima_2_a_1#7:       10 r21 <= 100
 distancia_maxima_2_a_2#8:       1000000 r22 <= 100
 distancia_maxima_2_a_3#9:       8 r23 <= 100
 distancia_maxima_3_a_1#10:      12 r31 <= 100
 distancia_maxima_3_a_2#11:      8 r32 <= 100
 distancia_maxima_3_a_3#12:      1000000 r33 <= 100
 r11_sale_desde_cliente_visitado#13: x11 + x21 + x31 - r11 + d1 >= 0
 r12_sale_desde_cliente_visitado#14: x11 + x21 + x31 - r12 + d1 >= 0
 r13_sale_desde_cliente_visitado#15: x11 + x21 + x31 - r13 + d1 >= 0
 r21_sale_desde_cliente_visitado#16: x12 + x22 + x32 - r21 + d2 >= 0
 r22_sale_desde_cliente_visitado#17: x12 + x22 + x32 - r22 + d2 >= 0
 r23_sale_desde_cliente_visitado#18: x12 + x22 + x32 - r23 + d2 >= 0
 r31_sale_desde_cliente_visitado#19: x13 + x23 + x33 - r31 + d3 >= 0
 r32_sale_desde_cliente_visitado#20: x13 + x23 + x33 - r32 + d3 >= 0
 r33_sale_desde_cliente_visitado#21: x13 + x23 + x33 - r33 + d3 >= 0
 Conservacion_1#22:              x12 + x13 - x21 - x31  = 0
 Conservacion_2#23:              - x12 + x21 + x23 - x32  = 0
 Conservacion_3#24:              - x13 - x23 + x31 + x32  = 0
 cota_u1#25:                     u1 + d1 >= 1
 cota_u2#26:                     u2 + d2 >= 1
 cota_u3#27:                     u3 + d3 >= 1
 cota_u1#28:                     u1 + 3 d1 <= 3
 cota_u2#29:                     u2 + 3 d2 <= 3
 cota_u3#30:                     u3 + 3 d3 <= 3
 detour_x12#31:                  2 x12 + 2 r12 + u1 - u2 - 3 d1 - 3 d2 <= 1
 detour_x13#32:                  2 x13 + 2 r13 + u1 - u3 - 3 d1 - 3 d3 <= 1
 detour_x21#33:                  2 x21 + 2 r21 - u1 + u2 - 3 d1 - 3 d2 <= 1
 detour_x23#34:                  2 x23 + 2 r23 + u2 - u3 - 3 d2 - 3 d3 <= 1
 detour_x31#35:                  2 x31 + 2 r31 - u1 + u3 - 3 d1 - 3 d3 <= 1
 detour_x32#36:                  2 x32 + 2 r32 - u2 + u3 - 3 d2 - 3 d3 <= 1
 Asegurarse_de_visitar_cliente_1#37: x11 + x21 + x31 + r11 + r21 + r31 + d1
                                 >= 1
 Asegurarse_de_visitar_cliente_2#38: x12 + x22 + x32 + r12 + r22 + r32 + d2
                                 >= 1
 Asegurarse_de_visitar_cliente_3#39: x13 + x23 + x33 + r13 + r23 + r33 + d3
                                 >= 1
 maximo_una_entrega_refrigerada_desde_1#40: r13 <= 1
 maximo_una_entrega_refrigerada_desde_2#41: r23 <= 1
 maximo_una_entrega_refrigerada_desde_3#42: r33 <= 1
Bounds
 0 <= x11 <= 1
 0 <= x12 <= 1
 0 <= x13 <= 1
 0 <= x21 <= 1
 0 <= x22 <= 1
 0 <= x23 <= 1
 0 <= x31 <= 1
 0 <= x32 <= 1
 0 <= x33 <= 1
 0 <= r11 <= 1
 0 <= r12 <= 1
 0 <= r13 <= 1
 0 <= r21 <= 1
 0 <= r22 <= 1
 0 <= r23 <= 1
 0 <= r31 <= 1
 0 <= r32 <= 1
 0 <= r33 <= 1
 0 <= u1 <= 2
 0 <= u2 <= 2
 0 <= u3 <= 2
 0 <= d1 <= 1
 0 <= d2 <= 1
 0 <= d3 <= 1
Binaries
 x11  x12  x13  x21  x22  x23  x31  x32  x33  r11  r12  r13  r21  r22  r23 
 r31  r32  r33  d1  d2  d3 
Generals
 u1  u2  u3 
End
