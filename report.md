The Resiliency of Gendered Associations about Leadership
================

Write-up by Salim Damerdji. Experiment conducted by Salim Damerdji, Roberto Lievana, and Aditya Jhanwar in 2019.

Introduction
============

In the US, women hold far fewer elite leadership positions than men. As of 2019, women account for 23.7% of US congresspersons; women hold only 6.6% of Fortune 500 CEO roles; and all 45 presidents in American history have been men[1] [2].

Unsurprisingly, leadership is associated with masculine-coded traits, such as being tough and commanding[3]. This association itself makes it harder for women to succeed in leadership positions[4] [5].

We ran an experiment to test the resiliency of these gendered associations. We find evidence that people will associate men with leadership all the same even after reading arguments that this association is harmful.

Methodology
===========

For our study, we recruited 48 volunteers, all of whom were STEM undergraduate or graduate students at UC Berkeley. Of our 48 volunteers, we had 24 self-identified female participants and 24 self-identified male participants. We asked participants in the treatment groups to read an argument about women leadership. Afterwards, each participant took an Implicit Association Test (IAT).

Treatment and Control Groups
----------------------------

Participants in the treatment groups read at least one of two arguments about women leadership.

Here is the pro-diversity argument: 'The University of California-Davis reported that the top 25 California companies with the highest percentage of women executives and board members saw a 74 percent higher return on assets and equity than the broader set of companies surveyed. This included companies such as William-Sonoma, Yahoo!, and Wells Fargo'[6].

Here is the anti-stereotype argument: 'We often think of leaders as dominant and ambitious-as embodying qualities that closely match the stereotype of men. On the other hand, the traits that make up the feminine stereotype (e.g., friendliness and sensitivity) are seen as less vital to leadership. These stereotypes result in women being evaluated less positively than men for leadership positions' [7][8].

We chose to study these two arguments because they are both archetypal: the pro-diversity argument is archetypal of a business-oriented argument that sells diversity as a route to organizational success; the second argument is, in contrast, archetypal of a social-justice-oriented argument that focuses on existing harmful stereotypes. Due to how common both of these types of arguments are, we chose to study them.

Experimental subjects received one of four treatment combinations: prior to taking the IAT, the subject either read nothing, read only the pro-diversity argument, read only the anti-stereotype argument, or read both.

Participants in the control group read nothing prior to taking the IAT.

Blocking
--------

We blocked by gender because we thought it a good bet that women internalized stereotypes about women differently than men internalized those stereotypes. Blocking by gender converts this unplanned systematic variability into planned variability, reducing noise and increasing statistical power. In the results section, we show this strategy was well-advised.

Power
-----

For logistical feasibility, we looked for the lowest sample size n that a) yields a balanced dataset and b) yields a power of at least 0.8.

We We used dry run data to estimate variance. At an alpha level of .05, percent significance level, equal variance of errors for both genders, and equal differential effects in the response of approximately 0.3 for the two levels of both the factors (which we decided on based upon calculated results from our data as well as hypothesizing about what the expected effects would be for the full-scale experiment). The plot below shows a single factor's resulting power curve, as a function of the number of individuals per treatment / block combination.

Measurement
-----------

We use an Implicit Association Test (IAT) to measure how strongly a subject associates each gender with leadership. An IAT offers an indirect measure the strength of a person's automatic association of two concepts. We implemented an IAT that is an abridged modification of Harvard's IAT. This tool has been well-studied by a large literature base that has thoroughly explored best practices for using an IAT [9].

One advantage is that unlike self-reporting, an IAT can measure unconscious associations or biases that people would not admit to having. The main shortcoming is that IAT scores are quite noisey. Despite this, there are few other available tools for measi Nevertheless, they're one of the few existing tools for social science research when it comes to taboo associations.

To measure the response, we gave participants an abbreviated IAT that consisted of five stages. In stage one, subjects press 'e' for male names and one key for female names. In stage two, it is similar, but for words that are categorized as related to leaders or supporters. In stage three, subjects press 'e' for male names or leader-related words, and 'i' for female names or supporter-related words. In stage four, subjects press 'e' for supporter-related words, and 'i' for leader-related words. In stage five, subjects press 'e' for male or supporter-related words, and 'i' for leader-related words or female names.

