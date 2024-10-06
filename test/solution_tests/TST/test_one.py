from solutions.CHK import checkout_solution


class TestSum():
    def test_one(self):
        assert checkout_solution.checkout("A") == 1

    def test_not_recogised_sku(self):
        assert checkout_solution.checkout("E") == -1
        
    def test_eight_A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 360

