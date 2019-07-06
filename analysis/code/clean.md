Clean Data
================
Salim Damerdji

#### Load Data

After loading the data and removing incomplete observations, to each dataframe I add a column that indicates which computer the subject took the experiment on.

``` r
get_iat_tibble <- function(file_name, cp_num){
  df <- read.csv(file_name) %>%
    as_tibble() %>%
    select_if(function(x) !(all(is.na(x)) | all(x==""))) %>%
    na.omit() %>%
    mutate(cp = cp_num)
  return(df)
}

aj1 <- get_iat_tibble('../data/raw/RESULTS_aj_1.csv', 1)
aj2 <- get_iat_tibble('../data/raw/RESULTS_aj_2.csv', 1)
rb1 <- get_iat_tibble('../data/raw/RESULTS_rb_1.csv', 2)
rb2 <- get_iat_tibble('../data/raw/RESULTS_rb_2.csv', 2)
rb3 <- get_iat_tibble('../data/raw/RESULTS_rb_3.csv', 2)
sd1 <- get_iat_tibble('../data/raw/RESULTS_sd_1.csv', 3)
sd2 <- get_iat_tibble('../data/raw/RESULTS_sd_2.csv', 3)
```

#### Merge Data

``` r
# Rename columns so they can be merged
sd1 <- rename_at(sd1, vars(contains('X')), funs(sub('X', 'stage', .)))
listDf = list(aj1, aj2, rb1, rb2, rb3, sd1, sd2)
for (i in seq_along(listDf)){
  setnames(listDf[[i]], colnames(sd1))
}

# Merge
merged_unbalanced <- rbind(aj1,aj2,rb1,rb2,rb3,sd1,sd2) %>%
  mutate(time = chron(times = time))
```

#### Balance the dataset

We have an imbalanced dataset since not all treatment/block combinations are equally represented in our dataset. This can be seen below:

``` r
merged_unbalanced %>%
  group_by(gender, factor) %>%
  count()
```

    ## # A tibble: 8 x 3
    ## # Groups:   gender, factor [8]
    ##   gender factor     n
    ##   <fct>   <int> <int>
    ## 1 Female      1     6
    ## 2 Female      2     8
    ## 3 Female      3     6
    ## 4 Female      4     7
    ## 5 Male        1     6
    ## 6 Male        2     7
    ## 7 Male        3     7
    ## 8 Male        4     6

We can balance this dataset by removing extraneous observations. I can do this by taking only 6 subjects per treatment/block combination. If a treatment/block combination has k subjects, where k&gt;6, I remove the k-6 subjects who took the experiment **last.**

Someone else might prefer to remove observations according to some metric that would improve power. For example, they could remove the noisiest subjects. But I worry this approach would introduce bias. It's more neutral to merely removing the subjects who took the experiment last.

``` r
balanced <- merged_unbalanced %>% 
  group_by(factor, gender) %>%
  top_n(n=6, wt=time) %>%
  ungroup() %>%
  arrange(time) %>%
  mutate(subject_id = 1:48)
```

#### Tidy the Data

Transform dataframe so every row is an observation (a reaction time) and every column is a variable.

``` r
# Tidy the dataset, in the Hadley Wickham sense of 'tidy', not the KonMari sense
(tidy_balanced <- balanced %>%
  select(subject_id, cp, time, factor, gender, everything()) %>%
  gather(key = 'trial', value = 'response', 6:75))
```

    ## # A tibble: 3,360 x 7
    ##    subject_id    cp time        factor gender trial    response
    ##         <int> <dbl> <S3: times>  <int> <fct>  <chr>       <dbl>
    ##  1          1     2 10:31:06         3 Male   stage1_0     1.94
    ##  2          2     2 10:34:22         3 Female stage1_0     4.45
    ##  3          3     2 10:45:03         2 Female stage1_0     1.88
    ##  4          4     2 10:48:56         4 Female stage1_0    28.4 
    ##  5          5     1 10:52:27         1 Male   stage1_0     1.42
    ##  6          6     3 11:42:21         4 Male   stage1_0     1.83
    ##  7          7     3 12:09:09         4 Female stage1_0     4.41
    ##  8          8     3 12:15:50         3 Male   stage1_0     1.67
    ##  9          9     1 12:17:19         4 Male   stage1_0     6.29
    ## 10         10     3 12:18:55         1 Female stage1_0     1.51
    ## # ... with 3,350 more rows

#### Outliers

##### Exploration of Outliers

Greenwald et al's meta-analysis recommends IAT studies defines outliers as reaction times that last longer than 10 seconds.

``` r
tidy_balanced %>%
  filter(grepl("stage[3,5]",trial)) %>% # only reaction times from stages 3 and 5
  group_by(subject_id) %>% # count towards the IAT score
  filter(response > 10)
```

    ## # A tibble: 14 x 7
    ## # Groups:   subject_id [10]
    ##    subject_id    cp time        factor gender trial     response
    ##         <int> <dbl> <S3: times>  <int> <fct>  <chr>        <dbl>
    ##  1          9     1 12:17:19         4 Male   stage3_0      11.3
    ##  2         31     2 13:15:00         3 Female stage3_0      11.4
    ##  3         42     2 15:26:03         1 Female stage3_0      10.0
    ##  4         22     3 12:42:25         2 Female stage3_1      10.3
    ##  5         25     1 12:47:01         4 Male   stage3_1      11.3
    ##  6         39     2 15:10:15         1 Female stage3_1      10.8
    ##  7         31     2 13:15:00         3 Female stage3_9      42.8
    ##  8         18     1 12:32:44         1 Male   stage3_15     21.4
    ##  9         18     1 12:32:44         1 Male   stage3_16     10.9
    ## 10         31     2 13:15:00         3 Female stage3_19     30.8
    ## 11         14     1 12:26:50         4 Male   stage5_0      10.1
    ## 12         20     3 12:37:44         1 Male   stage5_0      20.2
    ## 13         25     1 12:47:01         4 Male   stage5_3      11.3
    ## 14         47     1 22:33:35         2 Male   stage5_4      12.1

