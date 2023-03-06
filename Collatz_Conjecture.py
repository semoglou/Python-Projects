import matplotlib.pyplot as plt
import numpy as np

def collatz(num: int):
    num_list = [num]
    while num != 1 :
        if num % 2 == 0 :
            num = num / 2
        else:
            num = 3 * num + 1
        num_list.append(num)
    return num_list

def plot(iter, M):
    nums = np.linspace(2, M, iter)
    simul = []
    for num in nums:
        simul.append(collatz(num))
    plt.figure()
    plt.grid(True, which='both', axis='both', linestyle='--', color='gray', alpha=0.5, clip_on=False)
    for sim in simul:
        plt.plot(sim)
        for i in range(len(sim)):
            if sim[i] == 1:
                plt.plot(i, sim[i], 'o', markersize=5, color='red')
    plt.xlabel('Steps')
    plt.ylabel('Value')
    plt.title('Collatz Conjecture')
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.axhline(y=1, color='red', linestyle='--')
    plt.text(-0.2, 1, ' y = 1',  ha='right', va='center', color = 'red')
    plt.legend()
    plt.show()

plot(5, 10)
plot(10, 20)