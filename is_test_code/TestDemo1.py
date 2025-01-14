class TestDemo1:
    def test_method1(self):
        assert 1 == 1

    def test_method2(self):
        assert 2 == 2

    def test_method3(self):
        assert 3 == 3
    
    def test_method4(self):
        assert 4 == 4
    
    def test_method5(self):
        assert 5 == 5
    
    def print_result(self):
        print("All test cases passed")


if __name__ == '__main__':
    test_obj = TestDemo1()
    test_obj.test_method1()
    test_obj.test_method2()
    test_obj.test_method3()
    test_obj.test_method4()
    test_obj.test_method5()
    test_obj.print_result()