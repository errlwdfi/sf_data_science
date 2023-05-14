import numpy as np

def random_predict(number:int=1) -> int:
    """Predict a number randomly

    Args:
        number (int, optional): Made up number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)


def score_game(random_predict) -> int:
    """How many attempts does it take in average to predict a number in 1000 rounds

    Args:
        random_predict (_type_): prediction function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f'Your algorithm predicts a number in average in: {score} attempts')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)