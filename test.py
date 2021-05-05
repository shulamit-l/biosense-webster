from vending_machine import VendingMachineFactory


def main():
    print('Welcome to the vending machine!')

    # test creating a VendingMachineFactory
    vending_machine = VendingMachineFactory().createVendingMachine()

    # test purchase main function
    for i in range(10):
        assert (vending_machine.purchase('Soda', [5, 5, 5, 1]) == [10])

    # test change (the 10 coins finished, so the change return in 5 coins)
    assert (vending_machine.purchase('Soda', [5, 5, 5, 1]) == [5, 5])

    # test reset function
    vending_machine.reset()
    for i in range(10):
        assert (vending_machine.purchase('Soda', [5, 5, 5, 1]) == [10])

    # test refund function
    # ---can't refund---
    assert (vending_machine.refund('Coke') == (None, []))
    # -----refund-----
    assert (vending_machine.purchase('Coke', [5, 2]) == [])
    assert (vending_machine.refund('Coke') == ('Coke', [5, 2]))

    # trying to buy item that sold out
    for i in range(19):
        vending_machine.purchase('Coke', [5, 2])

    # trying to buy without enough money
    assert (vending_machine.purchase('Water', [1]) == [])

    # trying to buy with incorrect coins
    assert (vending_machine.purchase('Water', [3, 2]) == [])

    # trying to buy when the machine has'nt enough change to return
    vending_machine.reset()
    for i in range(11):
        vending_machine.purchase('Coke', [10, 5])


if __name__ == '__main__':
    main()
