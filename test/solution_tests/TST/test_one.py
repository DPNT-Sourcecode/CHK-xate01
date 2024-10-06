from solutions.CHK import checkout_solution


class TestSum():
    def test_one_A(self):
        assert checkout_solution.checkout("A") == 50

    def test_eight_A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 360

    def test_two_A(self):
        assert checkout_solution.checkout("AA") == 100

    def test_five_B(self):
        assert checkout_solution.checkout("BBBBB") == 120

    def test_not_recogised_sku(self):
        assert checkout_solution.checkout("E") == -1
        


