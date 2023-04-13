import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import anderson_ksamp

chat_id = 298754188 # Ваш chat ID, не меняйте название переменной
def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.01
    res = anderson_ksamp([x, y])
    return res.pvalue < alpha # Ваш ответ, True или False

# def solution(x: np.array, y: np.array) -> bool:
#     p_value = anderson_ksamp([x, y]).pvalue 
#     alpha =  0.01
#     return p_value < alpha # Ваш ответ, True или False


# import pandas as pd
# import numpy as np
# from scipy.stats import anderson_ksamp

# chat_id = 298754188 # Ваш chat ID, не меняйте название переменной

# def solution(x: np.array, y: np.array) -> bool:
#     p_value = anderson_ksamp([x, y]).pvalue 
#     alpha = 0.01
#     return p_value < alpha # Ваш ответ, True или False




# def solution(x: np.array, y: np.array) -> bool:
#     return stats.cramervonmises_2samp(x, y).pvalue < 0.01 # Ваш ответ, True или False


# def solution(x: np.array, y: np.array) -> bool:
#     # Измените код этой функции
#     # Это будет вашим решением
#     # Не меняйте название функции и её аргументы
    
#     return anderson_ksamp([x, y]).pvalue < 0.01 # Ваш ответ, True или False
# def solution(x: np.array, y: np.array) -> bool:
#     res = stats.cramervonmises_2samp(x, y)
#     return res.pvalue < 0.01
