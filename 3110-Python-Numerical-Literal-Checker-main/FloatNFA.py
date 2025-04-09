from LiteralChecker import NFA

## NFA for floating-point numbers

states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E', '_', '-'}
transitions = {
    'q0': {str(d): {'q1'} for d in range(10)} | {'-': {'q0'}},
    'q1': {str(d): {'q1'} for d in range(10)} | {'.': {'q2'}} | {'_': {'q3'}},
    'q2': {str(d): {'q2'} for d in range(10)} | {'_': {'q3'}},
    'q3': {'_': {'q7'}} | {'E': {'q4'}} | {'e': {'q4'}} ,
    'q4': {'_': {'q5'}} | {'-': {'q5'}},
    'q5': {str(d): {'q6'} for d in range(10)},
    'q6': {str(d): {'q6'} for d in range(10)} | {'_': {'q7'}},
}
start_state = 'q0'
accept_states = {'q7'''}

FloatNFA = NFA(states, alphabet, transitions, start_state, accept_states)

## Testing
userInput = input()
print(FloatNFA.accepts(userInput))

# File test
# FloatNFA.fileTest('in.txt', 'out.txt')