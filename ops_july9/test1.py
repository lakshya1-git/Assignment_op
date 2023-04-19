class bank:
    def test(self):
        print('Totoal t')

    def transaction(self):
        print("Total traction value")
    def account_opeining(self):
        print('this will show your despoinsitedamount')
class Hdfc_bank(bank):
    def test(slef):
        print("test 2l")
    def hdfc_to_icici(self):
        print("this will show you all the trqaction happedn to icici through dffc")
class ineuron_bank:
        def account_status_icici(self):
            print("print a account staqtuts in isisi")
class icici(Hdfc_bank, bank, ineuron_bank):
    def c_icici(self):
        print("this is all traction  happeen to icici through bank")
obj = icici()
obj.transaction()
obj.account_opeining()
obj.test()
obj.hdfc_to_icici()
obj.account_opeining()
