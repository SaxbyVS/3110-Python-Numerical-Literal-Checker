from LiteralChecker import NFA

## NFA for floating-point numbers

states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E', '+', '-'}
transitions = {
    'q0': {str(d): {'q1'} for d in range(10)} | {'.': {'q3'}},
    'q1': {str(d): {'q1'} for d in range(10)} | {'.': {'q2'}},
    'q2': {str(d): {'q2'} for d in range(10)} | {'e': {'q4'}, 'E': {'q4'}},
    'q3': {str(d): {'q2'} for d in range(10)},
    'q4': {'+': {'q5'}, '-': {'q5'}} | {str(d): {'q6'} for d in range(10)},
    'q5': {str(d): {'q6'} for d in range(10)},
    'q6': {str(d): {'q6'} for d in range(10)},
}
start_state = 'q0'
accept_states = {'q1', 'q2', 'q6'}

FloatNFA = NFA(states, alphabet, transitions, start_state, accept_states)

## Testing
userInput = input()
print(FloatNFA.accepts(userInput))

# File test
# FloatNFA.fileTest('in.txt', 'out.txt')