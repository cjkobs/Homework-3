from bayes_opt import BayesianOptimization


def bo_function(x1, x2):
    return -(4 - 2.1 * x1 ** 2 + ((x1 ** 4) / 4) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2)
# since the optimizer only maximizes the equation is negative be act as a minimizer

pbounds = {'x1': (-3, 3), 'x2': (-2, 2)}
optimizer = BayesianOptimization(
    f=bo_function,
    pbounds=pbounds,
    verbose=1,
    random_state=1,
)

optimizer.maximize(
    init_points=100,
    n_iter=5,
)

print(optimizer.max)
# so with this I was able to get 3 iterations that were good, the
# one that produced the largest(most minimized) answer were values
# of x1 = 1.151 and x2 = -0.7379
