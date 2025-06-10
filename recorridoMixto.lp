\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj1: 1000000 x11 + 5 x12 + 8 x13 + 5 x21 + 1000000 x22 + 6 x23 + 8 x31
       + 6 x32 + 1000000 x33 + 2 r11 + 2 r12 + 2 r13 + 2 r21 + 2 r22 + 2 r23
       + 2 r31 + 2 r32 + 2 r33
Subject To
 Visitar_una_sola_vez_cliente_1#0: x11 + x12 + x13 <= 1
 Visitar_una_sola_vez_cliente_2#1: x21 + x22 + x23 <= 1
 Visitar_una_sola_vez_cliente_3#2: x31 + x32 + x33 <= 1
 distancia_maxima_1_a_1#3:       1000000 r11 <= 10
 distancia_maxima_1_a_2#4:       10 r12 <= 10
 distancia_maxima_1_a_3#5:       12 r13 <= 10
 distancia_maxima_2_a_1#6:       10 r21 <= 10
 distancia_maxima_2_a_2#7:       1000000 r22 <= 10
 distancia_maxima_2_a_3#8:       8 r23 <= 10
 distancia_maxima_3_a_1#9:       12 r31 <= 10
 distancia_maxima_3_a_2#10:      8 r32 <= 10
 distancia_maxima_3_a_3#11:      1000000 r33 <= 10
 r21_sale_desde_cliente_visitado#12: x21 + x22 + x23 - r21 >= 0
 r22_sale_desde_cliente_visitado#13: x21 + x22 + x23 - r22 >= 0
 r23_sale_desde_cliente_visitado#14: x21 + x22 + x23 - r23 >= 0
 r31_sale_desde_cliente_visitado#15: x31 + x32 + x33 - r31 >= 0
 r32_sale_desde_cliente_visitado#16: x31 + x32 + x33 - r32 >= 0
 r33_sale_desde_cliente_visitado#17: x31 + x32 + x33 - r33 >= 0
 Conservacion_1#18:              x12 + x13 - x21 - x31  = 0
 Conservacion_2#19:              - x12 + x21 + x23 - x32  = 0
 Conservacion_3#20:              - x13 - x23 + x31 + x32  = 0
 detour_u1#21:                   u1  = 0
 detour_x23#22:                  2 x23 + 2 r23 + u2 - u3 <= 1
 detour_x32#23:                  2 x32 + 2 r32 - u2 + u3 <= 1
 cota_u2#24:                     u2 >= 1
 cota_u3#25:                     u3 >= 1
 Asegurarse_de_visitar_cliente_2#26: x12 + x22 + x32 + r12 + r22 + r32  = 1
 Asegurarse_de_visitar_cliente_3#27: x13 + x23 + x33 + r13 + r23 + r33  = 1
 maximo_una_entrega_refrigerada_desde_1#28: r13 <= 1
 maximo_una_entrega_refrigerada_desde_2#29: r23 <= 1
 maximo_una_entrega_refrigerada_desde_3#30: r33 <= 1
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
Binaries
 x11  x12  x13  x21  x22  x23  x31  x32  x33  r11  r12  r13  r21  r22  r23 
 r31  r32  r33 
Generals
 u1  u2  u3 
End
