class Solution:
	def reverseBits(self, n: int) -> int:
		binary = list(bin(n))[2:] # we don't need 0b
		remainder = ["0"]
		zerosNeeded = 32 - len(binary)
		newBinary = binary[::-1] + remainder * zerosNeeded # add the missing zeros

		return int("".join(newBinary), 2)
        