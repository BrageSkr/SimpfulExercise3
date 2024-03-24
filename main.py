import matplotlib.pyplot as plt
from simpful import *
from mpl_toolkits.mplot3d import Axes3D

FS = FuzzySystem()

# Define fuzzy sets and linguistic variables for the inputs
FS.add_linguistic_variable("delay", LinguisticVariable(
    [
        FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.1, d=0.3), term="VS"),
        FuzzySet(function=Triangular_MF(a=0.1, b=0.3, c=0.5), term="S"),
        FuzzySet(function=Trapezoidal_MF(a=0.4, b=0.6, c=0.7, d=0.7), term="M")
    ],
    concept="delay",
    universe_of_discourse=[0, 0.7]
))

FS.add_linguistic_variable("server", LinguisticVariable(
    [
        FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.2, d=0.3), term="S"),
        FuzzySet(function=Triangular_MF(a=0.15, b=0.3, c=0.45), term="RS"),
        FuzzySet(function=Triangular_MF(a=0.3, b=0.5, c=0.7), term="M"),
        FuzzySet(function=Triangular_MF(a=0.55, b=0.7, c=0.85), term="RL"),
        FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.8, c=1,d=1), term="L"),

    ],
    concept="server",
    universe_of_discourse=[0, 1]
))

FS.add_linguistic_variable("repair", LinguisticVariable(
    [
        FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.4, d=0.6), term="L"),
        FuzzySet(function=Triangular_MF(a=0.4, b=0.6, c=0.8), term="M"),
        FuzzySet(function=Trapezoidal_MF(a=0.6, b=0.8, c=1, d=1), term="H")
    ],
    concept="repair",
    universe_of_discourse=[0, 1]
))

# Define fuzzy sets and linguistic variable for the output
FS.add_linguistic_variable("output", LinguisticVariable(
    [
        FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=0.1, d=0.3 ), term="VS"),
        FuzzySet(function=Triangular_MF(a=0, b=0.2, c=0.4), term="S"),
        FuzzySet(function=Triangular_MF(a=0.25, b=0.35, c=0.45), term="RS"),
        FuzzySet(function=Triangular_MF(a=0.3, b=0.5, c=0.7), term="M"),
        FuzzySet(function=Triangular_MF(a=0.55, b=0.65, c=0.75), term="RL"),
        FuzzySet(function=Triangular_MF(a=0.6, b=0.8, c=1), term="L"),
        FuzzySet(function=Trapezoidal_MF(a=0.7, b=0.9, c=1, d=1), term="VL")
    ],
    universe_of_discourse=[0, 1]
))

# Define fuzzy rules
FS.add_rules([
    "IF (delay IS VS) AND (server IS S) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS VS) AND (server IS RS) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS VS) AND (server IS M) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS VS) AND (server IS RL) AND (repair IS L) THEN (output IS S)",
    "IF (delay IS VS) AND (server IS L) AND (repair IS L) THEN (output IS S)",
    "IF (delay IS S) AND (server IS S) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS S) AND (server IS RS) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS S) AND (server IS M) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS S) AND (server IS RL) AND (repair IS L) THEN (output IS S)",
    "IF (delay IS S) AND (server IS L) AND (repair IS L) THEN (output IS S)",
    "IF (delay IS M) AND (server IS S) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS RS) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS M) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS RL) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS L) AND (repair IS L) THEN (output IS VS)",
    "IF (delay IS VS) AND (server IS S) AND (repair IS M) THEN (output IS S)",
    "IF (delay IS VS) AND (server IS RS) AND (repair IS M) THEN (output IS S)",
    "IF (delay IS VS) AND (server IS M) AND (repair IS M) THEN (output IS RS)",
    "IF (delay IS VS) AND (server IS RL) AND (repair IS M) THEN (output IS M)",
    "IF (delay IS VS) AND (server IS L) AND (repair IS M) THEN (output IS M)",
    "IF (delay IS S) AND (server IS S) AND (repair IS M) THEN (output IS VS)",
    "IF (delay IS S) AND (server IS RS) AND (repair IS M) THEN (output IS VS)",
    "IF (delay IS S) AND (server IS M) AND (repair IS M) THEN (output IS S)",
    "IF (delay IS S) AND (server IS RL) AND (repair IS M) THEN (output IS RS)",
    "IF (delay IS S) AND (server IS L) AND (repair IS M) THEN (output IS RS)",
    "IF (delay IS M) AND (server IS S) AND (repair IS M) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS RS) AND (repair IS M) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS M) AND (repair IS M) THEN (output IS VS)",
    "IF (delay IS M) AND (server IS RL) AND (repair IS M) THEN (output IS S)",
    "IF (delay IS M) AND (server IS L) AND (repair IS M) THEN (output IS S)",
    "IF (delay IS VS) AND (server IS S) AND (repair IS H) THEN (output IS VL)",
    "IF (delay IS VS) AND (server IS RS) AND (repair IS H) THEN (output IS VL)",
    "IF (delay IS VS) AND (server IS M) AND (repair IS H) THEN (output IS M)",
    "IF (delay IS VS) AND (server IS RL) AND (repair IS H) THEN (output IS RL)",
    "IF (delay IS VS) AND (server IS L) AND (repair IS H) THEN (output IS L)",
    "IF (delay IS S) AND (server IS S) AND (repair IS H) THEN (output IS L)",
    "IF (delay IS S) AND (server IS RS) AND (repair IS H) THEN (output IS RL)",
    "IF (delay IS S) AND (server IS M) AND (repair IS H) THEN (output IS M)",
    "IF (delay IS S) AND (server IS RL) AND (repair IS H) THEN (output IS M)",
    "IF (delay IS S) AND (server IS L) AND (repair IS H) THEN (output IS M)",
    "IF (delay IS M) AND (server IS S) AND (repair IS H) THEN (output IS M)",
    "IF (delay IS M) AND (server IS RS) AND (repair IS H) THEN (output IS RS)",
    "IF (delay IS M) AND (server IS M) AND (repair IS H) THEN (output IS S)",
    "IF (delay IS M) AND (server IS RL) AND (repair IS H) THEN (output IS RS)",
    "IF (delay IS M) AND (server IS L) AND (repair IS H) THEN (output IS RS)",
    # Add more rules as needed
])

# Set antecedents values
FS.set_variable("delay", 0.5)
FS.set_variable("server", 0.5)
FS.set_variable("repair", 0.5)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["output"]))
FS.plot_variable("delay")
FS.plot_variable("server")
FS.plot_variable("repair")
FS.plot_variable("output")
FS.plot_surface(["server","delay"],"output")
FS.plot_surface(["delay","repair"],"output")