# [HR agency data exploration](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration)

## Contents
[1. Data download and initial operations](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#Data_download_and_initial_operations)

[2. Visual data analysis](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#Visual_data_analysis)

[3. Statistical data analysis](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#Statistical_data_analysis)

[4. HR-agency key questions](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#HR-agency_key_questions)

[5. Additional explorations](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#Additional_explorations)

[5. Conclusion](https://github.com/errlwdfi/sf_data_science/tree/main/hr_exploration/README.md#Conclusion)

### Download data and initial operations

* Download data.

* Locate nan values and remove duplicates.

* Check the type of data in the columns.

* Locate non-informative features which won't participate in the exploration.

* Divide all features on numerical and categorical.

* Gather statistics on each feature.

### Visual data analysis

* Build histograms for numerical features.

* Determine number of records for categorical features and build visualizations.

* Create visualizations which show an impact of each feature on Data Scientist salary or salary in general.

* Give preliminary answers regarding visual analysis "Which features affect salary?".

### Statistical data analysis

* Build null and alternative hypothesises regarding business case.

* Choose stasistical test for each hypothesis and make preliminary checks if necessary.

### HR agency key questions

* Do Data Scientists have annual salary growth?

* What are Data Scientist and Data Engineer salaries in comparison in 2022?

* How do Data scientist salaries depend on company size?

* Is there a link between Data Scientist and Data Engineer job presence and company size?

### Additional explorations

* How do Data Scientist salaries depend on remote ratio?

* How do Data Scientist salaries depend on level of experience?

### Conclusion

* General conclusion on exploration

#### Data

All necessary data contained in */hr_exploration/data/ds_salaries.csv*.

**Data description**

* work_year - a year when salary was paid

* experience_level - work experience in specified job during year with possible values:

    * EN - Entry level, Junior

    * MI - Mid-level, Intermediate

    * SE - Senior level, Expert

    * EX - Executive level, Director

* employment_type - type of employment for this job:

    * PT - partial time

    * FT - full time

    * CT - contract

    * FL - freelance

* job_title - a job where person worked during a year

* salary - gross salary paid

* salary_currency - salary currency in ISO4217

* salary_in_usd - salary in USD

* employee_residence - employee's country of inhabitance in ISO3166

* remote_ratio - part of job performed remotely:

    * 0 - remote work is absent (less than 20%)

    * 50 - partially remote work

    * 100 - entirely remote work (more than 80%)

* company_location - employer's headquarters country in ISO3166

* company_size - average number of people who worked in company during a year:

    * S - less than 50 employees (small company)

    * M - from 50 to 250 employees (middle company)

    * L - more than 250 employees (large company)