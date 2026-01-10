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

As the table shows, some predictions are quite accurate and some are not. 

The model still needs more unit to train on and maybe the vector mapping needs to be improved.

| Name                                                            |   Original Cost |   Predicted Cost | Uncertainty   | Quality   |   Score |
|-----------------------------------------------------------------|-----------------|------------------|---------------|-----------|---------|
| Legion Tactical Squad                                           |              34 |               40 | ±10.6         | MEDIOCRE  |      74 |
| Legion Assault Squad                                            |              38 |               44 | ±6.3          | GOOD      |      86 |
| Legion Tactical Support Squad                                   |              50 |               89 | ±25.3         | MEDIOCRE  |      72 |
| Legion Heavy Support Squad                                      |              50 |               69 | ±12.7         | GOOD      |      82 |
| Legion Terminator Squad                                         |              75 |               80 | ±18.3         | GOOD      |      77 |
| Legion Sicaran Battle Tank (Accelerator Cannon + Heavy Bolters) |              75 |               70 | ±10.4         | GOOD      |      85 |
| Legion Sicaran Battle Tank, with Omega plasma array             |              75 |               68 | ±9.1          | GOOD      |      87 |
| Predator Annihilator                                            |              60 |               64 | ±5.9          | EXCELLENT |      91 |
| Predator Destructor                                             |              60 |               57 | ±5.9          | GOOD      |      90 |
| Land Raider                                                     |              75 |               60 | ±9.9          | GOOD      |      83 |
| Spartan Assault Tank                                            |             125 |              144 | ±21.0         | GOOD      |      85 |
| Legion Thunderhawk Gunship                                      |             250 |              167 | ±28.8         | GOOD      |      83 |
| Fire Raptor Gunship                                             |             150 |              125 | ±28.7         | GOOD      |      77 |
| Storm Eagle Attack Ship                                         |             125 |              146 | ±26.3         | GOOD      |      82 |
| Xiphon Interceptor                                              |             125 |               98 | ±21.9         | GOOD      |      78 |
| Contemptor Dreadnought with Lascannon                           |              60 |               55 | ±7.8          | GOOD      |      86 |
| Contemptor Dreadnought with Assault Cannon                      |              60 |               50 | ±6.3          | GOOD      |      88 |
| Deredo Dreadnought                                              |             100 |               91 | ±25.5         | MEDIOCRE  |      72 |
| Vindicator                                                      |              50 |               57 | ±6.2          | GOOD      |      89 |
| Vindicator Laser Destroyer                                      |              70 |               53 | ±14.0         | MEDIOCRE  |      74 |
| Legion Whirlwind                                                |              75 |               86 | ±12.4         | GOOD      |      85 |
| Legion Whirlwind Scorpius                                       |              75 |               71 | ±11.0         | GOOD      |      85 |
| Typhon Siege Tank                                               |             133 |              210 | ±34.4         | GOOD      |      84 |
| Cerberus Tank Destroyer                                         |             133 |              202 | ±41.9         | GOOD      |      79 |
| Kratos Battle Tank with H.B.                                    |             100 |              160 | ±22.1         | GOOD      |      86 |
| Kratos Battle Tank with Las.                                    |             100 |              187 | ±26.8         | GOOD      |      86 |
| Legion Mastodon Armored Transport                               |             200 |              192 | ±38.3         | GOOD      |      80 |
| Land Speeder with Plasma                                        |              40 |               28 | ±7.6          | MEDIOCRE  |      73 |
| Land Speeder with Melta                                         |              40 |               33 | ±9.1          | MEDIOCRE  |      72 |
| Javelin Attack Speeder Cyclone                                  |              50 |               44 | ±5.6          | GOOD      |      87 |
| Javelin Attack Speeder Lascannons                               |              50 |               43 | ±6.0          | GOOD      |      86 |
| Outrider squad                                                  |              35 |               34 | ±11.7         | MEDIOCRE  |      65 |
| Infantry Section                                                |              14 |               23 | ±8.1          | BAD       |      64 |
| Infantry with flamers                                           |              19 |               39 | ±16.2         | BAD       |      58 |
| Veletaris Storm Section                                         |              19 |               24 | ±16.0         | BAD       |      33 |
| Ogryn Charonite Squad                                           |              38 |               27 | ±12.6         | BAD       |      54 |
| Tactical Command Unit                                           |              50 |               25 | ±9.9          | BAD       |      61 |
| Legate Command Unit                                             |             150 |               26 | ±11.8         | BAD       |      54 |
| Rapier Mole Mortar                                              |              25 |               44 | ±21.3         | BAD       |      52 |
| Rapier Laser Destroyer                                          |              25 |               27 | ±7.9          | MEDIOCRE  |      71 |
| Rapier Light Artillery                                          |              25 |               41 | ±15.9         | BAD       |      62 |
| Aethon Heavy Sentinel                                           |               0 |               31 | ±8.5          | MEDIOCRE  |      73 |
| Tarantula, Twin Lascannon                                       |              25 |               36 | ±24.7         | BAD       |      31 |
| Tarantula, Hyperios air-defence missile launcher                |              25 |               39 | ±25.6         | BAD       |      35 |
| Leman Russ (Battle cannon + Las)                                |              58 |               63 | ±11.7         | GOOD      |      81 |
| Leman Russ (Battle cannon + H.B.)                               |              58 |               60 | ±9.8          | GOOD      |      84 |
| Leman Russ (Vanquisher + Las)                                   |              58 |               63 | ±11.7         | GOOD      |      81 |
| Leman Russ (Vanquisher + H.B.)                                  |              58 |               59 | ±9.8          | GOOD      |      83 |
| Leman Russ (Annihilator)                                        |              58 |               50 | ±11.3         | GOOD      |      77 |
| Leman Russ (Demolisher)                                         |              58 |               59 | ±15.1         | MEDIOCRE  |      74 |
| Leman Russ (Exterminator)                                       |              58 |               56 | ±9.9          | GOOD      |      82 |
| Leman Russ (Executioner)                                        |              58 |               50 | ±9.6          | GOOD      |      81 |
| Malcador (battle cannon, demolisher, las.spon.)                 |             100 |               88 | ±16.1         | GOOD      |      82 |
| Malcador (vanquisher, demiólisher, h.b.spon.)                   |             100 |               75 | ±14.9         | GOOD      |      80 |
| Malcador (las cannons)                                          |              70 |               67 | ±14.5         | GOOD      |      78 |
| Dracosan with las cannon                                        |               0 |               36 | ±12.1         | MEDIOCRE  |      66 |
| Dracosan with demolisher                                        |               0 |               52 | ±14.7         | MEDIOCRE  |      72 |
| Medusa                                                          |              83 |               54 | ±22.3         | BAD       |      59 |
| Basilisk                                                        |              83 |               70 | ±7.9          | GOOD      |      89 |
| Basilisk (Barrage)                                              |              83 |               89 | ±15.7         | GOOD      |      82 |
| Arvus Lighter                                                   |              25 |               44 | ±32.0         | BAD       |      28 |
| Malcador Infernus                                               |              70 |               57 | ±10.0         | GOOD      |      82 |
| Malcador Valdor                                                 |              83 |               77 | ±22.9         | MEDIOCRE  |      70 |
| Shadowsword                                                     |             200 |              189 | ±9.9          | EXCELLENT |      95 |
| Stromblade                                                      |             200 |              175 | ±14.9         | EXCELLENT |      91 |
| Stormsword                                                      |             200 |              162 | ±29.5         | GOOD      |      82 |
| Baneblade                                                       |             200 |              166 | ±11.0         | EXCELLENT |      93 |
| Stormhammer                                                     |             200 |              159 | ±16.7         | GOOD      |      89 |
| Avenger Strike Fighter                                          |             125 |               85 | ±14.5         | GOOD      |      83 |
| Thunderbolt                                                     |             112 |               78 | ±8.3          | GOOD      |      89 |
| Marauder Bomber                                                 |             125 |              120 | ±15.2         | GOOD      |      87 |


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

| Name                                                            |   Original Cost |   Predicted Cost | Uncertainty   | Quality   |   Score |
|-----------------------------------------------------------------|-----------------|------------------|---------------|-----------|---------|
| Legion Heavy Support Squad                                      |            50   |               72 | ±14.2         | GOOD      |      80 |
| Land Speeder with Plasma                                        |            40   |               39 | ±14.8         | BAD       |      62 |

For instance the Land Speeder with Plasma is currently scoring low because the uncertainty of 14 is about 38% of the predicted cost of 39, but Legion Heavy Support Squad gets a higher score while also having 14 points of uncertainty, but it's only about 20% of the predicted cost.

