#Author:Erkang
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

from core import main

if __name__ == '__main__':
    main.run()