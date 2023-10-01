import numpy as np
import matplotlib.pyplot as plt
import questionary
from colorama import Fore, Style
from pyfiglet import Figlet

#title screen
f = Figlet(font='larry3d')
print(Fore.YELLOW + f.renderText('vaccine simulation'))
print(f'{Fore.LIGHTGREEN_EX}Welcome to VEABG (viral evolution analyser by graph)!\n{Style.RESET_ALL}')
gray = Fore.WHITE + Style.BRIGHT
blue = Fore.BLUE
print(gray + 'This work is licensed under a CC BY-NC-SA 4.0 License. Read it here: ' + blue + 'https://creativecommons.org/licenses/by-nc-sa/4.0/')
print(gray + 'Source code: ' + blue + 'https://github.com/malwprotector/veabg\n')
print(f'{Fore.LIGHTRED_EX + Style.BRIGHT}WARNING! Please note that this programme has been produced for school purposes ONLY. It may contain erroneous or inaccurate information. You use it at your own risk.\n{Style.RESET_ALL}')

# Simulation parameters
population = int(questionary.text("Enter the total population size covered by the vaccination study: ").ask())

initial_infected = int(questionary.text("Enter the initial number of infected population:  ").ask())

infection_rate = float(questionary.rawselect(
    "Select the infection rate (probability of a susceptible person getting infected on contact): ",
    choices=["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
).ask())

recovery_rate = float(questionary.rawselect(
    "Select the recovery rate (probability of an infected person recovering per day: ",
    choices=["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
).ask())

days_simulation = int(questionary.text("Enter the number of days to simulate: ").ask())

vaccination_rate = float(questionary.rawselect(
    "Select the daily vaccination rate: ",
    choices=["0.01", "0.02", "0.03", "0.04", "0.05", "0.06", "0.07", "0.08", "0.09", "0.1"],
).ask())

quarantine_rate = float(questionary.rawselect(
    "Select the daily quarantine rate (proportion of infected individuals in quarantine: ",
    choices=["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
).ask())

social_contacts = int(questionary.text("Enter the average number of social contacts per day: ").ask())

mobility_factor = float(questionary.rawselect(
    "Enter the factor reducing social contacts due to mobility restrictions: ",
    choices=["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
).ask())

vaccine_efficacy = float(questionary.rawselect(
    "Enter the efficacy of the vaccine (reduces the probability of infection): ",
    choices=["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"],
).ask())

#confirmation
print(f'{Fore.CYAN + Style.BRIGHT}population size covered by the vaccination study:{Style.RESET_ALL}', Fore.YELLOW + str(population) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}initial number of infected population:{Style.RESET_ALL}', Fore.YELLOW + str(initial_infected) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}infection rate:{Style.RESET_ALL}', Fore.YELLOW + str(infection_rate) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}recovery rate:{Style.RESET_ALL}', Fore.YELLOW + str(recovery_rate) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}number of days to simulate:{Style.RESET_ALL}', Fore.YELLOW + str(days_simulation) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}daily vaccination rate:{Style.RESET_ALL}', Fore.YELLOW + str(vaccination_rate) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}daily quarantine rate:{Style.RESET_ALL}', Fore.YELLOW + str(quarantine_rate) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}social contacts per day:{Style.RESET_ALL}', Fore.YELLOW + str(social_contacts) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}factor reducing social contacts due to mobility restrictions:{Style.RESET_ALL}', Fore.YELLOW + str(mobility_factor) + Style.RESET_ALL)
print(f'{Fore.CYAN + Style.BRIGHT}vaccine efficacy:{Style.RESET_ALL}', Fore.YELLOW + str(vaccine_efficacy) + Style.RESET_ALL)



confirmation = questionary.confirm('Are the data entered correct?').ask()
if confirmation == True:
    print(f'{Fore.LIGHTGREEN_EX}Initialising the simulation...{Style.RESET_ALL}')
else:
    print(f'{Fore.LIGHTRED_EX + Style.BRIGHT}Please restart the script, and ensure that the values entered are correct.\n Closing...{Style.RESET_ALL}')
    exit()

# Initialize arrays to track the evolution
print(f'{Fore.LIGHTGREEN_EX}Initialising arrays to track the evolution...{Style.RESET_ALL}')
susceptible = np.zeros(days_simulation)
infected = np.zeros(days_simulation)
recovered = np.zeros(days_simulation)
vaccinated = np.zeros(days_simulation)
quarantined = np.zeros(days_simulation)

# Initialize population
print(f'{Fore.LIGHTGREEN_EX}Initialising population...{Style.RESET_ALL}')
susceptible[0] = population - initial_infected
infected[0] = initial_infected
recovered[0] = 0

# Simulation
print(f'{Fore.LIGHTGREEN_EX}Starting simulation...{Style.RESET_ALL}')
for day in range(1, days_simulation):
    # Calculate the number of new infections
    new_infections = (infection_rate * (1 - (quarantined[day-1] / infected[day-1])) *
                      (susceptible[day-1] / population) * social_contacts * mobility_factor * infected[day-1])
    new_infections *= (1 - (vaccinated[day-1] / population) * vaccine_efficacy)

    # Calculate the number of recoveries
    recoveries = recovery_rate * infected[day-1]

    # Update populations
    susceptible[day] = susceptible[day-1] - new_infections
    infected[day] = infected[day-1] + new_infections - recoveries
    recovered[day] = recovered[day-1] + recoveries

    # Vaccination
    people_vaccinated = susceptible[day] * vaccination_rate
    susceptible[day] -= people_vaccinated
    vaccinated[day] = vaccinated[day-1] + people_vaccinated

    # Quarantine
    quarantined[day] = infected[day] * quarantine_rate
print(f'{Fore.LIGHTGREEN_EX}Done!{Style.RESET_ALL}')

# Plotting the results
print(f'{Fore.LIGHTGREEN_EX}generating the graph...{Style.RESET_ALL}')
days = np.arange(days_simulation)
plt.plot(days, susceptible, label='Susceptible')
plt.plot(days, infected, label='Infected')
plt.plot(days, recovered, label='Recovered')
plt.plot(days, vaccinated, label='Vaccinated')
plt.plot(days, quarantined, label='Quarantined')
plt.xlabel('Days')
plt.ylabel('Population')
plt.legend()
plt.show()
print('Closing...')

