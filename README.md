# The Epic Armageddon Machine Spirit
New unit points prediction for Epic Armageddon using machine learning 

## What
The goal is to train a model on the existing units for [Epic Armagaddon](https://net-armageddon.org) found in the [Tournament Pack](https://tp.net-armageddon.org/) and use that model to predict the point cost of new units, with a good starting point, in order to skip time comsuming play testing.

## How
By converting unit profiles to vectors and feeding them to a Gaussian Process Regression (GPR) model, it is able to predict a point value and also an uncertainty measure of a new unit. GPR is preferred for at task like this, because it can produce pretty accurate prediction based on a small set of data points (hundreds), compared to neural nets that usually requires large data sets (thousands). 

## Why
I want to adopt the new Legion Imperialis releases from Games Workshop into the Epic Armageddon ruleset (also by Games Workshop).

## Current state

By training on a small portion of Space Marines, Orks, Steel Legion and some Eldar and trying to predict the point cost of unis from the Horus Heresy Supplement.

| Name                                                            |   Original Cost |   Predicted Cost | Uncertainty   | Quality   |   Score |
|-----------------------------------------------------------------|-----------------|------------------|---------------|-----------|---------|
| Legion Tactical Squad                                           |            34   |               38 | ±11.3         | MEDIOCRE  |      71 |
| Legion Assault Squad                                            |            37.5 |               44 | ±2.7          | EXELENT   |      94 |
| Legion Tactical Support Squad                                   |            50   |               89 | ±30.4         | MEDIOCRE  |      66 |
| Legion Heavy Support Squad                                      |            50   |               72 | ±14.2         | GOOD      |      80 |
| Legion Terminator Squad                                         |            75   |               83 | ±21.4         | MEDIOCRE  |      74 |
| Legion Sicaran Battle Tank (Accelerator Cannon + Heavy Bolters) |            75   |               78 | ±11.6         | GOOD      |      85 |
| Legion Sicaran Battle Tank, with Omega plasma array             |            75   |               76 | ±11.4         | GOOD      |      85 |
| Predator Annihilator                                            |            60   |               63 | ±2.7          | EXELENT   |      96 |
| Predator Destructor                                             |            60   |               62 | ±2.7          | EXELENT   |      96 |
| Spartan Assault Tank                                            |           125   |              157 | ±28.4         | GOOD      |      82 |
| Legion Thunderhawk Gunship                                      |           250   |              185 | ±35.2         | GOOD      |      81 |
| Fire Raptor Gunship                                             |           150   |              139 | ±35.0         | MEDIOCRE  |      75 |
| Storm Eagle Attack Ship                                         |           125   |              154 | ±31.5         | GOOD      |      80 |
| Xiphon Interceptor                                              |           125   |               94 | ±26.1         | MEDIOCRE  |      72 |
| Contemptor Dreadnought with Lascannon                           |            60   |               53 | ±6.5          | GOOD      |      88 |
| Contemptor Dreadnought with Assault Cannon                      |            60   |               51 | ±2.9          | EXELENT   |      94 |
| Deredo Dreadnought                                              |           100   |              100 | ±30.6         | MEDIOCRE  |      69 |
| Vindicator                                                      |            50   |               56 | ±2.7          | EXELENT   |      95 |
| Vindicator Laser Destroyer                                      |            70   |               50 | ±17.0         | MEDIOCRE  |      66 |
| Legion Whirlwind                                                |            75   |               87 | ±13.8         | GOOD      |      84 |
| Legion Whirlwind Scorpius                                       |            75   |               79 | ±11.7         | GOOD      |      85 |
| Typhon Siege Tank                                               |           133.3 |              210 | ±41.0         | GOOD      |      81 |
| Cerberus Tank Destroyer                                         |           133.3 |              192 | ±48.5         | MEDIOCRE  |      75 |
| Kratos Battle Tank with H.B.                                    |           100   |              185 | ±28.4         | GOOD      |      85 |
| Kratos Battle Tank with Las.                                    |           100   |              201 | ±34.2         | GOOD      |      83 |
| Legion Mastodon Armored Transport                               |           200   |              196 | ±46.0         | GOOD      |      77 |
| Land Speeder with Plasma                                        |            40   |               39 | ±14.8         | BAD       |      62 |
| Land Speeder with Melta                                         |            40   |               35 | ±9.3          | MEDIOCRE  |      74 |
| Javelin Attack Speeder Cyclone                                  |            50   |               55 | ±13.6         | GOOD      |      75 |
| Javelin Attack Speeder Lascannons                               |            50   |               50 | ±13.1         | MEDIOCRE  |      74 |
| Outrider squad                                                  |            35   |               47 | ±19.0         | BAD       |      59 |
| Leman Russ (Battle cannon + Las)                                |            58.3 |               69 | ±15.8         | GOOD      |      77 |

**Original Cost**
This is the cost from the epic armageddon AU, Horus Heresy suplement

**Predicted Cost**
This is the current model's prediction

**Uncertainty**
How many points, + or - from the predicted cost

**Quality**
Label of score, for readability

**Score**
The score is calculated by comparing the Uncertainty to the Predicted Cost. 

For instance the Land Speeder with Plasma is currently scoring low because the uncertainty of 14 is about 38% of the predicted cost of 39, but Legion Heavy Support Squad gets a higher score while also having 14 points of uncertainty, but it's only about 20% of the predicted cost.

It's impressive to see how close some predictions are to the original cost. 
