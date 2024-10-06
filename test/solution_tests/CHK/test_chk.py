from solutions.CHK import checkout_solution


class TestSum():
    def test_one_A(self):
        assert checkout_solution.checkout("A") == 50

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
        
    def test_one_of_each(self):
        assert checkout_solution.checkout("ABCDE") == 155

    def test_not_recogised_sku(self):
        assert checkout_solution.checkout("-") == -1
        
    def test_no_sku(self):
        assert checkout_solution.checkout("") == 0

