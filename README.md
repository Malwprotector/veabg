# Viral evolution analyser by graph 
<a> <img src='https://raw.githubusercontent.com/Malwprotector/veabg/main/illustration.png'></img></a>

veabg is a vaccine simulator in python that produces a graph based on input data. It was produced as part of a school science course.

When you are asked to select values with shortcuts, use ctrl+n to move the cursor.

<strong>WARNING! Please note that this programme has been produced for school purposes ONLY. It may contain erroneous or inaccurate information. You use it at your own risk.</strong>

# FAQ

<strong>What is infection rate?</strong>


The infection rate in a simulation like this represents the probability that a susceptible person will become infected when in contact with an infected person. In other words, it measures the likelihood of transmission when an infected person interacts with a susceptible person.

Here's a bit more detail:

1. **Probability of Transmission**: An infection rate of 0.2, for example, means that there's a 20% chance of an uninfected person becoming infected if they come into contact with an infected person.

2. **Key Parameter for Spread**: The infection rate is a critical parameter in modeling the spread of infectious diseases. A higher infection rate means the disease spreads more easily.

3. **Dependent on the Disease**: Different diseases have different natural infection rates. For example, highly contagious diseases like measles have very high infection rates, while others like HIV have lower rates.

4. **Affected by Interventions**: Public health measures, like vaccination, quarantine, and social distancing, can directly influence the effective infection rate by reducing the number of interactions between infected and susceptible individuals.

5. **Calibration**: In the context of a simulation like this, the infection rate is a parameter that might be calibrated using real-world data or adjusted based on the specifics of the simulated scenario.

Remember that in a real-world scenario, the actual infection rate of a disease depends on various factors including the pathogen's characteristics, the environment, and human behavior. It's a complex parameter that's central to understanding and managing epidemics.

<strong>What is the recovery rate?</strong>


The recovery rate in a virus simulation represents the probability that an infected individual will recover from the illness in a given period, typically a day. It is a crucial parameter in modeling the spread of infectious diseases.

In more detail:

1. **Infected Population**: This is the number of individuals who are currently infected with the virus.

2. **Recovery Rate**: If the recovery rate is 0.2 (20%), it means that on average, 20% of the infected population will recover each day. This rate takes into account both natural recovery and any medical interventions that might expedite the recovery process.

3. **New Recoveries**: In the simulation, each day, a number of individuals equal to the recovery rate times the current number of infected individuals are moved from the "infected" category to the "recovered" category.

4. **Effect on Transmission**: A higher recovery rate means that infected individuals are more likely to recover quickly, which can slow down the spread of the virus. Conversely, a lower recovery rate would mean that individuals are sick for a longer period, potentially leading to a faster spread.

5. **Impact of Healthcare**: A higher recovery rate can also represent better healthcare, as individuals are more likely to recover with medical treatment.

In real-world terms, the recovery rate is influenced by factors like the nature of the virus (some viruses are more lethal and have lower recovery rates), the availability of medical care, and the overall health of the population.

In summary, the recovery rate is a crucial parameter in modeling the dynamics of infectious diseases, as it helps to determine how quickly infected individuals will recover and no longer be able to spread the virus.

<strong>What is the daily vaccination rate?</strong>


The "daily vaccination rate" in this context refers to the proportion of the population that is being vaccinated each day. It's a measure of how quickly the vaccination campaign is being carried out.

For example, if the daily vaccination rate is set to 0.02, it means that on each day of the simulation, 2% of the total population is being vaccinated. This rate is applied consistently each day.

The purpose of specifying a daily vaccination rate in a simulation like this is to model the gradual rollout of a vaccination campaign over time. It allows you to explore different scenarios of vaccination speed and its impact on the spread of a virus.

In real-world situations, the vaccination rate can be influenced by various factors such as availability of vaccines, logistical challenges, public willingness to get vaccinated, and government policies. By including this parameter in the simulation, you can analyze how different rates of vaccination affect the overall outcome of the epidemic.

