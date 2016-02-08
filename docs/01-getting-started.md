# Getting Started

## What is Machine Learning?

- Artificial Intelligence?
- Modeling (Regression)?
- Prediction?
- Statistics?
- Data Science?

In some ways, machine learning is automated data science. But machine learning requires a lot of human learning and understanding (otherwise you wouldn't be here). So maybe it's more like what a software developer would do if she were given a data science problem. And data science is just using data to create representations or abstractions of data. Often these representations are useful for performing prediction. Predicting the future is what humans spend their lives learning how to do. It's why children perform "experiments" by pushing their food of the table and onto the floor. They are testing their "hypothesis" that a caregiver will put it back on the table or clean up the mess. They are also testing their hypothesis that the food won't just disappear, or transform into something different (like icecream), or become unedible.

Just like a child, machines have to perform experiments  repeatedly with the same starting conditions (inputs) and also with a large variety of inputs, before they'll get "bored" and be certain that they know how to predict the future for new examples.

But one thing that humans learn how to do (in young adulthood) that machines are still very bad at is inferring general concepts from only one or two examples. This is an area of active research. Keep this in mind when you are asked to apply machine learning to a new problem. During this course you will get a feel for where current machine learning technology works well and where it does not, this is "the state of the art." So when you try to push the limits, you'll know when to get creative or when to reuse someone else's approach.

## Machine Intelligence is Everywhere

Machine Learning snuck up on us and is now a part of nearly everything we do. Children spend most of their waking hours looking at a computer screen of some sort. Adults spend a little less time, but still much of their lives. Those screens are windows into a variety of machine learning systems.

Brainstorm with students about ml in their lives
- did they ride public transport, use Google maps, wayze, or Evans ridereport app
- did they use their phone
  - login, wifi, autocomplete
interact with any websites?
  - purchases
  - analytics
  - advertisements
- Spam filter
- Spelling corrector
- Fraud detection
- Recruiting (reading resumes and matching to job openings)
- writing poetry
- generating visual art (painting)
- recognizing cats v dogs
- recognizing individual faces
- video captcha to verify face photos
- password security/randomness estimate ?
- banjo predictions of world events from twitter
  - only have to be a ms faster
  - beating associated press and CNN by hours
- chess
- jeopardy
- deep mind atari video games (breakout expert in 4 hr)
- go (enumerated all boards)
- cpap machines
- prosthetics
- radiology doctor bots
  - mri
  - ekg
- authentication: logging onto your computer, b am account
  - ekg
  - fingerprint
- Starbucks customer RF id
  - preference profiling
- home automation

[...and the list goes on...](http://hobsonlane.com/Definition-of-AI-and-a-Big-List-of-Applications/Exp)

## Compression

Surprisingly, many researchers in Machine Intelligence spend a lot of time creating new and better compression algorithms. Why would this be?

How is Machine Learning like ...

- Communication (transmitting information)
- Visualization (conveying knowledge to a human)

Later in this course you'll learn why. Once you've mastered the basics and can perform regression and classification several different ways, we'll talk about information theory, channel capacity, complexity, entropy, and intelligence metrics.

## Hack Oregon Applications

### Campaign Finance

If you had the financial transaction records for all Oregon:

- campaigns
- PACs
- candidates
- campaign managers

- money spent
- money received
- size of donors
- business location
  - donors
  - recipients
  - vendors
- home addresses
  - donors
  - recipients
  - vendors
- stated puposes/causes
- political party

What would you do with it?

What could you predict?

- election outcomes
- donor relationships
- money flow

What data would you need to train the model?
What would you need to make use of it?
What if transaction data was delayed by 1 month?
What if transactions were "laundered"?

### Agriculture

If you had access to the agricultural harvest data for Oregon:


- crop (Barley, Blackberries, Walnuts)
- county (jurisdiction)
- location
- acreage
- type of soil
- climate/weather
- water usage?

What would you do with it?
What could you predict?

- harvest during a drought?
- harvest during boom/glut (perfect weather)?

### Hunger

What would you do if you had...

- rental costs for each county in Oregon
- food costs in Oregon
- tax code information
- minimum wage in Oregon
- income statistics across Oregon
- meal statistics for poor families in Oregon
- federal guidelines and formulas for food "insecurity"

What would you do with it?
What could you predict?
Could you run a simulated experiment?
Could you estimate the "ROI"?
Is it possible that business would benefit from wage hike?

### Education

What would you do if you had...

- enrollment information for 10000+ individual students
- demographic information for those individuals

How would you protect their privacy?
Could you estimate the impact of policies?
Could you determine cause and effect?

## Motivation

If you have somehow avoided it today, I'm going to inject some ml. Answer a poll for me so i can learn which lectures worked well and which didn't. Get andrew at harv.is to sponsor us?
Bots are already our companions. We are already cyborgs. So get to know your partner or you may lose control over your life to those pulling the puppet strings of the bots. Train them like you'd train your pet dog, or lizard

## [Install Your Tools](install.md)

Learning vs teaching
   Feature engineering
Representation vs modeling
   Master Algorithm

## Regression

- Linear Regression
- Nonlinear Regression
- Multivariate Regression

Resources
- https://github.com/josephmisiti/awesome-machine-learning/blob/master/README.md
- that ml resource website i wrote review on?

## Food for Thought, Discussion

- What about wisdom of the crowds?
  - Can't we humans work together to be smart than machines?
- Is machine learning susceptable to any systematic biases?
  - Do logic fallacies apply to machines?
  - Are machines susceptable to cognitive biases?
  - Might any of the logic fallacies apply to machines?
- Do machines ever rely on "Rules of Thumb"?
  - hint: look up the word "heuristic"
- Are machines inherently moral, ethical? amoral? unethical?
  - Are machines objective? Do machines have prejudices, biases? 
- Are machines inherently anti-social? pro-social? a-social? 
  - What about the "control problem" that Elon Musk and others are worried about?
  - What about self driving cars having to decide whether endanger their owner by swerving to avoid
    - a squirrel
    - a family of ducks
    - a cat
    - a dog
    - an abandoned $1M Lamborghini
    - a dead body 
    - a dying person just hit by a car
    - a fatally ill zombie
    - an elderly or disabled person
    - hospital gurny with a patient
    - a pedestrian
    - a child
    - a baby carriage
    - a crowd
  - What if you are in a hury or have important cargo?
    - What if you are pregnant?
    - What if you're whole family is in the car?
    - What if Obama is your passenger?
    - What if you are an assassin or thief or mobster?
    - What if you are driving an armored car full of depositor savings or employee paychecks?

## Homework (optional)

- Sign up for the free Udacity course ["Introduction to Machine Learning"](https://udacity.com/course/viewer#!/c-ud120)
- Skip Lesson 0 (Welcome), and watch 2nd video in [Lesson 1 "Bayes Classifier -- Acerous or Non-Acerous"](https://www.udacity.com/course/viewer#!/c-ud120/l-2254358555/e-3077538977/m-3061308637)
  - What might be wrong with this picture?
  - Hint, it's not the "picture" that's wrong, but a feature concept.
- Watch the 3rd video in Lesson 1 to Take the [Supervised Classification Quiz](https://www.udacity.com/course/viewer#!/c-ud120/l-2254358555/e-2345828677/m-2407048539)
- Take the quiz on [Scatter Plot Intuition](https://www.udacity.com/course/viewer#!/c-ud120/l-2254358555/e-3014058778/m-3022458589)
- And [another](https://www.udacity.com/course/viewer#!/c-ud120/l-2254358555/e-3015228658/m-3022458586)
- How many human logic fallacies are listed on wikipedia or in any list?
  - cut and paste into excel, libre office, Google sheets, or your text editor
  - estimate
- If you like finance watch "The Big Short"
  - look for applications for machine learning
  - could a machine have predicted the 2008 crash?
  - why didn't the Scion prediction come true immediately?
  - can you predict the behavior of a mob? a corrupt system?