By this metric, there are 14 outlier response times to remove. These reaction times are so slow they indicate the subject was significantly distracted, attempted to get clarification on instructions, or did something else anamolous. Outlier removal filters out this noise.

``` r
tidy_balanced %>%
  filter(grepl("stage[3,5]",trial)) %>%
  nrow()
```

    ## [1] 1920

Since there are 1920 total observations, these outliers account for 0.7% of all observations.

Greenwald et al also recommends removing data for participants where more than 10% of their reaction times were under 300 milliseconds. This strategy helps address cases where participants are answering so quickly they could not *really* be reading the stimuli words. We don't have any subjects who did this:

``` r
tidy_balanced %>%
  group_by(subject_id) %>%
  filter(response < .3) %>%
  count()
```

    ## # A tibble: 6 x 2
    ## # Groups:   subject_id [6]
    ##   subject_id     n
    ##        <int> <int>
    ## 1          4     1
    ## 2          5     1
    ## 3          9     1
    ## 4         11     1
    ## 5         23     2
    ## 6         38     2

No subject reacted that quickly more than twice, which is far below the 10% threshold.

##### Remove Outliers

``` r
no_outliers <- tidy_balanced %>%
  group_by(subject_id) %>%
  filter(response < 10)
```

#### Create Final Dataframe

Ultimately, our analysis is only of how treatment affects the IAT scores. We only care about the IAT scores's summary of the reaction times, not the reaction times themselves. So, for our analysis, we should retidy data so rows are particpants, rather than reaction times. And we'll add a feature that tells us a subject's IAT score. Our scoring metric is justified further in the write-up. In short, the score is the difference of mean response times for stage 3 & 5, divided by standard deviation of response times across both stages for that person.

``` r
# Remove stages 1,2,4
df <- no_outliers %>%
  filter(grepl("stage[3,5]",trial)) %>%
  arrange(subject_id)

# Determine each subject's mean response time for
# stage 3 (male_leader) and 5 (female_leader)
(mean_response <- df %>% 
  mutate(is_stage_3 = grepl("stage3",trial)) %>%
  group_by(subject_id, cp, time, factor, gender, is_stage_3) %>%
  summarise(mean = mean(response)) %>%
  spread(key = is_stage_3, value = mean) %>%
  rename(stage3_mean = 'TRUE', stage5_mean = 'FALSE'))
```

    ## # A tibble: 48 x 7
    ## # Groups:   subject_id, cp, time, factor, gender [48]
    ##    subject_id    cp time        factor gender stage5_mean stage3_mean
    ##         <int> <dbl> <S3: times>  <int> <fct>        <dbl>       <dbl>
    ##  1          1     2 10:31:06         3 Male         1.35        1.23 
    ##  2          2     2 10:34:22         3 Female       0.903       1.02 
    ##  3          3     2 10:45:03         2 Female       2.11        1.65 
    ##  4          4     2 10:48:56         4 Female       2.33        1.25 
    ##  5          5     1 10:52:27         1 Male         1.22        1.06 
    ##  6          6     3 11:42:21         4 Male         1.03        1.00 
    ##  7          7     3 12:09:09         4 Female       0.760       1.04 
    ##  8          8     3 12:15:50         3 Male         1.27        0.876
    ##  9          9     1 12:17:19         4 Male         2.12        1.05 
    ## 10         10     3 12:18:55         1 Female       1.50        1.42 
    ## # ... with 38 more rows

We use the mean\_response dataframe to compute IAT scores

``` r
(iat_df <- df %>% 
  group_by(subject_id) %>%
  summarise(sd = sd(response)) %>%
  right_join(mean_response) %>%
  mutate(diff = (stage5_mean - stage3_mean)) %>%
  mutate(iat_d = diff/sd) %>%
  select(-sd, sd))
```

    ## Joining, by = "subject_id"

    ## # A tibble: 48 x 10
    ##    subject_id    cp time  factor gender stage5_mean stage3_mean    diff
    ##         <int> <dbl> <S3:>  <int> <fct>        <dbl>       <dbl>   <dbl>
    ##  1          1     2 10:3~      3 Male         1.35        1.23   0.117 
    ##  2          2     2 10:3~      3 Female       0.903       1.02  -0.122 
    ##  3          3     2 10:4~      2 Female       2.11        1.65   0.459 
    ##  4          4     2 10:4~      4 Female       2.33        1.25   1.08  
    ##  5          5     1 10:5~      1 Male         1.22        1.06   0.155 
    ##  6          6     3 11:4~      4 Male         1.03        1.00   0.0292
    ##  7          7     3 12:0~      4 Female       0.760       1.04  -0.280 
    ##  8          8     3 12:1~      3 Male         1.27        0.876  0.394 
    ##  9          9     1 12:1~      4 Male         2.12        1.05   1.07  
    ## 10         10     3 12:1~      1 Female       1.50        1.42   0.0742
    ## # ... with 38 more rows, and 2 more variables: iat_d <dbl>, sd <dbl>

R's ANOVA functions are also easier to use if we add a binary feature for each treatment.

``` r
iat_df <- iat_df %>%
  mutate(prodiversity = (factor %in% c(2,4))) %>%
  mutate(antistereotype = (factor %in% c(3,4)))
```

#### Write Out CSV

``` r
write.csv(iat_df, file = '../data/clean/iat_scores.csv')
```