Our computer program tracks the delay between when a particular stimulus (e.g. the name 'Joe') is displayed on the center of the screen, and when the subject presses the appropriate key on the keyboard (e.g. 'e'). A screenshot of this setup is displayed in figure 2. This delay is measured in seconds and is rounded to the 5th decimal place. Thus, our measurements are accurate up to the the tenth of a millisecond.

Only the reaction times for stages 3 and 5 are relevant for the response. For those stages, we remove all reaction times longer than 10 seconds, as is standardly practiced in the IAT literature (Flint et al. 2013). These extremely slow responses are indications that participants became distracted or needed clarifications on the instructions. These outliers account for 0.72% of measured reaction times for stage 3 and 5. (That is 14 of 1920 measurements.)

From the remaining reaction times for stage 3 and 5, we subtract the average reaction times stage 3 from that of stage 5. We then divide this difference by the standard deviation for the reaction times across stage 3 and 5. We do this following the lead of experts who argue that "magnitudes of differences between experimental treatment means are often correlated with variability of the data from which the means are computed" (Greenwald et al. 2003). In our dataset, we found a large association of r = .54 between these the magnitude of differences and the variability of the data. This adjustment makes sense since we want our IAT score to be valid and reflect the signal of implicit bias, not the noise of variability in response times.

In short, our response of interest, the IAT score, is the mean reaction time for stage 3 minus the mean reaction time for stage 5, divided by the standard deviation of reaction times for those two stages. The basic intuition is that if subjects have quicker reaction times for stage 3 than for stage 5, then it's easier for the subject to mentally associate male names and leadership stimuli than female names and leadership stimuli. A large, positive IAT score indicates greater levels of implicit bias.

Protocol
--------

We performed complete randomization within each block. To assign treatments to subjects, we generated two lists where each of the four treatment combinations were listed four times. Both of these lists were randomly rearranged in R. We used the first list to assign treatment combinations to males as they volunteered to participate, and we used the second list for females.

As subjects arrived for the experiment, we used R to randomly assign them to one of the available computers. On that computer, we opened the IAT computer program we coded. Then we input the correct factor combination for that subject, without allowing the subject to see the treatments being assigned. We instructed subjects that all instructions were delivered by the computer program.

The computer program displayed the arguments, if any, that the subject was asked to read. If the subject was assigned to read both arguments, the program, in effect, flipped a coin to decide which to display first. Furthermore, for each stage of the IAT, we randomly order the possible stimuli to display on the screen. We perform these randomizations as insurance against unknown systematic bias, not because we suspected they would bias our results.

Validity
--------

Like many other analyses of complicated human responses, it's difficult to study implicit bias with a single measure. There are limitations to the response we have chosen.

First, IAT scores are merely proxies for implicit bias. Virtually all measures of human attitudes are based on indirect measures - including self-reporting or behavior - and our proxy is likewise indirect. Thus, it is a fair question whether high IAT scores are relevant indications of implicit bias.

A 2009 meta-study by Greenwald et al. found that, across 122 studies and 14,900 subjects, IAT scores positively correlated with "a wide range of criterion measures, from interracial friendliness and impression formation to anxious and shy behaviors, consumer choices, and voting," with an average pearson coefficient of .274. These findings held up across a plethora of different types of IATs, including IATs designed to test implicit gender bias.

A correlation coefficient of .274 is not high, but neither are correlation coefficients for other proxies for bias, including self-reporting (Greenwald et al. 2009). Moreover, IAT scores are more reliable than self-reporting for socially sensitive topics (Greenwald et al. 2009). That's because IAT scores can capture implicit biases that subjects may be unconscious of or unwilling to report on a survey.

Second, our results are limited in that they only measure the marginal effect of hearing the pro-diversity or anti-stereotype argument one time. It's entirely possible - indeed, likely - that our participants, UC Berkeley students, have heard arguments similar to the pro-diversity or anti-stereotype argument before. Thus, we are not able to study the effect of hearing these arguments repeatedly or, even, for the very first time.

