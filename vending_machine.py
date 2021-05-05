from collections import defaultdict
from typing import List

from error_class import VendingMachineError


class VendingMachineFactory:
    def createVendingMachine(self):
        return VendingMachine()


class VendingMachine:
    items = {'Coke': 7, 'Soda': 6, 'Water': 5}

    # ------------------------Main functions------------------------#

    # initializing items _inventory and coins _inventory
    def __init__(self):
        self._inventory = {'Coke': 20, 'Soda': 20, 'Water': 20}
        self._coins = {10: 10, 5: 10, 2: 10, 1: 10}
        self._purchases = defaultdict(int)

    # purchase management function - input: an item and coins to pay output: coins as change
    def purchase(self, item: str, coins: List[int]) -> List[int]:
        if self.is_in_stock(item):
            if sum(coins) < self.items[item]:
                print(f"Price not full paid. Item costs {self.items[item]} NIS, only {sum(coins)} NIS was paid.")
                return []

            self._inventory[item] -= 1
            self._purchases[item] += 1
            change = self.change(item, coins)
            if change < 0:
                return []

            return self.get_change(change)

        print(f"We don't have {item} in the stock. Please buy another item")
        return []

    # function to allow refund by cancelling request
    def refund(self, item: str) -> [str, List[int]]:
        if self._purchases[item] == 0:
            print("The item you are trying to refund has not been purchased.")
            return None, []

        self._inventory[item] -= 1
        self._purchases[item] += 1
        return item, self.get_change(self.items[item])

    # function to allow reset operation for vending machine supplier
    def reset(self):
        self.__init__()

    # --------------------------End Main functions--------------------------#

    # --------------------------Auxiliary functions--------------------------#

    # function that returns true if the item is in stock
    def is_in_stock(self, item: str) -> bool:
        return item in self._inventory and self._inventory[item] > 0

    # function for paying an item. input: item, coins output: change
    def change(self, item: str, coins: List[int]) -> int:
        paid = 0
        try:
            for coin in coins:
                if coin not in self._coins:
                    raise VendingMachineError('This kind of coin is incorrect')

                paid += coin
                self._coins[coin] += 1

        except VendingMachineError as e:
            print(e.data)
            return -1

        return paid - self.items[item]

    # auxiliary function that converts change into coins
    def get_change(self, change: int) -> List[int]:
        change_to_return = []
        for coin in self._coins:
            num_of_coin = change // coin
            if num_of_coin <= self._coins[coin]:
                change -= coin * num_of_coin
                change_to_return += [coin] * num_of_coin
                self._coins[coin] -= num_of_coin

            else:
                change -= coin * self._coins[coin]
                change_to_return += [coin] * self._coins[coin]
                self._coins[coin] = 0
        try:
            if change:
                raise VendingMachineError('Not sufficient change in inventory... Initialize your machine')

        except VendingMachineError as e:
            print(e.data)
            return []

        return change_to_return
    # ----------------------------End Auxiliary functions----------------------------#
