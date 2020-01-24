from scipy.special import comb
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def probabilities_num_alive(m_rate, num_offspring):
    prob_num_alive = []
    for num_a in range(num_offspring + 1):
        num_d = num_offspring - num_a
        n_choose_a = comb(num_offspring, num_a)

        p_num_a = n_choose_a * ((1 - m_rate) ** num_a) * (m_rate ** num_d)
        prob_num_alive.append(p_num_a)

    return prob_num_alive


def plot_probabilities_num_alive(probabilities_list):
    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    plt.title(
        'Probability of each Number of Children Surviving Past 5 Years Old\n When Number of Children Born = ' + str(
            len(probabilities_list) - 1))
    plt.ylabel('Probability')
    plt.xlabel('Number of Children Surviving')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    x = list(range(len(probabilities_list)))
    for a, b in zip(x, probabilities_list):
        plt.text(a, b, "{:0.0%}".format(b), ha='center', va='bottom', size=15)
    plt.bar([str(value) for value in x], probabilities_list)


def probabilities_num_alive_list(m_rate, max_children):
    prob_num_alive_list = []
    for i in range(1, max_children + 1):
        prob_num_alive_list.append(probabilities_num_alive(m_rate, i))
    return prob_num_alive_list


def plot_probabilities_num_alive_list(prob_num_alive_list):
    for prob_num_alive in prob_num_alive_list:
        plot_probabilities_num_alive(prob_num_alive)
        plt.show()
        print('\n')


def expected_number_surviving(probabilities_list):
    weighted_sum = 0
    for num_surviving in range(len(probabilities_list)):
        weighted_sum += probabilities_list[num_surviving] * num_surviving
    return weighted_sum


def expected_number_surviving_list(prob_num_alive_list):
    ex_num_surviving_list = []
    for prob_num_alive in prob_num_alive_list:
        ex_num_surviving_list.append(expected_number_surviving(prob_num_alive))
    return ex_num_surviving_list


def plot_expected_number_surviving_list(ex_num_surviving_list):
    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    plt.title('Expected Number of Children Surviving Past 5 Years Old \n Based on Number of Children Born')
    plt.ylabel('Number of Children Surviving')
    plt.xlabel('Number of Children Born')
    x = list(range(1, len(ex_num_surviving_list) + 1))
    for a, b in zip(list(range(len(x))), ex_num_surviving_list):
        plt.text(a, b + 0.05, str(round(b, 1)), ha='center', va='bottom', size=15)
    plt.scatter([str(value) for value in x], ex_num_surviving_list)


def prob_at_least_n_survive_list(n, prob_num_alive_list):
    prob_at_lst_n_survive_list = []
    for prob_num_alive in prob_num_alive_list:
        if len(prob_num_alive_list) > n:
            prob = prob_at_least_n_survive(n, prob_num_alive)
            prob_at_lst_n_survive_list.append(prob)
        else:
            prob_at_lst_n_survive_list.append(0)
    return prob_at_lst_n_survive_list


def prob_at_least_n_survive(n, prob_num_alive):
    return sum(prob_num_alive[n:])


def plot_prob_at_least_n_survive_list(prob_at_lst_n_survive_list):
    at_least_num = prob_at_lst_n_survive_list.count(0) + 1
    plt.style.use('seaborn')
    plt.style.use('seaborn-talk')
    plt.title('Probability That At Least ' + str(
        at_least_num) + ' Children Survive Past 5 Years Old\n Based on Number of Children Born')
    plt.ylabel('Probability')
    plt.xlabel('Number of Children Born')
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    x = list(range(at_least_num, len(prob_at_lst_n_survive_list) + at_least_num - 1))
    for a, b in zip(list(range(len(x))), prob_at_lst_n_survive_list[at_least_num - 1:]):
        plt.text(a, b + 0.01, "{:0.0%}".format(b), ha='center', va='bottom', size=15)
    x = [str(value) for value in x]
    plt.scatter(x, prob_at_lst_n_survive_list[at_least_num - 1:])