Nevertheless, we believe it's still useful to study the marginal effect of these arguments. Given that arguments similar to the ones we study are fairly common, it's worth learning whether there are gains in gender diverse leadership to be made by repeating these arguments. Moreover, if we suppose that an argument's efficacy fades with time, then the marginal effect of these arguments can inform us about the argument's total effect.

Replicability
-------------

The response in question is fairly reliable. Although there is noise in a person's reaction times, this noise is reduced by taking the average of repeated measurements. So even if a person does not react with the exact same speed across repeated trials, their average reaction time should be approximately similar when they take the the test under the same conditions.

Helpfully, there is no measurement error because a computer can measure response times both accurately and precisely without the influence of human error. This helps improve the replicability of our response, reducing noise in our experiment.

Other Words of Caution
----------------------

First, we only measure short-term impacts on implicit bias. We had participants complete the IAT immediately after treatments were applied. Thus, our response could only measure impacts on implicit bias in the short-term. To many people, it is of greater interest whether these arguments impact implicit bias in the long-term. Due to practical limitations, we were not able to follow up with participants to study the effect of the treatment. Nevertheless, our results are still of interest in that we should not expect long-term effects unless there are short-term effects.

Second, our experiment does not prove there exists implicit bias against female leadership. For all we can show, the IAT scores are inflated because participants struggled to adapt to using a new key to press for categorizing gendered names. To rectify this limitation, we would had to have randomized the stages of our IAT test such that stages 2 and 3 could be ordered after stages 4 and 5. Nevertheless, our experiment tests whether our treatments affect the relative levels of implicit bias, though we make no claims about the absolute levels of that bias.

Third, UC Berkeley STEM students are not representative of the general population in America. While our motivation is related to larger trends in America, we of course also care about how Berkeley STEM students respond to the arguments we have studied. Furthermore, our experiment can help inform a larger project whereby other researchers study other subsets of the general population for the same phenomena, and a literature review could confirm or deny whether our findings hold generally.

Fourth, the arguments we study are merely archetypes of the types of arguments we are interested in. However, our results cannot be quickly generalized to other arguments that are substantially different. For example, if we find a significant effect for the prodiversity argument, it may be due to the tone, the use of empirics, or the framing of the argument. Our study is not able to exactly discern these differences. Nevertheless, it is still a worthwhile to see whether this argument has a significant effect on implicit bias because it serves as an indication about the prospects of other similar arguments.

Data Table
----------

In the data table below, subject\_id is a unique identifier for each participant, time refers to when the test was started, 'cp' denotes which of three computers the subject took the IAT on, 'prodiversity' is a column of booleans that indicate whether the subject read the prodiversity argument, 'anti-stereotype' is likewise a column of booleans that indicate whether the subject read the anti-stereotype argument, and 'iat' denotes the subject's IAT score.

Results
=======

Checking Model Assumptions
--------------------------

Before conducting any analysis or exploring the data we first wanted to determine if the assumptions of a parametric model are met. Several assumptions for such a model we wanted to test were normally distributed and homoskedastic errors as well as constant effects and additivity.

We created two interaction plots to better understand if an additive or interaction model would best suit our observed data. Figure 4 is a 2-way interaction plot that highlights the interaction effects of the factors of interest, whereas figure 5 is a 3-way interaction plot that accounts for the blocks of male and female genders. For added clarity in analysis, we included standard error bars to account for variability in the data to better gauge the plot.

As we can see in both the 2-way and 3-way interaction plots, the 'lines' do not appear to be parallel. This was also the case for additional 2-way interaction models that were produced as well. However, when accounting for the variability of the data as displayed by the standard error bars we noticed that we did not have enough data to accurately determine whether there is in fact some sort of interaction prevalent. Hence, after careful analysis and observation of the plots we reasoned that we would assume an additive model as the noise in the 'lines' could perhaps be explained by the variability itself rather than through an interaction term.

We implemented a fitted versus residual plot as it serves as a robust method in examining several model assumptions such as constant variance and zero-mean errors. From observing the fitted versus residual plot that was produced given our data we found the errors to be fairly homoskedastic, which argued that the aforementioned assumptions were in fact met. In our judgment, this held true within blocks as well; although variance decreases among large fitted values for males, this coincides with fewer observations, so it is not strong evidence that any assumptions of ANOVA are violated.

