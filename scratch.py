import pandas as pd
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt

# Initial assumptions for the seed round
seed_investment = 8.12 * 1e6  # $8.12 million
seed_ownership = 0.20  # 20% equity ownership

# Founder ownership post-seed round
founder_ownership_post_seed = 1 - seed_ownership

# Scenario options for Series A
scenarios_a = {
    "Scenario 1 ($25M)": 25000000,
    "Scenario 2 ($35M)": 35000000,
    "Scenario 3 ($45M)": 45000000
}

# Widgets for user inputs
scenario_a_widget = widgets.Dropdown(
    options=scenarios_a.keys(),
    value="Scenario 1 ($25M)",
    description='Series A Scenario:',
    style={'description_width': 'initial'}
)

investment_a_widget = widgets.FloatSlider(
    value=10.00,
    min=1.00,
    max=20.00,
    step=0.10,
    description='Series A Investment $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

dilution_a_widget = widgets.FloatSlider(
    value=0.50,
    min=0,
    max=1,
    step=0.05,
    description='Series A Dilution:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

# Additional rounds (Series B, C, and D)
investment_b_widget = widgets.FloatSlider(
    value=15.00,
    min=1.00,
    max=25.00,
    step=0.10,
    description='Series B Investment $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

pre_money_b_widget = widgets.FloatSlider(
    value=50.00,
    min=10.00,
    max=100.00,
    step=1.00,
    description='Series B Pre-Money $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

dilution_b_widget = widgets.FloatSlider(
    value=0.50,
    min=0,
    max=1,
    step=0.05,
    description='Series B Dilution:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

investment_c_widget = widgets.FloatSlider(
    value=20.00,
    min=1.00,
    max=30.00,
    step=0.10,
    description='Series C Investment $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

pre_money_c_widget = widgets.FloatSlider(
    value=100.00,
    min=20.00,
    max=200.00,
    step=1.00,
    description='Series C Pre-Money $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

dilution_c_widget = widgets.FloatSlider(
    value=0.50,
    min=0,
    max=1,
    step=0.05,
    description='Series C Dilution:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

investment_d_widget = widgets.FloatSlider(
    value=25.00,
    min=1.00,
    max=50.00,
    step=0.10,
    description='Series D Investment $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

pre_money_d_widget = widgets.FloatSlider(
    value=150.00,
    min=50.00,
    max=300.00,
    step=1.00,
    description='Series D Pre-Money $ (M):',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

dilution_d_widget = widgets.FloatSlider(
    value=0.50,
    min=0,
    max=1,
    step=0.05,
    description='Series D Dilution:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

return_multiple_widget = widgets.SelectionSlider(
    options=[1, 2, 3, 5],
    value=1,
    description='Return x:',
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

# Widgets for probability of success
prob_success_a_widget = widgets.FloatRangeSlider(
    value=[0.3, 0.7],
    min=0,
    max=1,
    step=0.05,
    description='Prob. of Success Series A:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

prob_success_b_widget = widgets.FloatRangeSlider(
    value=[0.5, 0.8],
    min=0,
    max=1,
    step=0.05,
    description='Prob. of Success Series B:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

prob_success_c_widget = widgets.FloatRangeSlider(
    value=[0.6, 0.8],
    min=0,
    max=1,
    step=0.05,
    description='Prob. of Success Series C:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

prob_success_d_widget = widgets.FloatRangeSlider(
    value=[0.6, 0.9],
    min=0,
    max=1,
    step=0.05,
    description='Prob. of Success Series D:',
    continuous_update=False,
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

# Widgets for participation levels
participation_levels = ['None', '10%', 'Quarter Pro Rata', 'Half Pro Rata', 'Full Pro Rata']

participation_a_widget = widgets.Dropdown(
    options=participation_levels,
    value='Full Pro Rata',
    description='Participation Series A:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

participation_b_widget = widgets.Dropdown(
    options=participation_levels,
    value='Full Pro Rata',
    description='Participation Series B:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

participation_c_widget = widgets.Dropdown(
    options=participation_levels,
    value='Full Pro Rata',
    description='Participation Series C:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

participation_d_widget = widgets.Dropdown(
    options=participation_levels,
    value='Full Pro Rata',
    description='Participation Series D:',
    style={'description_width': 'initial'},
    layout=widgets.Layout(width='300px')
)

# Function to calculate post-dilution ownership
def calculate_post_dilution_ownership(initial_ownership, dilution):
    return initial_ownership * (1 - dilution)

# Function to calculate necessary exit valuation
def calculate_exit_valuation(investment_amount, ownership_percentage, target_return):
    return (target_return * investment_amount) / ownership_percentage

# Function to adjust ownership based on participation level
def adjust_ownership(ownership, participation):
    if participation == 'Full Pro Rata':
        return ownership
    elif participation == 'Half Pro Rata':
        return ownership / 2
    elif participation == 'Quarter Pro Rata':
        return ownership / 4
    elif participation == '10%':
        return ownership / 10
    else:
        return 0

# Function to calculate follow-on investment based on participation level
def calculate_follow_on_investment(required_follow_on, participation):
    if participation == 'Full Pro Rata':
        return required_follow_on
    elif participation == 'Half Pro Rata':
        return required_follow_on / 2
    elif participation == 'Quarter Pro Rata':
        return required_follow_on / 4
    elif participation == '10%':
        return required_follow_on / 10
    else:
        return 0

# Function to perform calculations
# Function to perform calculations
def perform_calculations(scenario_a, investment_amount_a_m, dilution_a, investment_amount_b_m, pre_money_b_m, dilution_b, investment_amount_c_m, pre_money_c_m, dilution_c, investment_amount_d_m, pre_money_d_m, dilution_d, return_multiple, prob_success_a_range, prob_success_b_range, prob_success_c_range, prob_success_d_range, participation_a, participation_b, participation_c, participation_d):
    investment_amount_a = investment_amount_a_m * 1e6  # Convert millions to actual value
    pre_money_valuation_a = scenarios_a[scenario_a]
    post_money_valuation_a = pre_money_valuation_a + investment_amount_a
    series_a_ownership = investment_amount_a / post_money_valuation_a
    
    # Calculate ownership post Series A considering initial dilution from seed round
    founder_ownership_post_series_a = founder_ownership_post_seed * (pre_money_valuation_a / post_money_valuation_a)
    seed_ownership_post_series_a = seed_ownership * (pre_money_valuation_a / post_money_valuation_a)
    post_dilution_ownership_a = calculate_post_dilution_ownership(series_a_ownership, dilution_a)
    
    # Series B calculations
    investment_amount_b = investment_amount_b_m * 1e6
    pre_money_valuation_b = pre_money_b_m * 1e6
    post_money_valuation_b = pre_money_valuation_b + investment_amount_b
    required_follow_on_b = post_dilution_ownership_a * post_money_valuation_b
    follow_on_b = calculate_follow_on_investment(required_follow_on_b, participation_b)
    total_investment_b = investment_amount_b + follow_on_b
    series_b_ownership = total_investment_b / post_money_valuation_b
    founder_ownership_post_series_b = founder_ownership_post_series_a * (pre_money_valuation_b / post_money_valuation_b)
    seed_ownership_post_series_b = seed_ownership_post_series_a * (pre_money_valuation_b / post_money_valuation_b)
    post_dilution_ownership_b = calculate_post_dilution_ownership(series_b_ownership, dilution_b)
    
    # Series C calculations
    investment_amount_c = investment_amount_c_m * 1e6
    pre_money_valuation_c = pre_money_c_m * 1e6
    post_money_valuation_c = pre_money_valuation_c + investment_amount_c
    required_follow_on_c = post_dilution_ownership_b * post_money_valuation_c
    follow_on_c = calculate_follow_on_investment(required_follow_on_c, participation_c)
    total_investment_c = investment_amount_c + follow_on_c
    series_c_ownership = total_investment_c / post_money_valuation_c
    founder_ownership_post_series_c = founder_ownership_post_series_b * (pre_money_valuation_c / post_money_valuation_c)
    seed_ownership_post_series_c = seed_ownership_post_series_b * (pre_money_valuation_c / post_money_valuation_c)
    post_dilution_ownership_c = calculate_post_dilution_ownership(series_c_ownership, dilution_c)

    # Series D calculations
    investment_amount_d = investment_amount_d_m * 1e6
    pre_money_valuation_d = pre_money_d_m * 1e6
    post_money_valuation_d = pre_money_valuation_d + investment_amount_d
    required_follow_on_d = post_dilution_ownership_c * post_money_valuation_d
    follow_on_d = calculate_follow_on_investment(required_follow_on_d, participation_d)
    total_investment_d = investment_amount_d + follow_on_d
    series_d_ownership = total_investment_d / post_money_valuation_d
    founder_ownership_post_series_d = founder_ownership_post_series_c * (pre_money_valuation_d / post_money_valuation_d)
    seed_ownership_post_series_d = seed_ownership_post_series_c * (pre_money_valuation_d / post_money_valuation_d)
    post_dilution_ownership_d = calculate_post_dilution_ownership(series_d_ownership, dilution_d)

    # Total investment across all rounds
    total_investment = investment_amount_a + total_investment_b + total_investment_c + total_investment_d

    # Necessary exit valuation at IPO to achieve the return multiple
    necessary_exit_valuation = calculate_exit_valuation(total_investment, post_dilution_ownership_d, return_multiple)

    # Calculate the combined probability of success
    combined_probability = np.random.uniform(*prob_success_a_range) * np.random.uniform(*prob_success_b_range) * np.random.uniform(*prob_success_c_range) * np.random.uniform(*prob_success_d_range)

    # Calculate the expected value based on probabilities
    expected_value = combined_probability * necessary_exit_valuation

    return necessary_exit_valuation, combined_probability, expected_value, post_dilution_ownership_d, post_money_valuation_a, post_money_valuation_b, post_money_valuation_c, post_money_valuation_d, follow_on_b, follow_on_c, follow_on_d

# Function to update and display the initial table
# Function to update and display the initial table
def update_display_table(scenario_a, investment_amount_a_m, dilution_a, investment_amount_b_m, pre_money_b_m, dilution_b, investment_amount_c_m, pre_money_c_m, dilution_c, investment_amount_d_m, pre_money_d_m, dilution_d, return_multiple, prob_success_a_range, prob_success_b_range, prob_success_c_range, prob_success_d_range, participation_a, participation_b, participation_c, participation_d):
    necessary_exit_valuation, combined_probability, expected_value, post_dilution_ownership_d, post_money_valuation_a, post_money_valuation_b, post_money_valuation_c, post_money_valuation_d, follow_on_b, follow_on_c, follow_on_d = perform_calculations(
        scenario_a, investment_amount_a_m, dilution_a, investment_amount_b_m, pre_money_b_m,
        dilution_b, investment_amount_c_m, pre_money_c_m, dilution_c, investment_amount_d_m,
        pre_money_d_m, dilution_d, return_multiple, prob_success_a_range, prob_success_b_range,
        prob_success_c_range, prob_success_d_range, participation_a, participation_b, participation_c,
        participation_d
    )


    # Create DataFrame for the result
    result_df = pd.DataFrame([
        {
            'Round': 'Seed',
            'Investment': f"${seed_investment/1e6:,.2f}M",
            'Post-Money Valuation': 'N/A',
            'Dilution Level': 'N/A',
            'Ownership %': seed_ownership * 100,
            'Participation': 'N/A'
        },
        {
            'Round': 'Series A',
            'Investment': f"${investment_amount_a_m:,.2f}M",
            'Post-Money Valuation': f"${post_money_valuation_a / 1e6:,.2f}M",
            'Dilution Level': f"{int(dilution_a * 100)}%",
            'Ownership %': (investment_amount_a_m * 1e6 / post_money_valuation_a) * 100,
            'Participation': participation_a
        },
        {
            'Round': 'Series B',
            'Investment': f"${investment_amount_b_m:,.2f}M",
            'Follow-On': f"${follow_on_b / 1e6:,.2f}M",
            'Post-Money Valuation': f"${post_money_valuation_b / 1e6:,.2f}M",
            'Dilution Level': f"{int(dilution_b * 100)}%",
            'Ownership %': (investment_amount_b_m * 1e6 / post_money_valuation_b) * 100,
            'Participation': participation_b
        },
        {
            'Round': 'Series C',
            'Investment': f"${investment_amount_c_m:,.2f}M",
            'Follow-On': f"${follow_on_c / 1e6:,.2f}M",
            'Post-Money Valuation': f"${post_money_valuation_c / 1e6:,.2f}M",
            'Dilution Level': f"{int(dilution_c * 100)}%",
            'Ownership %': (investment_amount_c_m * 1e6 / post_money_valuation_c) * 100,
            'Participation': participation_c
        },
        {
            'Round': 'Series D',
            'Investment': f"${investment_amount_d_m:,.2f}M",
            'Follow-On': f"${follow_on_d / 1e6:,.2f}M",
            'Post-Money Valuation': f"${post_money_valuation_d / 1e6:,.2f}M",
            'Dilution Level': f"{int(dilution_d * 100)}%",
            'Ownership %': (investment_amount_d_m * 1e6 / post_money_valuation_d) * 100,
            'Participation': participation_d
        },
        {
            'Round': 'Post-IPO',
            'Investment': 'N/A',
            'Post-Money Valuation': f"${necessary_exit_valuation / 1e6:,.2f}M",
            'Dilution Level': 'N/A',
            'Ownership %': post_dilution_ownership_d * 100,
            'Participation': 'N/A'
        },
        {
            'Round': 'Expected Value',
            'Investment': 'N/A',
            'Post-Money Valuation': f"${expected_value / 1e6:,.2f}M",
            'Dilution Level': 'N/A',
            'Ownership %': 'N/A',
            'Participation': 'N/A'
        }
    ])

    # Highlight each series with different colors
    def highlight_rounds(row):
        if row['Round'] == 'Seed':
            return ['background-color: lightblue'] * len(row)
        elif row['Round'] == 'Series A':
            return ['background-color: lightgreen'] * len(row)
        elif row['Round'] == 'Series B':
            return ['background-color: lightyellow'] * len(row)
        elif row['Round'] == 'Series C':
            return ['background-color: lightcoral'] * len(row)
        elif row['Round'] == 'Series D':
            return ['background-color: lightpink'] * len(row)
        elif row['Round'] == 'Expected Value':
            return ['background-color: lightgrey'] * len(row)
        else:
            return ['background-color: white'] * len(row)

    # Display the result
    styled_df = result_df.style.apply(highlight_rounds, axis=1)
    display(styled_df)

# Monte Carlo Simulation Function
# Monte Carlo Simulation Function
def monte_carlo_simulation(scenario_a, investment_amount_a_m, dilution_a, investment_amount_b_m, pre_money_b_m, dilution_b, investment_amount_c_m, pre_money_c_m, dilution_c, investment_amount_d_m, pre_money_d_m, dilution_d, return_multiple, prob_success_a_range, prob_success_b_range, prob_success_c_range, prob_success_d_range, participation_a, participation_b, participation_c, participation_d, num_simulations=10000):
    outcomes = []

    for _ in range(num_simulations):
        necessary_exit_valuation, combined_probability, expected_value, post_dilution_ownership_d, post_money_valuation_a, post_money_valuation_b, post_money_valuation_c, post_money_valuation_d, follow_on_b, follow_on_c, follow_on_d = perform_calculations(
            scenario_a, investment_amount_a_m, dilution_a, investment_amount_b_m, pre_money_b_m,
            dilution_b, investment_amount_c_m, pre_money_c_m, dilution_c, investment_amount_d_m,
            pre_money_d_m, dilution_d, return_multiple, prob_success_a_range, prob_success_b_range,
            prob_success_c_range, prob_success_d_range, participation_a, participation_b, participation_c,
            participation_d
        )

        outcomes.append(expected_value)

    outcomes = np.array(outcomes)
    
    plt.hist(outcomes / 1e6, bins=50, edgecolor='k')
    plt.title('Monte Carlo Simulation of Expected Value')
    plt.xlabel('Expected Value ($M)')
    plt.ylabel('Frequency')
    plt.show()
    
    print(f"Mean Expected Value: ${np.mean(outcomes) / 1e6:.2f}M")
    print(f"Standard Deviation: ${np.std(outcomes) / 1e6:.2f}M")
    print(f"5th Percentile: ${np.percentile(outcomes, 5) / 1e6:.2f}M")
    print(f"95th Percentile: ${np.percentile(outcomes, 95) / 1e6:.2f}M")


# Interactive output
output = widgets.interactive_output(update_display_table, {
    'scenario_a': scenario_a_widget,
    'investment_amount_a_m': investment_a_widget,
    'dilution_a': dilution_a_widget,
    'investment_amount_b_m': investment_b_widget,
    'pre_money_b_m': pre_money_b_widget,
    'dilution_b': dilution_b_widget,
    'investment_amount_c_m': investment_c_widget,
    'pre_money_c_m': pre_money_c_widget,
    'dilution_c': dilution_c_widget,
    'investment_amount_d_m': investment_d_widget,
    'pre_money_d_m': pre_money_d_widget,
    'dilution_d': dilution_d_widget,
    'return_multiple': return_multiple_widget,
    'prob_success_a_range': prob_success_a_widget,
    'prob_success_b_range': prob_success_b_widget,
    'prob_success_c_range': prob_success_c_widget,
    'prob_success_d_range': prob_success_d_widget,
    'participation_a': participation_a_widget,
    'participation_b': participation_b_widget,
    'participation_c': participation_c_widget,
    'participation_d': participation_d_widget
})

# Monte Carlo Simulation Button
monte_carlo_button = widgets.Button(description="Run Monte Carlo Simulation", layout=widgets.Layout(width='300px'))
monte_carlo_output = widgets.Output()

def on_monte_carlo_button_clicked(b):
    with monte_carlo_output:
        monte_carlo_output.clear_output()
        monte_carlo_simulation(
            scenario_a_widget.value, investment_a_widget.value, dilution_a_widget.value,
            investment_b_widget.value, pre_money_b_widget.value, dilution_b_widget.value,
            investment_c_widget.value, pre_money_c_widget.value, dilution_c_widget.value,
            investment_d_widget.value, pre_money_d_widget.value, dilution_d_widget.value,
            return_multiple_widget.value, prob_success_a_widget.value, prob_success_b_widget.value,
            prob_success_c_widget.value, prob_success_d_widget.value, participation_a_widget.value,
            participation_b_widget.value, participation_c_widget.value, participation_d_widget.value
        )

monte_carlo_button.on_click(on_monte_carlo_button_clicked)

# Organize widgets into columns
column1 = widgets.VBox([
    scenario_a_widget, investment_a_widget, dilution_a_widget,
    prob_success_a_widget, participation_a_widget
])

column2 = widgets.VBox([
    investment_b_widget, pre_money_b_widget, dilution_b_widget,
    prob_success_b_widget, participation_b_widget
])

column3 = widgets.VBox([
    investment_c_widget, pre_money_c_widget, dilution_c_widget,
    prob_success_c_widget, participation_c_widget
])

column4 = widgets.VBox([
    investment_d_widget, pre_money_d_widget, dilution_d_widget,
    prob_success_d_widget, participation_d_widget, return_multiple_widget
])

# Display widgets in columns
widgets_box = widgets.HBox([column1, column2, column3, column4])

# Display widgets and output
display(widgets_box, output, monte_carlo_button, monte_carlo_output)
