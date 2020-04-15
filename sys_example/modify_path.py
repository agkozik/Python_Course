import sys
import os.path

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(current_path)
module_path = os.path.join(parent_path, 'essential')
sys.path.append(module_path)

import modfibonacci

print(modfibonacci.n_fibonacci(10))
