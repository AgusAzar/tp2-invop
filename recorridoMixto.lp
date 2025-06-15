\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj1: 1000000 x11 + 5 x12 + 8 x13 + 5 x21 + 1000000 x22 + 6 x23 + 8 x31
       + 6 x32 + 1000000 x33
Subject To
 Visitar_una_sola_vez_cliente_1#0: x11 + x12 + x13  = 1
 Visitar_una_sola_vez_cliente_2#1: x21 + x22 + x23  = 1
 Visitar_una_sola_vez_cliente_3#2: x31 + x32 + x33  = 1
 Conservacion_1#3:               x12 + x13 - x21 - x31  = 0
 Conservacion_2#4:               - x12 + x21 + x23 - x32  = 0
 Conservacion_3#5:               - x13 - x23 + x31 + x32  = 0
 detour_u1#6:                    u1  = 0
 detour_x23#7:                   2 x23 + u2 - u3 <= 1
 detour_x32#8:                   2 x32 - u2 + u3 <= 1
 cota_u2#9:                      u2 >= 1
 cota_u3#10:                     u3 >= 1
 cota_u2#11:                     u2 <= 2
 cota_u3#12:                     u3 <= 2
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
 0 <= u1 <= 2
 0 <= u2 <= 2
 0 <= u3 <= 2
Binaries
 x11  x12  x13  x21  x22  x23  x31  x32  x33 
Generals
 u1  u2  u3 
End