We also wanted to confirm that the errors are normally distributed as per another important assumption of the model and ANOVA analysis. We produced a Q-Qplot as it would best indicate a violation in the normality assumption.

The results produced showed that the errors are distributed fairly normally albeit with some noise present. However, there does not seem to be any outliers and seems like a satisfactory match for the assumption. We did try using transformations on the data to form much more stringently normally distributed data, which would lead to that much more of an effective and representative model, but ultimately were unsuccessful of finding any such transformation and we felt the results produced were satisfactory.

Independence Assumption
-----------------------

In addition to analyzing the standard model assumptions we also took a look at other aspects of the data for sources of bias and variability. Our experiment took place mainly during 10 AM - 2 PM, which was the assigned time for running our experiment. Since we were unable to recruit all subjects necessary for the experiment during the time, we gathered the remaining subjects necessary afterwards outside of lab hours. We were concerned of possibility of the times subjects performed the experiment having some effect with the response times. We also were concerned with which computer the IAT was taken on. Fortunately, neither plot suggests we violate the independence of errors assumption since the residuals all look quite similar.

Parallel Dot Chart
------------------

As a means of viewing the entire data in a concise method, we produced a parallel dot chart. We observe in the figure below that subjects who identified as female seem to have higher response times in general compared to those who were male. This reaffirms the presence of variability in the responses for the different genders and that blocking was in fact an appropriate choice for our design of the experiment.

ANOVA
Our model is

yijkl=i+j+k+ijkl

Where i = 1, 2 and i is the Factor A "pro-diversity", j = 1, 2 and j is the Blocking Factor "gender" , k = 1, 2 and k represents Factor B "anti-stereotype"; and l = 1 .. 48 and ijkl are the error terms. We assume the ijkl ~ N ( 0,2)

In addition we considered gender to be a fixed effect rather than a random effect. Gender is constant across individuals over time. To make it clear, any effects of being a male will not change over time. This means that gender has a fixed effect.

The only significant effect in our analysis corresponds to the blocking factor "gender" \[F(1, 44) = 6.026, P&lt;0.05\] from Table 1. Most of the variance that was previously attributed to residuals has now been partitioned to the block effect. This was going to help us explain the differences between the different factors more profoundly, however, the two factors of interest showed minimal effect \[F(1, 44) = 0.0072, P&gt;0.05\] and \[F(1, 44) = 0.0315 , P&gt;0.05\] from Table 1.

Here is a table of estimated effects:

Effects of Blocking
-------------------

The blocking strategy in the experiment proved to be successful. Our suspicion, that baseline rates of implicit bias vary by gender was correct. The large variation between gender/blocks is clear with a F-ratio \[F(1, 44) = 6.026, P&lt;0.05\] from our ANOVA analysis in Table 1. Blocking by gender enabled us to convert this unplanned systematic variability into planned variability which reduced the noise in our experiment and increased the power of our experiment. Any cause due to a difference in sex is taken into consideration by using gender as a blocking factor.

Contrast
--------

Let's examine the contrast for whether there was a difference in response between the control group and the treatment groups. This corresponds to the coefficient vector of (-3, -3, 1, 1, 1, 1, 1, 1), where first two entries of the coefficient vector correspond to the two control groups (one per gender), and the last four entries correspond to the remaining treatment / block combinations. Our null hypothesis is that there is no difference between the control groups and treatment groups. Our alternative hypothesis is that there is some difference.

The unbiased estimate of this linear combination is 0.0571. We use MS residuals as an estimate for error, by multiplying it by the square root of ??wi/ni., which is 3.8333.

Thus, our t-statistic is .0571 / sqrt(.1691\*3.8333). This t-statistic has a p-value of 0.9445. Clearly, this is not statistically significant. So, we fail to reject the null that there is no difference between the control and treatment groups.

Results and Ideas For Future Research
-------------------------------------

In short, gender appears to be predictive of IAT scores, but the arguments displayed did not have an effect. This is an interesting finding that we found surprising. It would be natural to assume that these arguments were suggestive enough to reduce implicit bias. Perhaps implicit bias is resilient, or these arguments were unconvincing, or some other possibility could explain this result.

