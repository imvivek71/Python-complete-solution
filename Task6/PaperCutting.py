#"The paper of size A0 has dimensions of 1189mm by 841mm. Each subsequent size A(n) is defined as A(n-1), cut in half parallel to its shorter sides. I write a programme to calculate and print paper sizes A0, A1, A2, and A8
side1 = 1189
side2 = 841
print("Dimenstions of A0 is {} by {}".format(side1,side2))
side1 = side1/2
print("Dimenstions of A1 is {} by {}".format(side1,side2))
side1 = side1/2
print("Dimenstions of A2 is {} by {}".format(side1,side2))
side1 = 1189/2**8
print("Dimenstions of A8 is {} by {}".format(side1,side2))
