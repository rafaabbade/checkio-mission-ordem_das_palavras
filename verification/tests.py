"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        [
    {
        "input": ["Eu gosto de programar em Python", ["gosto", "programar"]],
        "answer": true
    },
    {
        "input": ["Eu gosto de programar em Python", ["programar", "gosto"]],
        "answer": false
    }
]
    ]
}