Due to this uncertainty, we believe this was merely a starting point for the many possibilities of these sorts experiment. An issue that was touched on earlier is that our experiment was limited to STEM students at UC Berkeley, which does not necessarily generalize well to the standard characteristics of males and females in the larger scope of the population. An adaption of this experiment in which one would source subjects more openly and not within a single cluster could lead to much more robust results. In addition, our main factors only accounted for different types of text whereas other forms of media could have different implications and effects on the response. With further resources and newfound experience in designing and analyzing an experiment, we suspect that we or even other individuals with more domain knowledge on the subject of the experiment could further expand on the what the motivation behind the experiment is.

References
----------

Dasgupta, Nilanjana, and Anthony G. Greenwald. "On the Malleability of Automatic Attitudes: Combating Automatic Prejudice with Images of Admired and Disliked Individuals." Journal of Personality and Social Psychology, vol. 81, no. 5, 2001, pp. 800-814., <doi:10.1037//0022-3514.81.5.800>. Flint, Stuart W., et al. "Counter-Conditioning as an Intervention to Modify Anti-Fat Attitudes." Health Psychology Research, vol. 1, no. 2, 2013, p. 24., <doi:10.4081/hpr.2013.738>. Harvard, Project Implicit. <https://implicit.harvard.edu/implicit/selectatest.html> Page-Gould, Elizabeth, and Amanda Sharples. How to Avoid Picking Up Prejudice from the Media. Greater Good, 7 Sept. 2016, greatergood.berkeley.edu/article/item/how\_to\_avoid\_picking\_up\_prejudice\_from\_media. Thomas, Breda, et al. Can Female Role Models Reduce the Gender Gap in Science? Evidence from Classroom Interventions in French High Schools. Working Paper. 2018.

Article on how to compute IAT score: <https://faculty.washington.edu/agg/pdf/GB&N.JPSP.2003.pdf>

Article on external validity: <http://www.people.fas.harvard.edu/~banaji/research/publications/articles/2009_Greenwald_JPSP.pdf>

Article on Women Leadership Gap <https://www.americanprogress.org/issues/women/reports/2018/11/20/461273/womens-leadership-gap-2/>

Article Times

<http://time.com/4064665/women-college-degree/>

[1] Mejia, Zameena. Just 24 Female CEOs Lead the Companies on the 2018 Fortune 500-Fewer than Last Year. CNBC, 21 May 2018, www.cnbc.com/2018/05/21/2018s-fortune-500-companies-have-just-24-female-ceos.html.

[2] DeSilver, Drew. "A Record Number of Women Will Be Serving in the New Congress." Pew Research Center, Pew Research Center, 18 Dec. 2018, www.pewresearch.org/fact-tank/2018/12/18/record-number-women-in-congress/.

[3] Zheng, Wei, et al. "How Women Manage the Gendered Norms of Leadership." Harvard Business Review, 28 Nov. 2018, hbr.org/2018/11/how-women-manage-the-gendered-norms-of-leadership.

[4] Zheng, Wei, et al. "How Women Manage the Gendered Norms of Leadership." Harvard Business Review, 28 Nov. 2018, hbr.org/2018/11/how-women-manage-the-gendered-norms-of-leadership.

[5] Eagly, Alice H., et al. "Gender and the Effectiveness of Leaders: A Meta-Analysis." Psychological Bulletin, vol. 117, no. 1, 1 Jan. 1995, pp. 125-145., <doi:10.1037//0033-2909.117.1.125>.

[6] Lemke, Tim. "Do Companies With Female Executives Perform Better?" The Balance, The Balance, 1 Feb. 2019, www.thebalance.com/do-companies-with-female-executives-perform-better-4586443.

[7] Prime, Jeanine. Women "Take Care," Men "Take Charge." Edited by Andrea Juncos and Kara Patterson, Catalyst, 2005, pp. 1-38, Women "Take Care," Men "Take Charge."

[8] Although neither argument *explicitly* says that diversity is good or stereotypes are bad, it's convienent to use these descriptions as shorthand.

[9] A Google Scholar search yields over 26,500 results for articles containing the exact wording: 'implicit association test.'