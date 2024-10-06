from solutions.CHK import checkout_solution


class TestSum():
    def test_eight_A(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_one_A(self):
        assert checkout_solution.checkout("A") == 50

    def test_two_A(self):
        assert checkout_solution.checkout("AA") == 100

    def test_five_B(self):
        assert checkout_solution.checkout("BBBBB") == 120

    def test_one_B(self):
        assert checkout_solution.checkout("B") == 30

    def test_one_C(self):
        assert checkout_solution.checkout("C") == 20

    def test_three_D(self):
        assert checkout_solution.checkout("DDD") == 45

    def test_one_E(self):
        assert checkout_solution.checkout("E") == 40

    def test_two_E(self):
        assert checkout_solution.checkout("EE") == 80

    def test_two_E_one_B(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_two_E_two_B(self):
        assert checkout_solution.checkout("EEBB") == 110

    def test_four_E_two_B(self):
        assert checkout_solution.checkout("EEEEBB") == 160

    def test_one_F(self):
        assert checkout_solution.checkout("F") == 10

    def test_six_F(self):
        assert checkout_solution.checkout("FFFFFF") == 40

    def test_seven_F(self):
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_one_of_each_ABCDE(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_two_G(self):
        assert checkout_solution.checkout("GG") == 40

    def test_ten_H(self):
        assert checkout_solution.checkout("HHHHHHHHHH") == 80

    def test_five_H(self):
        assert checkout_solution.checkout("HHHHH") == 45

    def test_eleven_H(self):
        assert checkout_solution.checkout("HHHHHHHHHHH") == 90

    def test_one_I(self):
        assert checkout_solution.checkout("I") == 35

    def test_two_K(self):
        assert checkout_solution.checkout("KK") == 120

    def test_one_K(self):
        assert checkout_solution.checkout("K") == 70

    def test_four_N_one_M(self):
        assert checkout_solution.checkout("NNNNM") == 160

    def test_three_N(self):
        assert checkout_solution.checkout("NNNM") == 120

    def test_five_P(self):
        assert checkout_solution.checkout("PPPPP") == 200

    def test_three_Q(self):
        assert checkout_solution.checkout("QQQ") == 80

    def test_three_R_one_Q(self):
        assert checkout_solution.checkout("RRRQ") == 150

    def test_four_U(self):
        assert checkout_solution.checkout("UUUU") == 120 

    def test_two_V(self):
        assert checkout_solution.checkout("VV") == 90

    def test_three_V(self):
        assert checkout_solution.checkout("VVV") == 130

    def test_one_W(self):
        assert checkout_solution.checkout("W") == 20

    def test_one_S(self):
        assert checkout_solution.checkout("S") == 20

    def test_one_T(self):
        assert checkout_solution.checkout("T") == 20

    def test_one_X(self):
        assert checkout_solution.checkout("X") == 17

    def test_one_Y(self):
        assert checkout_solution.checkout("Y") == 20

    def test_one_Z(self):
        assert checkout_solution.checkout("Z") == 21
        
    def test_one_stx(self):
        assert checkout_solution.checkout("STX") == 45

    def test_not_recogised_sku(self):
        assert checkout_solution.checkout("-") == -1

    def test_no_sku(self):
        assert checkout_solution.checkout("") == 0
