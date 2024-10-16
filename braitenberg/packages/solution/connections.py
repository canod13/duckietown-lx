from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    
    res[200:300, 100:200] = 0.8
    res[300:400, 100:200] = 0.7
    res[400:500, 100:200] = 0.6

    res[200:300, 200:300] = 0.4
    res[300:400, 200:300] = 0.3
    res[400:500, 200:300] = 0.2

    res[200:300, 300:450] = 0.2
    res[300:400, 300:450] = 0.1
    res[400:500, 300:450] = 0.1
    
    #res[300:500, 0:100] = 0.1
    #
    # res[400:500, 0:100] = -0.2


    #3Versuch
    #res[300:500, 0:200] = 0.1
    #res[300:500, 200:400] = 0.3
    #res[300:500, 400:600] = 0.8
    #2 versuch
    #res[350:500, 500:650] = -1
    #res[400:450, 400:500] =-1
    #res[450:500, 200:500] =-1
    #res[300:350, 500:650] =-0.5
    #res[300:400, 450:500] =-0.5

    #res[450:500, 0:200] =1

    #res[0:250, 0:650] =1
    #res[250:500, 0:200] =1
    #res[250:500, 200:250] =0.5
    #res[250:300, 250:500] =0.5
    #res[300:500, 250:450] =-1
    #res[300:500, 450:500] =-0.5
    #res[250:500, 500:650] =1



    
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #res[200:300, 100:200] = 0.2
    #res[300:400, 100:200] = 0.1
    #res[400:500, 100:200] = 0.1

    res[200:300, 200:300] = 0.4
    res[300:400, 200:300] = 0.3
    res[400:500, 200:300] = 0.2

    res[200:300, 300:500] = 0.8
    res[300:400, 300:500] = 0.7
    res[400:500, 300:500] = 0.6

    #res[300:500, 550:650] = 0.1

    




    
    
    #3Versuch
    #res[300:500, 0:200] = 0.8
    #res[300:500, 200:400] = 0.4
    #res[300:500, 400:600] = 0.2

    #2 Versuch
    #res[300:350, 0:200] = -0.5
    #res[300:450, 150:200] =-0.5
    #res[350:500, 0:150] = -1
    #res[450:500, 150:450] = -1
    #res[450:500, 450:650] = 1
    #1 versuch
    #res[0:250, 0:650] = 1    
    #res[250:300, 0:250] = 0.5
    #res[300:450, 200:250] = 0.5
    #res[300:450, 250:650] = 1

    

    # ---
    return res
