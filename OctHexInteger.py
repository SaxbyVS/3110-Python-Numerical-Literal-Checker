from LiteralChecker import NFA, string

## NFA for octal and hex integers

#redundantdelete
#function adds transitions to given transitions dictionary from a state to every given next state with every symbol
def add_transitions(transitions_dict, state, symbols, next_states):
    if state not in transitions_dict:
        transitions_dict[state] = dict()
    for i in symbols:
        transitions_dict.get(state).update({i: next_states})

#helper sets
non_zero_digits = [str(digit) for digit in range(1, 10)]
decimal_digits = [str(digit) for digit in range(10)]
hex_digits = list(string.hexdigits)
octal_digits = list(string.octdigits)
binary_digits = ['0','1']

states = {'q0','q1','q2','q3', 'q4'}
alphabet = {'0','1','2','3','4','5','6','7','8','9','_'}
transitions = {
    'q0':{'0': {'q1'},}
}
add_transitions(transitions, 'q1', {'x', 'X'}, {'hexint'})

add_transitions(transitions, 'hexint', {'', '_'}, {'h1'})
add_transitions(transitions, 'h1', hex_digits, {'haccept'})
add_transitions(transitions, 'haccept', {''}, {'hexint'})

add_transitions(transitions, 'q1', {'o', 'O'}, {'octint'})

add_transitions(transitions, 'octint', {'', '_'}, {'o1'})
add_transitions(transitions, 'o1', octal_digits, {'oaccept'})
add_transitions(transitions, 'oaccept', {''}, {'octint'})

start_state = 'q0'
accept_states = {'haccept','oaccept'}

hex_oct_nfa = NFA(states, alphabet, transitions, start_state, accept_states)


##Testing

userInput = input()
print(hex_oct_nfa.accepts(userInput))
print(hex_oct_nfa.accepts("0xabcd10_1_1"))
print(hex_oct_nfa.accepts("0oabcd10_1_1"))
print(hex_oct_nfa.accepts("0o1010"))
print(hex_oct_nfa.accepts("0O1010"))
print("hi")

# works perfectly
# DecInt.fileTest('in.txt', "out.txt")