<strong>What is the daily quarantine rate?</strong>


The "daily quarantine rate" in this context represents the proportion of infected individuals who are isolated or kept in quarantine each day. It is a parameter in the simulation that determines how effective quarantine measures are at reducing the spread of the virus.

Here's how it works within the simulation:

1. **Calculation**: At each day of the simulation, the number of individuals who are quarantined is determined by multiplying the current number of infected individuals by the daily quarantine rate.

2. **Effect**: This effectively reduces the number of interactions infected individuals have with others in the population. Quarantining infected individuals helps limit their contact with susceptible individuals, which in turn slows down the spread of the virus.

3. **Impact on New Infections**: The daily quarantine rate is used to adjust the calculation of new infections. The formula for new infections includes a term that takes into account the proportion of infected individuals in quarantine.

   For example, if the daily quarantine rate is 0.3 (30%), it means that 30% of the infected individuals are in quarantine on a given day. This would result in a lower likelihood of spreading the virus, which is reflected in the calculation.

4. **Real-world Analogy**: In reality, this parameter could represent the effectiveness of public health measures such as contact tracing, isolation of infected individuals, and encouraging people who are sick to stay home.

In summary, the daily quarantine rate is a way to model the impact of quarantine measures on the spread of the virus within the simulation. A higher quarantine rate means more infected individuals are effectively isolated, leading to a slower spread of the virus.

<strong>What is the average of social contacts per day?</strong>


The "average number of social contacts per day" is a parameter in the simulation that represents how many interactions an individual has with other people in a given day. In the context of a virus spread simulation, this parameter is important because it influences the potential for the virus to spread from an infected person to others.

Here's what it means:

1. **High Value**: If the average number of social contacts per day is high, it implies that individuals are interacting with many others on a regular basis. This would lead to a higher likelihood of virus transmission, assuming the virus is contagious.

2. **Low Value**: Conversely, if this value is low, it suggests that individuals have fewer interactions with others. This would reduce the opportunities for the virus to spread.

For example, consider two scenarios:

- **Scenario A**: In a densely populated urban area with high social interaction, the average number of social contacts per day might be relatively high. This means people are frequently interacting with many others, potentially leading to a faster spread of a contagious virus.

- **Scenario B**: In a sparsely populated rural area or during a lockdown, the average number of social contacts per day might be much lower. This implies that people have fewer interactions, reducing the chances of virus transmission.

Adjusting this parameter allows the simulation to reflect different social behaviors and interventions that can affect the spread of a virus. It helps model the real-world dynamics of how people interact and how that impacts the spread of the virus in a population.

<strong>What is the factor reducing social contacts due to mobility restrictions?</strong>


The "factor reducing social contacts due to mobility restrictions" is a parameter in the simulation that represents the reduction in the number of social interactions people have due to measures put in place to restrict movement. 

In real-world scenarios, this could be related to various factors such as:

1. **Government-imposed restrictions**: These can include lockdowns, stay-at-home orders, or limitations on gatherings. These measures are put in place to reduce the spread of a disease by limiting the opportunities for people to come into close contact with one another.

2. **Public health recommendations**: Even in the absence of official restrictions, public health authorities may recommend or advise individuals to limit their social interactions, maintain physical distance, and take other precautions to reduce the risk of transmission.

3. **Behavioral changes**: During a pandemic or similar crisis, individuals may voluntarily choose to limit their social interactions, avoid crowded places, and take other precautions to protect themselves and others.

The parameter "factor reducing social contacts due to mobility restrictions" in your simulation allows you to model the impact of these measures on the spread of the virus. It represents a scaling factor applied to the average number of social contacts per day. For example, if this factor is set to 0.5, it means that social interactions are reduced to half of their normal level due to mobility restrictions.

In summary, this parameter helps simulate the effect of societal and governmental efforts to reduce the spread of a virus by limiting social interactions and mobility. This is an important factor to consider in epidemiological models to better understand how different interventions can influence the course of an epidemic.
