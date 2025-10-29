data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

# Separate the data by class
yes_data = [row for row in data if row[-1] == 'Yes']
no_data = [row for row in data if row[-1] == 'No']

# Helper function to calculate P(feature=value | class)
def prob(index, value, subset):
    count = sum(1 for row in subset if row[index] == value)
    return count / len(subset)

# Naive Bayes prediction
def predict(outlook, temperature, humidity, wind):
    total_yes = len(yes_data) / len(data)
    total_no = len(no_data) / len(data)

    # Likelihoods for "Yes" and "No"
    p_yes = (prob(0, outlook, yes_data) *
             prob(1, temperature, yes_data) *
             prob(2, humidity, yes_data) *
             prob(3, wind, yes_data) *
             total_yes)

    p_no = (prob(0, outlook, no_data) *
            prob(1, temperature, no_data) *
            prob(2, humidity, no_data) *
            prob(3, wind, no_data) *
            total_no)

    return 'Yes' if p_yes > p_no else 'No'

# Test sample
test = ['Sunny', 'Cool', 'High', 'Strong']
print("Prediction:", predict(*test))
