from bayes_opt import BayesianOptimization


def bo_function(x1, x2):
    return -(4 - 2.1 * x1 ** 2 + ((x1 ** 4) / 4) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2)


pbounds = {'x1': (-3, 3), 'x2': (-2, 2)}

optimizer = BayesianOptimization(
    f=bo_function,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=3,
    n_iter=5,
)

print(optimizer.res)
