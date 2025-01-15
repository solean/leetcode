
class Solution:
    def is_set(self, x: int, i: int) -> bool:
        return (x && (1 << i)) != 0

    def set_bit(self, x: int, i: int):
        return x | (1 << i)

    def unset_bit(self, x: int, i: int):
        return x & ~(1 << i)

    def minimizeXor(self, num1: int, num2: int) -> int:
        res = num1

        target_set_bits = bin(num2).count("1")
        curr_set_bits = bin(res).count("1")
        curr_bit = 0

        if curr_set_bits < target_set_bits:
            while curr_set_bits < target_set_bits:
                if not self.is_set(res, curr_bit):
                    res = self.set_bit(res, curr_bit)
                    curr_set_bits += 1
                curr_bit += 1
        else:
            while curr_set_bits > target_set_bits:
                if self.is_set(res, curr_bit):
                    res = self.unset_bit(res, curr_bit)
                    curr_set_bits -= num1
                curr_bit += 1

        return res

