# [Project 3: EDA + Feature Engineering. Competition on Kaggle](https://github.com/errlwdfi/sf_data_science/tree/main/booking)

## Table of contents
[1. Preliminary data analysis](https://github.com/errlwdfi/sf_data_science/tree/main/booking/README.md#Preliminary_data_analysis)

[2. Feature engineering](https://github.com/errlwdfi/sf_data_science/tree/main/booking/README.md#Feature_engineering)

[3. Correlation analysis](https://github.com/errlwdfi/sf_data_science/tree/main/booking/README.md#Correlation_analysis)

[4. Feature selection](https://github.com/errlwdfi/sf_data_science/tree/main/booking/README.md#Feature_selection)

[5. Model creation](https://github.com/errlwdfi/sf_data_science/tree/main/booking/README.md#Model_creation)

**Goals of the project**:

* Generate new features out of existing ones.

* Select more important features for the model.

* Model creation and MAPE calculation.

## Data

Feature description:

* *hotel_address* - address of hotel.

* *review_date* - date, when reviewer has rated the hotel.

* *average_score* - average score of hotel, calculated regarding last review of the last year.

* *reviewer_nationality* - country of reviewer's inhabitance.

* *negative_review* - negative review that reviewer has rated the hotel.

* *review_total_negative_word_counts* - total number of words in the negative review.

* *positive_review* - positive review that reviewer has rated the hotel.

* *review_total_positive_word_counts* - total number of words in the positive review.

* *reviewer_score* - the score that reviewer has rated the hotel relying on his experience.

* *total_number_of_reviews_reviewer_has_given* - number of reviews that reviewer had placed.

* *total_number_of_reviews* - total number of reviews that hotel has.

* *tags* - tags that reviewer has given to the hotel.

* *days_since_review* - number of days between date of check and date of cleaning.

* *additional_number_of_scoring* - number of scores that hotel has, rated by reviewers who haven't placed the review.

* *lat* - hotel's latitude.

* *lng* - hotel's longitude.