import numpy as np
import matplotlib.pyplot as plt
from zplane import zplane

#Zero = Z^2 + 1.5Z + 2
#Polo = Z^2
if __name__ == "__main__":
    num = np.array([1, 1.5, 2])
    dem = np.array([1, 0, 0])

    z = np.roots(num)
    p = np.roots(dem)

    print("Zeros: ", z)
    print("Polos: ", p)

    zplane(num, dem)

