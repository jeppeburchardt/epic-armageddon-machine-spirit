# The Epic Armageddon Machine Spirit
New unit points prediction for Epic Armageddon using machine learning 

## What
The goal is to train a model on the existing units for [Epic Armagaddon](https://net-armageddon.org) found in the [Tournament Pack](https://tp.net-armageddon.org/) and use that model to predict the point cost of new units, with a good starting point, in order to skip time comsuming play testing.

## How
By converting unit profiles to vectors and feeding them to a Gaussian Process Regression (GPR) model, it is able to predict a point value and also an uncertainty measure of a new unit. GPR is preferred for at task like this, because it can produce pretty accurate prediction based on a small set of data points (hundreds), compared to neural nets that usially requires large data sets (thousands). 

## Why
I want to adopt the new Legion Imperialis releases from Games Workshop into the Epic Armageddon ruleset (also by Games Workshop).

