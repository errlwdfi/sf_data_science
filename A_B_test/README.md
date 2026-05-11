# [A/B test](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test)

## Table of contents
[1. Data exploration](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test/README.md#data-exploration)

[2. Primary data analysis](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test/README.md#primary-data-analysis)

[3. Cumulative metrics](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test/README.md#cumulative-metrics)

[4. Statistical tests](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test/README.md#statistical-tests)

[5. Conclusion](https://github.com/errlwdfi/sf_data_science/tree/main/A_B_test/README.md#conclusion)

**Goals of the project**:

* Explore the data. Find out characteristics of its features.

* Check test duration in both samples. Remove any shared users from data.

* Group data. Visualize key features of the data.

* Generate cumulative features. Check whether they stabilize.

* Conduct statistical tests.

* Create confidence intervals.

* Make conclusion.

## Data

Feature description:

* *user_id* - unique number of user.

* *date* - date, when visit/purchase has been performed.

* *group* - sample type (A or B).

* *purchase* - binary variable indicating whether a purchase has been performed.

* *price* - purchase value.

## Useful formulas

*Confidence interval for proportion*:

$$p = \mu = X_p \pm z_{crit} \cdot \sqrt{\frac{X_p (1 - X_p)}{n}}$$,

$$z_{crit} \in N(0, 1)$$,

where $\mu$ - true mean value, $X_p$ - sample mean, $n$ - sample size, $N(0, 1)$ - normal distribution with zero mean value and stardard deviation of $1$.

*Confidence interval for proportion difference*:

$$\Delta p = \Delta X_p \pm z_{crit} \cdot \sqrt{\frac{X_{p_a}(1 - X_{p_a})}{n_a} + \frac{X_{p_b}(1 - X_{p_b})}{n_b}}$$, 

$$z_{crit} \in N(0, 1)$$,

where $\Delta X_p = X_{p_b} - X_{p_a}$, $X_{p_a}$ - sample A mean, $X_{p_b}$ - sample B mean, $n_a$ - sample A size, $n_b$ - sample B size.

*Confidence interval when true standard deviation is unknown*:

$$\mu = X_{mean} \pm t_{crit} \cdot \frac{X_{std}}{\sqrt{n}}$$,

$$t_{crit} = t_{\frac{1-\gamma}{2}} \in T(n-1)$$,

where $X_{mean}$ - sample mean, $\gamma$ - confidence level, $X_{std}$ - sample standard deviation, $n$ - sample size, $T(n - 1)$ - T-distribution with $n - 1$ degrees of freedom.