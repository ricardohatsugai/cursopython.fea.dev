import numpy as np
import time

star_time = time.time()

ativos_dev = np.random.randint(0, 1001, size=1_000_000_000)

end_time = time.time()

print(f"Result calculated in {(end_time - star_time)//60} minutes and {(end_time - star_time)%60} seconds")

print(F"O tamanho total do array é de {len(ativos_dev)}")