# Bayesian Net Markov Chain Monte Carlo

## Consultation

Grant Sparks and I collaboratively created the Conditional Probability Tables by discussing mathematical formulas, and then entering these formulas into a spreadsheet. From this sheet we calculated and entered the Conditional Probability values into the submitted tables and code. The values were checked against values submitted in the discussion threads for week 12 and 13; the values for P(A | B?,C?,D?) were checked against Kshitija Taywade's posted in week 12 and found to be correct, the values for P(D | A?,C?,E?) were obtained from Kshitija Taywade's post in week 13. All math involved can be found in the appropriate sheets in `CS 463 Bayesian Probabilities.xlsx`, (as Excel/Google Sheets formulas) which was used to calculate each CPT value.

## Process Description

I began writing formulas for calculating the specific conditional probabilities for each value, A, B, D, E. The formulas that were easy (E, A) could then be filled in on the CPT. The formulas that were harder required consulting with a classmate (Grant Sparks, see above section) and reading the class discussion threads. Both created a full understanding of the formulas involved for the more difficult Markov Blankets. With these probabilities I wrote psuedo code that detailed the algorithm; 
* randomly assing values to A, B, D, E
* check each assignment by comparing the current assignment of variables to the CPT, generating a new random variable, if that variable is in the range specified by the CPT for this assignment assign the checked variable `True`, otherwise `False`
* increment the counter if `B` == `True` for this run
* if this is a 100th run, print the counter / number of iterations so far
* repeat, keeping the current assignment of variables as at the end of the loop
I wrote the code, debugged, dumped the code output to files, charted the output.

## Running Code

`python run.py` will run one run of 10,000 iterations with a random intial assignment, printed before the ratio data. Ratios are printed every 100 iterations. Code is written and was run using Python 3.

## Conditional Probability Tables and Graphs

Conditional Probability Tables can be found in `data.pdf`, along with the raw ratio data for the 5 runs used to generate the graphs.

## Patterns

Clearly evidenced by the graph, the algorithm will move towards a 0.59 of B=T to iterations completed. Starting either high, (>0.65) or low (<0.56) the ratio of B=T will still approach the same value, 0.59 (within around a margin of about .01, higher numbers of iterations will produce a closer spread).

## Lessons Learned

Less of a lesson learned than a lesson correctly applied, but spending time obtaining a deeper conceptual understanding of the material (how Bayesian Nets operated, ignoring algorithmic implementations) helped greatly. Grant and I spent the majority of our time writing math by hand and comparing results of the CPT, and found that when we split up to actually write code it happened almost instantly. The psuedo-code I wrote was almost directly entered into my editor and produced a workable result. Additionally, this understanding of what I was actually trying to obtain through code writing meant that the gaps that did exist in my understanding (initially failing to correctly understand the P(D|...) equations) were easily "stubbed" into working code and returned to later, with only minor implications on the final answer rather than structural problems in the algorithm.

I also learned how Bayesian Nets actually worked, as it always increases your understanding from conceptually lecture-based workings to actual implementations. The math behind them is now solidified in my mind, whereas before there were gaps.
