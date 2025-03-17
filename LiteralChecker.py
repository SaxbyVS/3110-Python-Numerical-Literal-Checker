import string
class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions  # {state: {symbol: {next_states}}}
        self.start_state = start_state
        self.accept_states = accept_states

    def addTransitions(self, state, transition_list):
        for i in transition_list:
            self.transitions[state].add(i)

    def _epsilon_closure(self, states):
        """Find the epsilon closure of a set of states."""
        stack = list(states)
        closure = set(states)
        while stack:
            state = stack.pop()
            if '' in self.transitions.get(state, {}):  # Epsilon transition
                for next_state in self.transitions[state]['']:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
        return closure

    def accepts(self, input_string):
        """Check if the NFA accepts the input string."""
        current_states = self._epsilon_closure({self.start_state})
        for symbol in input_string:
            next_states = set()
            for state in current_states:
                if symbol in self.transitions.get(state, {}):
                    next_states.update(self.transitions[state][symbol])
            current_states = self._epsilon_closure(next_states)
        return bool(current_states & self.accept_states)

    def fileTest(self, filename):
        """reads batch file and returns expected result and tested actual result"""
        inputs = []
        with open(filename) as f:
            for i in f:
                i = i.rstrip()
                parts = i.rsplit(' ', 1)
                if len(parts) == 2 and parts[1].lower() in {'true', 'false'}:
                    inputs.append((parts[0], parts[1]))
        # print(inputs)
        for inp in inputs:
            print(inp[0]+" -- Expected: "+inp[1]+" -- Actual: "+str(self.accepts(inp[0])))


##Testing Example
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transitions = {
    'q0': {'a': {'q0', 'q1'}},
    'q1': {'b': {'q2'}},
    'q2': {}
}
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)
print(nfa.accepts("aab"))  # True
print(nfa.accepts("aba"))  # False

nfa.fileTest("in.txt")
## end of example

#function adds transitions to given transitions dictionary from a state to every given next state with every symbol
def add_transitions(transitions_dict, state, symbols, next_states):
    if state not in transitions_dict:
        transitions_dict[state] = dict()
    for i in symbols:
        transitions_dict.get(state).update({i: next_states})

#define sets
non_zero_digits = [str(digit) for digit in range(1, 10)]
decimal_digits = [str(digit) for digit in range(10)]
hex_digits = list(string.hexdigits)
octal_digits = list(string.octdigits)
binary_digits = ['0','1']

intlit_states = {'q0', 'q1', 'q2'}
intlit_alphabet = set(string.hexdigits)
intlit_alphabet.update('o','O','x','X')
intlit_transitions = {}
#todo create nfa transitions:
add_transitions(intlit_transitions, 'decint', non_zero_digits, {'q5'})
add_transitions(intlit_transitions, 'q0', {''}, {'nondecprefix', 'decint'})
add_transitions(intlit_transitions, 'q5', {'0'}, {'final'})
intlit_start = 'q0'
intlit_accept = {'final'}


intlit_nfa = NFA(intlit_states, intlit_alphabet, intlit_transitions, intlit_start, intlit_accept)
print(intlit_nfa.accepts("1b"))
print(intlit_nfa.accepts("20"))
print(intlit_nfa.accepts("21"))
